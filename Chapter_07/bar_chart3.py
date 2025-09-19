import matplotlib.pyplot as plt


def main():
    # Use x as bar centers
    centers = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    bar_width = 10

    # Build the bar chart with colors
    plt.bar(centers, heights, bar_width, color=('r', 'g', 'b', 'y', 'k'))

    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Center the year labels under each bar
    plt.xticks(centers, ['2016', '2017', '2018', '2019', '2020'])

    plt.yticks([0, 100, 200, 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    plt.show()


if __name__ == '__main__':
    main()
