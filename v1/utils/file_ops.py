import os
import pandas as pd
import tkinter.filedialog as fd

ext_ = {'csv':pd.read_csv,
        'xml':pd.read_xml,
        'json':pd.read_json,
        'parquet':pd.read_parquet}


def rec_file(filepath_):
    file_ext = os.path.basename(filepath_)
    
    return file_ext.split('.')[-1]


def open_file(filepath_):
    
    try:
        file_ext = os.path.exists(filepath_)
        
    except FileNotFoundError:
        print(f'File {filepath_} does not exist.')

    filetype_ = rec_file(filepath_)

    for key_ in ext_:
        if filetype_ in key_:
            dataset_ = ext_[key_](filepath_)

    return dataset_