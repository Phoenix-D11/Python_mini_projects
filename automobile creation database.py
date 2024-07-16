# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:28:22 2024

@author: Damilola Ayodele
"""

import sqlite3
import sqlalchemy
import pandas as pd



df = pd.read_csv("C:\Phoenix\Documents\Automobile.csv")


DATABASE_LOCATION = "sqlite:///C:/Users/Damilola Ayodele/automoble.sqlite"
# Connect to SQLite database (create if not exists)
conn = sqlite3.connect('automobile.db')
engine = sqlalchemy.create_engine(DATABASE_LOCATION)
# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define SQL query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS training (
    "id" INTEGER PRIMARY KEY,
"symboling" INTEGER,
"normalized_losses" INTEGER,
"make" TEXT,
"fuel_type" VARCHAR(255),
"aspiration" VARCHAR(255),
"number_of_doors" VARCHAR(255),
"body_style" VARCHAR(255),
"drive_wheels" VARCHAR(255),
"engine_location" VARCHAR(255),
"wheel_base" REAL,
"length" REAL,
"width" REAL,
"height" REAL,
"curb_weight" INTEGER,
"engine_type" VARCHAR(255),
"number_of_cylinders" VARCHAR(255),
"engine_size" INTEGER,
"fuel_system" VARCHAR(255),
"bore" REAL,
"stroke" REAL,
"compression_ratio" REAL,
"horsepower" INTEGER,
"peak_rpm" INTEGER,
"city_mpg" INTEGER,
"highway_mpg" INTEGER,
"price" INTEGER);
"""

# Execute the SQL query to create the table
cursor.execute(create_table_query)

try:
    df.to_sql("automobile", engine, index=False, if_exists='append')
except:
    print("Data already exists in the database")

conn.commit()
conn.close()
print("Close database successfully")
