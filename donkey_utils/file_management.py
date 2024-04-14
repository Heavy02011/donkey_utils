# http://docs.donkeycar.com/dev_guide/model/
import os
import tarfile
import numpy as np
from donkeycar.parts.tub_v2 import Tub
from donkeycar.pipeline.types import TubRecord
from donkeycar.config import load_config

import random

def setdir(new_path):
    # Change the current working directory
    print("Changing Working Directory to: ", new_path)
    os.chdir(new_path)

def getdir():
    # Verify the change
    print("Current Working Directory: ", os.getcwd())

def read_tub(car_app_path, tub_path):
    """
    read contents of an unzipped tub directory.

    Args:
    - car_app_path (str): Path to the car application directory.
    - tub_path (str): Path to the unzipped tub directory.
    - new_tub_path (str): Path to store the processed tub data.
    - return cfg & tub1
    """
    # Load the configuration
    cfg = load_config(os.path.join(car_app_path, 'config.py'))

    # Initialize the original and the new tub
    tub1 = Tub(tub_path)
    #tub2 = Tub(new_tub_path, inputs=['cam/image_array', 'user/angle', 'user/throttle', 'sensor'],
    #          types=['image_array', 'float', 'float', 'list'])

    return cfg, tub1

def process_tub(cfg, tub1):
    # Process each record in the original tub
    for record in tub1:
        t_record = TubRecord(config=cfg, base_path=tub1.base_path, underlying=record)
        img_arr = t_record.image(cached=False)
        # Add a random sensor reading
        record['sensor'] = list(np.random.uniform(size=2))
        record['cam/image_array'] = img_arr
        #tub2.write_record(record)

def list_object_data_attributes(obj):
    """
    Lists the data attribute keys of an object, excluding methods and built-in or special attributes.

    Parameters:
    - obj: The object to list data attribute keys for.

    Returns:
    - A list of strings representing the data attribute keys of the object.
    """
    keys = [key for key in dir(obj) if not key.startswith('__') and not key.endswith('__') and not callable(getattr(obj, key))]
    return keys


#######
import os

def setdir(new_path):
    os.chdir(new_path)

def getdir():
    return os.getcwd()
