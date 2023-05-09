import argparse
import logging
from my_package import my_module

def main():
    parser = argparse.ArgumentParser(description='My program')
    parser.add_argument('input_file', help='Input file')
    parser.add_argument('output_file', help='Output file')
    args = parser.parse_args()
    print(f'Input file: {args.input_file}')
    print(f'Output file: {args.output_file}')

if __name__ == '__main__':
    main()

def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    logging.info('Starting program')
    my_module.my_function() 
    
    logging.info('Program complete')
    
if __name__ == '__main__':
    main()