# -*- coding: utf-8 -*-

import os

def get_data_dir():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = curr_dir+"/../../../../data"

    return(data_dir)

def get_output_dir():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = curr_dir+"/../../../../output"

    return(output_dir)