# Expense Tracker

A Python-based expense tracking system that allows users to record expenses, analyze spending patterns, filter expenses by month, and visualize spending trends.

## Project Overview

This project is a command-line Expense Tracker developed using Python. It uses Pandas for data management and analysis and Matplotlib for visualizing expense patterns.

The application stores expense records in a CSV file and provides options to add expenses, view summaries, perform category-wise analysis, filter expenses by month, and display spending graphs.

## Key Features

- Add new expenses with date, category, and amount
- Store expense records in a CSV file
- View total and average expenses
- Perform category-wise expense analysis
- Identify highest and lowest spending categories
- View category frequency
- Filter expenses by month
- Identify daily spending patterns
- Display category-wise spending using bar charts
- Display daily spending trends using line charts
- Validate date and amount inputs

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV
- Visual Studio Code

## Project Files

```text
Expense-Tracker/
│
├── expenses.py
├── expenses.csv
└── README.md
```

## How to Run

1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open the project folder in Visual Studio Code.
4. Install the required libraries:

```bash
pip install pandas matplotlib
```

5. Make sure `expenses.csv` is present in the same folder as `expenses.py`.
6. Run the program:

```bash
python expenses.py
```

7. Use the menu displayed in the terminal to manage and analyze expenses.

## Project Workflow

```text
Expense Data
      ↓
CSV File
      ↓
Load Data using Pandas
      ↓
Add / Filter / Analyze Expenses
      ↓
Category & Daily Analysis
      ↓
Data Visualization using Matplotlib
```

## Future Scope

- Monthly and yearly spending reports
- Budget tracking and alerts
- Expense prediction
- Interactive dashboards
- Database integration
- User authentication
- Web or mobile application interface

## Author

**Man Mohini Sharma**
