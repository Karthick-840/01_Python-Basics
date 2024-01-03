# Basic Functions
import pandas as pd
import numpy as np

import random
import string
#Create a random dataset
import argparse

parser = argparse.ArgumentParser(description='Creating a big dataframe')
parser.add_argument('n', type=int, help='Number of rows in the dataframe')
parser.add_argument('file_name', type=str, help='name of the csv file')

args = parser.parse_args()

n= int(args.n)
file_name = args.file_name

if n is None:
    n = 100000000
    
if file_name is None:
    file_name = 'test1.csv'



# Function to generate a random name and position
def generate_name_and_position():
    first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    # .001% chance of being a C-suite or board member
    if random.random() < 0.0001:
        positions = ["CEO", "CTO", "CFO", "CMO", "COO", "Chairman", "Board Member"]
        position = random.choice(positions)
    else:
        positions = ["Data Scientist", "Machine Learning Engineer", "Data Engineer", "Data Analyst", "AI Researcher",
                     "Intern", "HR", "Manager", "Product Owner", "Developer"]
        position = random.choice(positions)

    return f"{random.choice(first_names)} {random.choice(last_names)}", position

# Function to generate a random company name
def generate_company_name():
    company_suffixes = ["Technologies", "Solutions", "Innovations", "Labs", "Systems", "Analytics"]
    company_prefixes = ['Alpha', 'Beta', 'Gamma', 'Delta','Meta']
    company_name = f"{random.choice(company_prefixes)} {random.choice(company_suffixes)}"
    
    return company_name


# Function to generate random years of experience, age, and salary with some null values
def generate_experience_age_salary():
    experience = random.randint(0, 10)
    age = random.randint(18, 65)
    salary = random.randint(8000, 120000)

    return experience, age, salary
def generate_csv(n,file_name):

    # Generate random data for 10000 rows
    data = [(*generate_name_and_position(), *generate_experience_age_salary(),generate_company_name()) for _ in range(n)]

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Position', 'Experience', 'Age', 'Salary','Company'])

    # Randomly remove values within each column
    for col in df.columns:
        # 10% chance of setting a value to NaN in each column
        df.loc[df.sample(frac=0.1).index, col] = np.nan

    # Write data to CSV file
    csv_file_path = file_name
    df.to_csv(csv_file_path, index=False)

    print(f"CSV file '{csv_file_path}' created successfully.")

    
generate_csv(n,file_name)