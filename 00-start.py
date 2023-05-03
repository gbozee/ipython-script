from IPython import get_ipython
ipython = get_ipython()

if '__IPYTHON__' in globals():
    ipython.magic('load_ext autoreload')
    ipython.magic('autoreload 2')

from example.webhook import *
from example.long_t_trades import *
from example.auto_future import *

Account = service_instance.service.Account