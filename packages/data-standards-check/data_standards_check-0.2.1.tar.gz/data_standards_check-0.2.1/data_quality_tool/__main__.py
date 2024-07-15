import os
import argparse
import sys
from data_quality_tool.scripts import check_and_export, generate_standard_file, get_current_date_indicator

def main():
    parser = argparse.ArgumentParser(description='Data Quality Tool')
    subparsers = parser.add_subparsers(dest='command')

    # Sub-parser for the check command
    check_parser = subparsers.add_parser('check', help='Check data quality and export log')
    check_parser.add_argument('data_folder', type=str, help='Path to the folder containing data files and standard file')

    # Sub-parser for the generate command
    generate_parser = subparsers.add_parser('generate', help='Generate data value standard file')
    generate_parser.add_argument('data_folder', type=str, help='Path to the folder to save the standard file')
    generate_parser.add_argument('--input_file', type=str, help='Path to the input CSV data file (optional)', default=None)

    args = parser.parse_args()

    if args.command == 'check':
        date_indicator = get_current_date_indicator()
        log_file_path = os.path.join(args.data_folder, f'check_log_{date_indicator}.csv')
        check_and_export(args.data_folder, log_file_path)
    elif args.command == 'generate':
        generate_standard_file(args.data_folder, args.input_file)
    else:
        print("Usage: data_check <command> [options]")
        print("Commands:")
        print("  check <data_folder>  Check data quality and export log")
        print("  generate <data_folder> [--input_file <input_file>]    Generate data value standard file")
        sys.exit(1)

if __name__ == '__main__':
    main()
