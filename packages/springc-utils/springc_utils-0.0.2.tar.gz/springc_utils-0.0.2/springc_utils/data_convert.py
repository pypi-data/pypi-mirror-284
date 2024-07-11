import torch
import numpy as np

def toTensor(a, cuda=None):
    if isinstance(a, torch.Tensor):
        pass
    else:
        a = torch.from_numpy(np.asarray(a))
    return a.cuda() if cuda else a

def toNumpy(a):
    if isinstance(a, torch.Tensor):
        return a.detach().cpu().numpy()
    else:
        return np.asarray(a)