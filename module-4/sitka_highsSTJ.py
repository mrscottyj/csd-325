"""
Weather Data Visualization Program
Modified to include menu system for viewing high or low temperatures
Author: Scott Johnson
Date: January 15th, 2025
CSD-325
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Display instructions when program starts
print("\nWELCOME TO SITKA WEATHER VIEWER")
print("This program displays high or low temperatures for 2018.")
print("-" * 50)

# Main program loop
while True:
    # Display menu
    print("\nMenu Options:")
    print("  1. Highs")
    print("  2. Lows")
    print("  3. Exit")
    
    # Get user choice
    choice = input("\nEnter your choice (1-3): ")
    
    # Exit option
    if choice == '3':
        print("\nThank you for using the weather viewer. Goodbye!\n")
        sys.exit()
    
    # Check for valid choice
    if choice not in ['1', '2']:
        print("Invalid choice. Please try again.")
        continue
    
    # Read the CSV file
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Get dates and temperatures from file
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])  # Added: read low temperatures
            lows.append(low)
    
    # Plot based on user choice
    fig, ax = plt.subplots()
    
    if choice == '1':
        # Plot high temperatures in red
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
    else:
        # Plot low temperatures in blue
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
    
    # Format plot
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()