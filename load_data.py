import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create the 'glasses' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS glasses (
        glass_type VARCHAR(50),
        stock INT,
        bar VARCHAR(50)
    )
''')

# Open the CSV file and load the data into the table
with open('your_csv_file.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip the header row

    for row in csv_data:
        cursor.execute('''
            INSERT INTO glasses (glass_type, stock, bar)
            VALUES (?, ?, ?)
        ''', row)

# Commit the changes and close the connection
conn.commit()
conn.close()


import requests

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process and work with the cocktail data as needed
else:
    print("Error occurred while fetching cocktail data.")

