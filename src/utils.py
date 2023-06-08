import os
import sys

import pandas as pd
import numpy

import dill

from src.exception import CustomException
def save_object(file_path, obj):
    '''
        Why this function is for (Will Write Later)
    '''
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)