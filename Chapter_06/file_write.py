# This program writes three lines of data
# to a file.

"""
File modes
Python File Open Modes (open(filename, mode))
r → Read only. File must exist. Pointer at start. Error if file missing.
w → Write only. Creates new file or truncates existing. Pointer at start.
a → Append only. Creates new file if missing. Pointer at end.
r+ → Read & write. File must exist. Pointer at start. Can overwrite but not truncate.
w+ → Read & write. Creates new file or truncates existing. Pointer at start.
a+ → Read & write. Creates new file if missing. Pointer at end, but can still read.
x → Exclusive write. Creates new file. Error if file already exists.
"""


def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()


# Call the main function.
if __name__ == '__main__':
    main()
