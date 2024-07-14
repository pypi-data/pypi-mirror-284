# Securewipe: Core functionality for securely overwriting files with random data.
# Author: Fidal
# Email: hellome@gmail.com
# Copyright: (c) 2024 Fidal

import os

def replace_random(file_path, passes=7):
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'wb') as file:
            for i in range(passes):
                file.write(b'\x00' * file_size)
                file.flush()
                os.fsync(file.fileno())

                file.write(b'\xFF' * file_size)
                file.flush()
                os.fsync(file.fileno())

                file.write(b'\xAA' * file_size)  
                file.flush()
                os.fsync(file.fileno())

                file.write(b'\x55' * file_size)  
                file.flush()
                os.fsync(file.fileno())

                random_bytes = os.urandom(file_size)
                file.write(random_bytes)
                file.flush()
                os.fsync(file.fileno())

                random_bytes = os.urandom(file_size)
                file.write(random_bytes)
                file.flush()
                os.fsync(file.fileno())

                random_bytes = os.urandom(file_size)
                file.write(random_bytes)
                file.flush()
                os.fsync(file.fileno())
    except Exception as e:
        raise e

def self_destruct(script_path):
    try:
        replace_random(script_path)
        os.remove(script_path)
    except Exception as e:
        raise e
