import os
import argparse
from securewipe.core import replace_random

def main():
    parser = argparse.ArgumentParser(description='Securely overwrite files with random data.')
    parser.add_argument('--self-destruct', metavar='PATH', type=str, help='Path to the file or directory to overwrite with random data.')
    
    args = parser.parse_args()
    
    if args.self_destruct:
        path = args.self_destruct
        if os.path.isfile(path):
            replace_random(path)
            print(f"Successfully overwritten: {path}")
        elif os.path.isdir(path):
            for file_name in os.listdir(path):
                file_path = os.path.join(path, file_name)
                if os.path.isfile(file_path):
                    replace_random(file_path)
                    print(f"Successfully overwritten: {file_path}")
        else:
            print(f"The path {path} does not exist.")

if __name__ == "__main__":
    main()
