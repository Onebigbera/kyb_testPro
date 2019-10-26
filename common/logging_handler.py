# -*-coding:utf-8 -*-
# File :logging_driver_.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    logging
"""

import logging.config
import os

# get config file path
root_dir = os.path.dirname(os.path.dirname(__file__))
config_path = '/'.join((root_dir, 'config', 'log.conf'))

# instance logging
CON_LOG = config_path
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
