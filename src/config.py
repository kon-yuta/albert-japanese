from dotenv import load_dotenv
load_dotenv()

import os
EXTRACTDIR            = os.getenv('EXTRACTDIR')
PRETRAINED_MODEL_PATH = os.getenv('PRETRAINED_MODEL_PATH')
FINETUNE_OUTPUT_DIR   = os.getenv('FINETUNE_OUTPUT_DIR')

#  import config
#  EXTRACTDIR = config.EXTRACTDIR
#  PRETRAINED_MODEL_PATH = config.PRETRAINED_MODEL_PATH
#  FINETUNE_OUTPUT_DIR = config.FINETUNE_OUTPUT_DIR
