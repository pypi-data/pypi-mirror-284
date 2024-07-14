import argparse
from .core import delete_file, self_destruct, replace_random

def main():
    parser = argparse.ArgumentParser(description="Securely wipe files or folders by overwriting with random data or delete files/directories.")
    parser.add_argument('--self-destruct', action='store_true', help='Self-destruct the script after execution. If path is specified, overwrite that file or directory.')
    parser.add_argument('--delete', type=str, help='Delete the specified file or directory.')
    parser.add_argument('target_path', nargs='?', default=None, help='Optional path to file or directory to overwrite or delete.')

    args = parser.parse_args()

    try:
        if args.self_destruct:
            self_destruct(args.target_path)
            if args.target_path:
                print(f"Securely wiped: {args.target_path}")
            else:
                print("Self-destructed successfully.")
        elif args.delete:
            delete_file(args.delete)
            print(f"Successfully deleted: {args.delete}")
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
    
