# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
    # Initialize an accumulator.
    total = 0.0

    try:
        # Open the sales_data.txt file.
        with open('sales_data.txt', 'r') as infile:
            # Read the values from the file and accumulate them.
            for line in infile:
                amount = float(line)
                total += amount

        # Print the total.
        print(f'{total:,.2f}')

    except FileNotFoundError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')


# Call the main function.
if __name__ == '__main__':
    main()
