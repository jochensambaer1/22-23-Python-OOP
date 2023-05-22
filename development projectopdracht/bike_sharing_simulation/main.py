import argparse # Import the argparse module
import logging # Import the logging module
import my_module # Import the module we just created

def main(): # Define the main function
    parser = argparse.ArgumentParser(description='My program') # Create a new ArgumentParser object
    parser.add_argument('input_file', help='Input file') # Add an argument to the parser
    parser.add_argument('output_file', help='Output file') # Add another argument to the parser
    args = parser.parse_args() # Parse the arguments and store the results in a variable
    
    print(f'Input file: {args.input_file}') # Print the value of the input_file argument
    print(f'Output file: {args.output_file}') # Print the value of the output_file argument

if __name__ == '__main__': # Only run the program if it is the main program
    main() # Call the main function

def main(): # Define the main function
    logging.basicConfig(level=logging.DEBUG, # Configure logging to log all messages
                        format='%(asctime)s %(levelname)s %(message)s')
    logging.info('Starting program') # Log a message to indicate the program is starting
    
    my_module.my_function() # Call the function from our module
    
    logging.info('Program complete') # Log a message to indicate the program is complete
    
if __name__ == '__main__': # Only run the program if it is the main program
    main() # Call the main function