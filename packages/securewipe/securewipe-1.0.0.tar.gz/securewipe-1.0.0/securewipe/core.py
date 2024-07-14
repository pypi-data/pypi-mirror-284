import os
import sys
import glob
import shutil
import time

def replace_random(file_path=None):
    if file_path is None:
        file_path = os.path.realpath(__file__)
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'wb') as file:
            random_bytes = os.urandom(file_size)
            file.write(random_bytes)
    except Exception as e:
        raise RuntimeError(f"Error while replacing random data: {e}")

def delete_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            raise FileNotFoundError(f"{file_path} does not exist or is not a valid file or directory.")
    except Exception as e:
        raise RuntimeError(f"Error while deleting {file_path}: {e}")

def self_destruct(target_path=None):
    try:
        if target_path is None:
            script_path = os.path.realpath(__file__)
            replace_random(script_path)
        elif os.path.isfile(target_path):
            replace_random(target_path)
        elif os.path.isdir(target_path):
            for file_path in glob.glob(os.path.join(target_path, '*')):
                if os.path.isfile(file_path):
                    replace_random(file_path)
        else:
            raise FileNotFoundError(f"{target_path} does not exist or is not a valid file or directory.")
        
        time.sleep(2)  
    except Exception as e:
        raise RuntimeError(f"Error during self-destruct: {e}")
            
