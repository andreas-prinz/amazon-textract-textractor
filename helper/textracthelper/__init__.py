__version__ = '0.0.3'

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())