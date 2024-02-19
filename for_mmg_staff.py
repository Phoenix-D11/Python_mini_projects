# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:33:01 2024

@author: DamilolaAyodele
"""

# Import Libraries
import pandas as pd
import re
from pathlib import Path

# Create the function to format the directory_path
def convert_to_cross_platform_path(path):
    """Convert Windows-style path to cross-platform path."""
    return str(Path(path).as_posix())

file_path = input("Input the file path here: ")
output_path = input("Enter where you want your file to be save here: ")

file_path = convert_to_cross_platform_path(file_path)

df_num = pd.read_excel(file_path)
print(df_num.shape)

# Functions for the process
def process_phone_numbers(df, column_name):
    # Step 1: Remove special characters from the specified column
    df[column_name] = df[column_name].apply(lambda x: re.sub(r'\W+', '', str(x)))
    
    # Step 2: Select viable phone numbers based on length criteria
    df['len_phone'] = df[column_name].apply(lambda x: len(str(x)))
    df = df[df['len_phone'].isin([10, 12, 13, 11])]
    df = df.drop('len_phone', axis=1)
    
    # Step 3: Select phone numbers with specific starting digits
    def check_starting_numbers(phone_number):
        if len(str(process_phone_numbers)) == 10 and str(phone_number)[:2] in ["91", "70", "80", "81", "90"] or str(phone_number)[:3] in ["810"]:
            return "234" + str(process_phone_numbers)
        else:
            return str(process_phone_numbers)
        
    # Apply the process_phone_numbers function to the 'Phone Numbers' column
    df['New_Phone Number'] = df['Phone Number'].apply(check_starting_numbers)
    
    return df

df_num = process_phone_numbers(df_num, 'Phone Number')
df_test = df_num.copy()
print(df_test.shape)

df_test["len"] = df_test["Phone Number"].apply(lambda x: len(x))

# Function to make it into an excel format template
def add_data_to_dataframe(df_t):
    new_cols = ['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name',
           'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi',
           'Name Prefix', 'Name Suffix', 'Initials', 'Nickname', 'Short Name',
           'Maiden Name', 'Birthday', 'Gender', 'Location', 'Billing Information',
           'Directory Server', 'Mileage', 'Occupation', 'Hobby', 'Sensitivity',
           'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership',
           'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type',
           'Phone 2 - Value', 'Organization 1 - Type', 'Organization 1 - Name',
           'Organization 1 - Yomi Name', 'Organization 1 - Title',
           'Organization 1 - Department', 'Organization 1 - Symbol',
           'Organization 1 - Location', 'Organization 1 - Job Description',
           'Unnamed: 41', 'Unnamed: 42', 'E-mail 1 - Type', 'E-mail 1 - Value']

    df_temp = pd.DataFrame(columns = new_cols)    
    df_temp['Name'] = df_t['First Name']
    df_temp['Given Name'] = df_t['Name']
    df_temp['Phone 1 - Value'] = df_t['Phone Number']
    df_temp['E-mail 1 - Value'] = df_t['Email']
    df_temp['Family Name'] = df_t['Last Name']
    df_temp['Organization 1 - Yomi Name'] = df_t['Contact owner']
    
    return df_temp

status = input("Are you trying to create a google contact list template")

df_google = add_data_to_dataframe(df_test)

def group_and_save_to_csv(data, column_name):
    unique_values = data[column_name].unique()

    for value in unique_values:
        group_data = data[data[column_name] == value]
        file_name = f"{value}_Contacts.csv"
        print(f"{value} has been saved")
        group_data.to_csv(f'{output_path}/{file_name}', index=False)

# Example usage:
# Assuming 'data' is your DataFrame and 'column_name' is the column to group by
# Replace 'data' and 'column_name' with your actual DataFrame and column name
group_and_save_to_csv(df_google, 'Organization 1 - Yomi Name')