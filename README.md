# Bike Share Data Analysis

## Project Overview
This project uses Python to explore data related to bike share systems
for three major US cities: Chicago, New York City, and Washington D.C.

## Software Requirements
- Python 3.6 or higher
- pandas library

Install dependencies with:
    pip install pandas

## Files Included
| File              | Description                                     |
|-------------------|-------------------------------------------------|
| bikeshare.py      | Main Python script — runs the analysis          |
| new_york_city.csv | Bike share data for New York City (excluded)    |
| .gitignore        | Prevents CSV files from being tracked by Git    |
| README.md         | Project documentation (this file)               |

## How to Run
1. Place the CSV data files in the same folder as bikeshare.py
2. Run the script:
    python bikeshare.py
3. Follow the interactive prompts:
   - Choose a city: Chicago, New York City, or Washington
   - Choose a filter: month, day, both, or none
   - Choose a month (January-June) and/or day if applicable

## Statistics Computed
- Most common month, day of week, and start hour
- Most common start station, end station, and trip combination
- Total and average trip duration
- User type counts, gender counts, and birth year stats