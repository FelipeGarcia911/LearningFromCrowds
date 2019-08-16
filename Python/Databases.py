import os
import numpy as np
import pandas as pd

def get_databases_path(databases_path):
    paths = list()
    ignore_path = ['.', 'Icon', ]
    for filename in os.listdir(databases_path):
        if any(path in filename for path in ignore_path):
            pass
        else:
            folder = databases_path + '/' + filename
            paths.append(folder)
    return paths

def get_database(path_info, filename):
    file_name = path_info + '/' + filename 
    return pd.read_csv(file_name, sep=',')