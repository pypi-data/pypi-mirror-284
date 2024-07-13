import torch
import torch.nn as nn
from torch.optim import Optimizer
from tortreinador.utils.metrics import r2_score, mixture
from tqdm import tqdm
from tortreinador.utils.Recorder import Recorder
from tortreinador.utils.WarmUpLR import WarmUpLR
from tortreinador.utils.View import visualize_lastlayer, visualize_train_loss, visualize_test_loss
from tensorboardX import SummaryWriter


class TorchTrainer:
    """
        The train loop based on pytorch

        Args:
            - is_gpu (bool): whether to use GPU or not
            - epoch (int): number of epochs to train for
            - log_dir (str): directory
            - model (torch.nn.Module):
            - optimizer (torch.optim.Optimizer):
            - extra_metric (torch.nn.Module):
            - criterion (torch.nn.Module):

    """

    def __init__(self,
                 is_gpu: bool = True,
                 epoch: int = 150, log_dir: str = None, model: nn.Module = None,
                 optimizer: Optimizer = None, extra_metric: nn.Module = None, criterion: nn.Module = None):

        if not isinstance(model, nn.Module) or not isinstance(optimizer, Optimizer) or not isinstance(criterion,
                                                                                                      nn.Module) or epoch is None:
            raise ValueError("Please provide the correct type of model, optimizer, criterion and the not none epoch")

        self.epoch = epoch
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion

        self.device = torch.device('cuda' if is_gpu and torch.cuda.is_available() else 'cpu')
        self.writer = SummaryWriter(log_dir=log_dir) if log_dir is not None else log_dir

        self.train_loss_recorder = Recorder(self.device.type)
        self.val_loss_recorder = Recorder(self.device.type)
        self.train_metric_recorder = Recorder(self.device.type)
        self.val_metric_recorder = Recorder(self.device.type)

        if extra_metric is not None:
            self.extra_metric = extra_metric
            self.extra_recorder = Recorder(self.device.type)

        self.epoch_train_loss = Recorder(self.device.type)
        self.epoch_val_loss = Recorder(self.device.type)
        self.epoch_train_metric = Recorder(self.device.type)
        self.epoch_val_metric = Recorder(self.device.type)
        self.epoch_extra_metric = None

        if 'extra_metric' in self.__dict__:
            self.epoch_extra_metric = Recorder(self.device.type)

        print("Epoch:{}, is GPU: {}".format(epoch, is_gpu))

    def calculate(self, x, y, mode='t'):

        pi, mu, sigma = self.model(x)

        loss = self.criterion(pi, mu, sigma, y)

        pdf = mixture(pi, mu, sigma)

        y_pred = pdf.sample()

        metric_per = r2_score(y, y_pred)

        return self._standard_return(loss, metric_per, mode, y, y_pred)

    def _standard_return(self, loss, metric_per, mode, y, y_pred):

        if mode == 't':
            return [loss, metric_per, 't']

        elif mode == 'v' and 'extra_metric' in self.__dict__:
            return [loss, metric_per, y, y_pred, 'v']

        elif mode == 'v':
            return [loss, metric_per, 'v']

    def cal_result(self, *args):
        if args[-1] == 't':
            self.train_loss_recorder.update(args[0])
            self.train_metric_recorder.update(args[1])
            return {
                'loss': (self.train_loss_recorder.val[-1].item(), '.4f'),
                'loss_avg': (self.train_loss_recorder.avg().item(), '.4f'),
                'train_metric': (self.train_metric_recorder.avg().item(), '.4f')
            }, args[0]

        elif args[-1] == 'v':
            self.val_loss_recorder.update(args[0])
            self.val_metric_recorder.update(args[1])
            if len(args[:-1]) == 4:
                self.extra_recorder.update(self.extra_metric(args[2], args[3]))
                return {
                    'loss': (self.val_loss_recorder.val[-1].item(), '.4f'),
                    'loss_avg': (self.val_loss_recorder.avg().item(), '.4f'),
                    'val_metric': (self.val_metric_recorder.avg().item(), '.4f'),
                    'extra_metric': (self.extra_recorder.avg().item(), '.4f')
                }

            else:
                return {
                    'loss': (self.val_loss_recorder.val[-1].item(), '.4f'),
                    'loss_avg': (self.val_loss_recorder.avg().item(), '.4f'),
                    'val_metric': (self.val_metric_recorder.avg().item(), '.4f'),
                }


    def _check_best_metric_for_regression(self, b_m):

        """
                Parameter Check

                Args:
                    - param b_m: A param like R-Square, this param is used to judging the model can be save or not

                    - return: bool: Whether the metric is best or not
        """

        if b_m >= 1.0:
            return False

        else:
            return True

    def _check_param_exist(self, b_m):
        if b_m is not None:
            return True

        else:
            return False


    def fit(self, t_l, v_l, **kwargs):
        """
            Args:
                - param t_l: training data loader
                - param v_l: validation data loader
                - kwargs:
                    - m_p (str): model save path
                    - w_e (int): Epochs of warm up
                    - l_m (dict): lr_milestones and gamma(option) e.g. 'l_m': {
                                                                                's_l': [20, 40],
                                                                                'gamma': 0.7
                                                                            }
                    - b_m (float): best metric(e.g. r2), this param is used to judging the model can be saved

        """
        if not self._check_param_exist(kwargs['b_m']):
            raise ValueError('Best metric does not exist')

        else:
            if not self._check_best_metric_for_regression(kwargs['b_m']):
                raise ValueError("Best metric can't higher than 1.0")

        IS_WARMUP = False
        IS_LR_MILESTONE = False

        self.model = nn.DataParallel(self.model)

        self.model.to(self.device)
        self.criterion.to(self.device)

        # Schedular 1
        if 'w_e' in kwargs.keys():
            IS_WARMUP = True
            warmup = WarmUpLR(self.optimizer, len(t_l) * kwargs['w_e'])

        # Schedular 2
        if 'l_m' in kwargs.keys():
            IS_LR_MILESTONE = True
            lr_schedular = torch.optim.lr_scheduler.MultiStepLR(self.optimizer,
                                                                milestones=kwargs['l_m']['s_l'],
                                                                gamma=kwargs['l_m']['gamma'])

        for name, parameters in self.model.named_parameters():
            print(name, ':', parameters.size())

        # Epoch
        for e in range(self.epoch):

            self.model.train()

            if IS_WARMUP is True and IS_LR_MILESTONE is True and e >= kwargs['w_e']:
                lr_schedular.step()

            # lr_schedular.step()

            i = 0

            with tqdm(t_l, unit='batch') as t_epoch:
                for x, y in t_epoch:
                    if IS_WARMUP is True and e < kwargs['w_e']:
                        warmup.step()
                    t_epoch.set_description(f"Epoch {e + 1} Training")

                    mini_batch_x = x.to(self.device)
                    mini_batch_y = y.to(self.device)
                    self.optimizer.zero_grad()

                    param_options, loss = self.cal_result(*self.calculate(mini_batch_x, mini_batch_y, mode='t'))

                    param_options['lr'] = (self.optimizer.state_dict()['param_groups'][0]['lr'], '.6f')

                    params = {key: "{value:{format}}".format(value=value, format=f)
                              for key, (value, f) in param_options.items()}

                    loss.backward()

                    self.optimizer.step()

                    if self.writer is not None:
                        n_iter = (e - 1) * len(t_l) + i + 1
                        visualize_lastlayer(self.writer, self.model, n_iter)
                        visualize_train_loss(self.writer, loss.item(), n_iter)

                    t_epoch.set_postfix(**params)

                # epoch_train_metric.append(self.train_metric_recorder.avg)
                # epoch_train_loss.append(self.train_loss_recorder.avg)

                self.epoch_train_metric.update(self.train_metric_recorder.avg())
                self.epoch_train_loss.update(self.train_loss_recorder.avg())


            with torch.no_grad():
                self.model.eval()

                with tqdm(v_l, unit='batch') as v_epoch:
                    v_epoch.set_description(f"Epoch {e + 1} Validating")

                    for v_x, v_y in v_epoch:
                        val_batch_x = v_x.to(self.device)
                        val_batch_y = v_y.to(self.device)

                        param_options = self.cal_result(*self.calculate(val_batch_x, val_batch_y, mode='v'))

                        params = {key: "{value:{format}}".format(value=value, format=f)
                                  for key, (value, f) in param_options.items()}

                        v_epoch.set_postfix(**params)

                self.epoch_val_loss.update(self.val_loss_recorder.avg())
                self.epoch_val_metric.update(self.val_metric_recorder.avg())

                if self.epoch_extra_metric is not None:
                    self.epoch_extra_metric.update(self.extra_recorder.avg())

                if self.writer is not None:
                    visualize_test_loss(self.writer, self.epoch_val_loss.val[-1], e)

                if self.val_metric_recorder.avg().item() > kwargs['b_m']:
                    kwargs['b_m'] = self.val_metric_recorder.avg().item()

                    if 'm_p' in kwargs.keys():
                        torch.save(self.model.state_dict(), '{}best_model.pth'.format(kwargs['m_p']))

                        print("Save Best model: Metric:{:.4f}, Loss Avg:{:.4f}".format(self.val_metric_recorder.avg().item(),
                                                                                   self.val_loss_recorder.avg().item()))

                    else:
                        print("Best model: R2:{:.4f}, Loss Avg:{:.4f}".format(self.val_metric_recorder.avg().item(),
                                                                              self.val_loss_recorder.avg().item()))

            self.train_loss_recorder.reset()
            self.val_loss_recorder.reset()
            self.train_metric_recorder.reset()
            self.val_metric_recorder.reset()
            if 'extra_metric' in self.__dict__:
                self.extra_recorder = self.extra_recorder.reset()

            if IS_WARMUP is False and IS_LR_MILESTONE is True:
                lr_schedular.step()

        if 'extra_metric' in self.__dict__:
            return self.epoch_train_loss, self.epoch_val_loss, self.epoch_val_metric, self.epoch_train_metric, self.epoch_extra_metric

        else:
            return self.epoch_train_loss, self.epoch_val_loss, self.epoch_val_metric, self.epoch_train_metric
