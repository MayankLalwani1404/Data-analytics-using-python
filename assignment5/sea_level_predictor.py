from code import interact
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import linregress
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Observed Data")



    # Create first line of best fit
    slope, intercept, _, _, _ = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(df["Year"].min(), 2051))
    sea_level_pred = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_pred, 'r', label="Best Fit (1880-2050)")
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = stats.linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

    # Create second line of best fit
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent_pred = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_level_recent_pred, 'g', label="Best Fit (2000-2050)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()