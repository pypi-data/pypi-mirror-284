# puddleext/cli.py
import argparse
from .convert import convert_file
from .view import view_file

def main():
    parser = argparse.ArgumentParser(description="Puddle CLI Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Subcommand for convert
    parser_convert = subparsers.add_parser('convert', help='Convert a file to a custom format')
    parser_convert.add_argument('input', type=str, help='Input file to convert')
    
    # Subcommand for view
    parser_view = subparsers.add_parser('view', help='View a file')
    parser_view.add_argument('input', type=str, help='Input file to view')

    args = parser.parse_args()

    if args.command == 'convert':
        convert_file(args.input)
    elif args.command == 'view':
        view_file(args.input)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
