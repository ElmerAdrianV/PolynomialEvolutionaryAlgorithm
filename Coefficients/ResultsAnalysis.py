import pandas as pd
import matplotlib.pyplot as plt

def generate_histogram_coef(csv_file, range_start, range_end, interval, coef_degree,poly_degree = 4):
    # Read the CSV file into a Pandas DataFrame with a default column name
    df = pd.read_csv(csv_file, header=None, names=['Value'])

    # Extract the single column
    data = df['Value']
    
    # Print the minimum and maximum values
    min_value = data.min()
    max_value = data.max()
    print(f"Minimum Value: {min_value}")
    print(f"Maximum Value: {max_value}")

    # Create a histogram
    plt.hist(data, bins=range(range_start, range_end + interval, interval), color='black', edgecolor='black')
    
    # Customize the plot
    plt.title(f'Histogram of coefficients with degree {coef_degree}')
    plt.xlabel('coefficients')
    plt.ylabel('Frequency')

    # Show the plot
    plt.show()

# Example usage:
ranges = [[-30,30],[-100,300],[-1000,1000]]
for i in range(0,3):
    csv_file_path = f'coef_{i+1}.csv'  # Replace with the path to your CSV file
    range_start = ranges[i][0]
    range_end = ranges[i][1]
    interval = 1
    generate_histogram_coef(csv_file_path, range_start, range_end, interval,i+1,4)
