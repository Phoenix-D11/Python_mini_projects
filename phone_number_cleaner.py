# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:52:32 2024

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
file_name = input("Eneter file name: ")
    
df_test.to_csv(f'{output_path}/{file_name}', index=False)
