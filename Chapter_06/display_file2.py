# This program displays the contents
# of a file.

def main():
    # Get the name of a file.
    filename = input('Enter a filename: ')

    try:
        # Open the file.
        with open(filename, 'r') as infile:
            # Read the file's contents.
            contents = infile.read()

            # Display the file's contents.
            print(contents)
    except FileNotFoundError:
        print(f'The file {filename} does not exist.')


# Call the main function.
if __name__ == '__main__':
    main()
