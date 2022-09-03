import sys
import socket
import time

# Open given file.
def open_file(input_file):
    filename = input_file

    # Open the file provided. Catch any exceptions.
    try:
        file = open(filename, 'r')
    except TypeError as tyerr:
        with open(filename, 'r') as already_open:
            file = already_open

    # Return the opened file.
    return file

# Close the file for cleanup.
def close_file(open_file):
    open_file.close()

# Function to convert decimals to ASCII using a given file.
def decimals_to_ASCII(input_file):
    file = input_file
    final_string = ''
    current_number = ''
    current_number_int = -999
    list_of_numbers = []
    list_of_chars = []

    # Read file and display contents.
    print('File contains following: ')
    for line in file:
        current_number = line
        current_number = current_number.strip()
        print(current_number)

        # Convert string to int before saving.
        current_number_int =  int(current_number)

        # Save to list of numbers.
        list_of_numbers.append(current_number_int)

    # Console output.
    print('Converting from Decimal to ASCII...')
    print('')

    # Run through the list of numbers and convert to ASCII.
    for number in list_of_numbers:
        ascii_char = chr(number)

        # Save to new list for output.
        list_of_chars.append(ascii_char)

    # Contactenate list to single string.
    for char in list_of_chars:
        final_string = final_string + char

    # Console output.
    print('Conversion complete.')
    print('')

    # Retun the output of the converted ASCII.
    return final_string

# Connect to a given server and read output from the server.
def netcat_connection(hostname, port):
    input_hostname = hostname
    input_port = port
    server_file = ''
    output_filename = 'server_response.txt'

    # Check to see if the porrt provided is usable.
    try:
        input_port = int(input_port)
    except ValueError as verr:
        print('Unable to match port number. Please try a different port.')
        return server_file
    except Exception as ex:
        print('Exception found while converting the port to type: int')
        return server_file

    # Create the connection to the server.
    print('Creating conneciton to server.')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((input_hostname, input_port))

    # While the server is returning a response, save it.
    res = ""
    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    # Print server response to screen.
    print('Server Response: ')
    print(res)

    # Write the response to a file to save for later.
    with open(output_filename, 'w') as server_file:
        server_file.write(res)

    # Clean up by closing connecitons and files.
    print('Closing connection to server.')
    sock.close()
    server_file.close()
    print('')

    # Return the filename.
    return output_filename

# Main function to run inital code.
def main():
    # Take in arguments from command line and set further variables.
    argument_list = sys.argv
    argument_length = len(sys.argv)
    arg_file = ''
    output_string = ''
    output_file = ''
    output_filename = ''
    hostname = ''
    host_port = ''

    # Console output.
    print('############################### Converter Run ##########################')
    print('')

    # Check the arguments brought in and determine what to run. If less than 2 args, print usage message.
    if len(sys.argv) < 2:
        print(('Usage: {0} [option] [argument]'.format(sys.argv[0])))
        print("Use option '-h' for help information.")

    # If the correct amount passed in, check what has been given.
    else:

        # Provide help text for -h.
        if argument_list[1] == '-h':
            print(('Usage: {0} [option] [argument]'.format(sys.argv[0])))
            print('')
            print("Options: ")
            print('-h   = Provides this help.')
            print('-f   = Provide a file to read Decimal numbers from.')
            print('-s   = Connect to server and save output to file.')

        # Read in the file if provided with -f.
        elif argument_list[1] == '-f':
            if argument_length < 3:
                print(('Usage: {0} [option] [argument]'.format(sys.argv[0])))
                print('Please identify the full file path required to convert using: -f [filepath/filename]')

            # If filename has been provided, open and run converter.
            elif argument_length >= 3:
                arg_file = argument_list[2]
                opened_file = open_file(arg_file)
                print('File opened sucessfully.')
                output_string = decimals_to_ASCII(opened_file)
                print('Resulting conversion to: ')
                print(output_string)
                close_file(opened_file)

        # Check if the server argument has been passed in, check a port has been provided.
        elif argument_list[1] == '-s':
            if argument_length < 3:
                print(('Usage: {0} [option] [argument]'.format(sys.argv[0])))
                print('Please identify the server connetion with: -s [hostname/IP] [Port]')

            # If server is provided but not port, display correct input.
            elif argument_length == 3:
                print(argument_list)
                print(('Usage: {0} [option] [argument]'.format(sys.argv[0])))
                print('Please identify the server connetion with both hostname and port: -s [hostname/IP] [Port]')

            # If server is provided, read from server and save to file then convert.
            elif argument_length >= 4:

                # Make the connection to the server.
                output_filename = netcat_connection(argument_list[2], argument_list[3])

                # Open the saved file to convert.
                opened_file = open_file(output_filename)
                print('File opened sucessfully.')

                # Convert provided decimal input to ASCII.
                output_string = decimals_to_ASCII(opened_file)

                # Print the result to screen. 
                print('Resulting conversion to: ')
                print(output_string)
                close_file(opened_file)

    # Console output.
    print('')
    print('############################### End of Run #############################')

# Main function to run from.
if __name__ == '__main__':

    # Run the main function.
    main()
