# Flask-Healthcare-Application

# Income & Expense Survey Web Application

A full-stack data collection and analysis pipeline built with **Flask**, **MongoDB**, **Jupyter Notebook** and deployed on **AWS**. This project allows users to submit personal income and expense data via a web form, securely store it in a database, and analyze the data through powerful Python-based visualizations.

---

##  Project Overview

This project enables efficient collection and analysis of user financial data:

-  Built with **Flask** for the web interface and backend logic.
-  Data stored securely in **MongoDB**.
-  User data modeled with a custom Python `User` class.
-  Data exported to CSV for analysis.
-  Analytical visualizations generated using **pandas**, **matplotlib**, and **seaborn** in **Jupyter Notebooks**.
-  Deployed on AWS - 

---

## Project Structure




## Technologies Used

- Flask: Web framework for UI and backend
- MongoDB: NoSQL database to store form submissions
- Python: Data processing and backend logic
- Pandas, Matplotlib, Seaborn: Data analysis and visualization
- HTML/CSS: Frontend layout and styling
- AWS: Host Flask Application

---

## User Flow

1. User fills out form at `/` (index.html).
2. Data is saved to MongoDB (`income_survey.responses` collection).
3. Developer runs `UserData.csv.ipynb`:
   - Connects to MongoDB
   - Converts documents into `User` objects
   - Exports data to `users.csv`
4. Developer runs `Analysis.ipynb`:
   - Loads CSV file
   - Generates visualizations and insights

---

## Data Model

Each user submission contains:

- `age`: int
- `gender`: str
- `total_income`: float
- `expenses`: dict with keys:
  - `utilities`
  - `entertainment`
  - `school_fees`
  - `shopping`
  - `healthcare`

---

## Form Inputs

- Age (number input)
- Gender (dropdown)
- Total Income (number input)
- Expenses (checkboxes + amount inputs for selected categories)

Form validates all required inputs before submission. Expense amounts are only submitted if their category is checked.

---

## Jupyter Notebooks

### 1. `UserData.csv.ipynb`
- Defines `User` class
- Reads data from MongoDB
- Exports data to `users.csv`

### 2. `Analysis.ipynb`
- Loads CSV with pandas
- Cleans and processes data
- Generates plots:
  - Income distribution by age
  - Gender-based spending across categories

---

## Sample CSV Output

| Age | Gender | Income | Utilities | Entertainment | School Fees | Shopping | Healthcare |
|-----|--------|--------|-----------|---------------|-------------|----------|------------|
| 25  | Female | 50000  | 2000      | 1500          | 3000        | 1000     | 500        |

---

##  Completed Features

- Flask app with user-friendly form
-  MongoDB for secure data storage
-  Custom Python `User` class for processing
-  CSV export functionality
-  Exploratory data analysis and visualizations
-  Charts and plots saved for reporting
-  AWS to host Flask Application
---

##  Notes

- After every new form submission, re-run `UserData.csv.ipynb` to update the CSV.
- Ensure consistent column casing for smooth analysis (`Gender` vs `gender`).

---
