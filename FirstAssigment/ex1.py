# =============================================================================
#
#    Program: Basic Sql 
#    Author: Yaniv Gabay
#    Date Created: 2024-04-04
#
#
#    Description:
#      Answer to the 31 questions given at [Assigment 1](https://mowgli.hac.ac.il/pluginfile.php/1622023/mod_resource/content/2/SQL_targil_1.pdf)         
#      Each question is a query
#    Requirments:
#      pip install sqlalchemy pandas
#      World.db3 local db file
# =============================================================================

from sqlalchemy import create_engine,exc,text
import pandas as pd
import os
import sqlite3

class DatabaseHandler:
    def __init__(self,db_url):
       
         # Check if the database file exists
        db_file_path = db_url.split('///')[-1] 

        # Check if the database file exists in the current directory
        if not os.path.isfile(db_file_path):
            raise FileNotFoundError(f"Database file not found at '{db_file_path}'. Please check the path and try again.")
        
        self.engine = create_engine(db_url)

    def execute_query(self,query):
       try:
            with self.engine.connect() as connection:
                df = pd.read_sql_query(query, con=connection)
            return df
       except exc.SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of an error
    def list_tables(self):
        with self.engine.connect() as connection:
            # Use the text() construct for raw SQL query strings
            result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
            tables = [row[0] for row in result]
        return tables


def execute_and_print_query(query,query_num,db):
    try:
        df = db.execute_query(query)
        
        print("=" * 55)
        print(f"Question: {query_num}")
        print("The query is:")
        print(query)
        print(f"Total Rows: {len(df)}")
        print("First 5 rows:")
        print(df.head())

        if len(df) > 5:
            print("Last 5 rows:")
            print(df.tail())
        
    except Exception as e:
        print(f"An error occurred while executing or printing the query: {e}")

db_handler = DatabaseHandler('sqlite:///World.db3')

print(db_handler.list_tables())

queries = [
    """
    SELECT name
    FROM City
    """,
    
    """
    SELECT name
    FROM Country
    """,
    
    """
    SELECT name
    FROM City
    WHERE CountryCode = 'NLD' 
    """,
    """
    SELECT name
    FROM Country
    WHERE code IN ('LBR','IOT','TKL')
    """,
    """
    SELECT name
    FROM City
    WHERE population > 4000000
    """,
    """
    SELECT name
    FROM city
    WHERE (population > 3000000 AND countrycode = 'BRA')
    """,
    """
    SELECT name
    from city
    WHERE population BETWEEN 150000 AND 170000
    """,
    """
    SELECT name
    from country
    WHERE indepyear IN (1970,1980,1990)
    """,
    """
    SELECT name
    from country
    WHERE indepyear = (1980 AND 1990) 
    """,
    """
    SELECT name
    from country
    WHERE indepyear BETWEEN 1980 AND 1990
    """,
    """
    SELECT name
    from country
    WHERE ((indepyear IS 1980) AND (continent = 'Africa'))
    """,
    """
    SELECT name
    from country
    WHERE ((indepyear IS 1980) OR (continent = 'Africa'))
    """,
]


# Execute and display results for each query with automatic numbering
for query_number, query in enumerate(queries, start=1):
    execute_and_print_query(query, query_number, db_handler)

