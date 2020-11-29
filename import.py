import csv
from sys import argv
import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables
env_path = Path('./plastic_footprint/plastic_footprint/') / '.env'
load_dotenv(dotenv_path=env_path)

#Script to import csv to postgres database
def main():
    # Check if the number of arguments is 2
    if len(argv) != 2:
        print("Usage: python3 import.py <filename>.csv")
        exit(1)

    # Read environment variables
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    # Import database
    db = psycopg2.connect(dbname="plastic_tracker", user=user, password=password, host="127.0.0.1")

    cur = db.cursor()
    # Delete all the database entries
    cur.execute("DELETE FROM plastic_tracker_product")
    
    # Open imported csv
    with open(argv[1], 'r') as f:
      reader = csv.reader(f)
      next(reader) # Skip the header row.
      for row in reader:
        cur.execute("INSERT INTO plastic_tracker_product VALUES (%s, %s, %s)",row)
    db.commit()
 
    exit(0)

main()

