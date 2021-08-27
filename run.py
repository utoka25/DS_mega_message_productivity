# import sys
# import os

import papermill as pm

# src_path = os.path.dirname(os.path.abspath(__file__))+'/src/'
# data_path = os.path.dirname(os.path.abspath(__file__))+'/data/'
#
# sys.path.insert(0, src_path)
# sys.path.insert(0, data_path)

pm.execute_notebook(
   'src/message_productivity.ipynb',
   'src/out.ipynb'
)

