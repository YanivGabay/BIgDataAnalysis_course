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

def replace_na(df):
    return df.fillna('Unknown')

def print_result(query,query_num,df,output_file=None):
    output = f"{'=' * 55}\n"
    output += f"Question: {query_num}\n"
    output += "The query is:\n"
    output += f"{query}\n"
    output += f"Total Rows: {len(df)}\n"
    output += "First 5 rows:\n"
    output += f"{df.head()}\n\n"

    if len(df) > 5:
        output += "Last 5 rows:\n"
        output += f"{df.tail()}\n"

    # Print to console
    print(output)

    # Write to file if specified
    if output_file:
        output_file.write(output)

def execute_and_print_query(query,query_num,db,output_file=None):
    try:
        df = db.execute_query(query)
       # Replace NaN values with 'Unknown' for better readability
       # Doesnt mess with the original data
        df = replace_na(df)
        
        print_result(query,query_num,df,output_file)
      
        
    except Exception as e:
        print(f"An error occurred while executing or printing the query: {e}")
def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("Yaniv Gabay 205745615\n")
            file.write("---SQL Queries and Results----\n")
        return file
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
        return None
def main():

    db_handler = DatabaseHandler('sqlite:///World.db3')
    #just to check the tables
    print(db_handler.list_tables())

    queries = [
        ###1-10###
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
        FROM city
        WHERE population BETWEEN 150000 AND 170000
        """,
        """
        SELECT name
        FROM country
        WHERE indepyear IN (1970,1980,1990)
        """,
        """
        SELECT name
        FROM country
        WHERE indepyear = (1980 AND 1990) 
        """,
        """
        SELECT name
        FROM country
        WHERE indepyear BETWEEN 1980 AND 1990
        """,

        ###11-20###

        """
        SELECT name
        FROM country
        WHERE ((indepyear IS 1980) AND (continent = 'Africa'))
        """,
        """
        SELECT name
        FROM country
        WHERE ((indepyear IS 1980) OR (continent = 'Africa'))
        """,
        """
        SELECT name
        FROM country
        WHERE continent IS 'Asia'
        """,
        """
        SELECT name
        FROM country
        WHERE continent IS NOT 'Asia'
        """,
        """
        SELECT name
        FROM country
        WHERE continent NOT IN ('Asia','Europe')
        """,
        """
        SELECT name
        FROM city
        WHERE name LIKE 'H%'
        """,
        """
        SELECT name
        FROM city
        WHERE name NOT LIKE '%e%'
        """,
        """
        SELECT DISTINCT language
        FROM countrylanguage
        ORDER BY language
        """,
        """
        SELECT name,indepyear
        FROM country
        ORDER BY
        indepyear ASC,
        name ASC
        """,
        """
        SELECT name,lifeexpectancy
        FROM country
        ORDER BY
            lifeexpectancy DESC,
            name ASC
        """,

        ###21-30###

        """
        SELECT name,GNP
        FROM country
        ORDER BY
            GNP DESC,
            name ASC
        LIMIT 10
        """,
        """
        SELECT name,GNP
        FROM country
        ORDER BY
            GNP DESC,
            name ASC
        LIMIT 10 OFFSET 10
        """,
        """
        SELECT name,GNP
        FROM country
        ORDER BY
            GNP ASC,
            name ASC
        LIMIT 10 
        """,
        ##didnt understand this question, what does "יבשת והאזור בסוגריים" means?
        """
        SELECT name country_name,
            continent || '-' || region AS 'continent-region'
        FROM country
        ORDER BY
            country_name ASC
        """,
        """
        SELECT name,
        round(population/1000000,2) as 'population in millions'
        FROM country
        WHERE name LIKE 'Z%'
        
        """,
        """
        SELECT name,GNP,GNPOLD
        FROM country
        WHERE GNP > (GNPOLD*2)
        """,
        """
        SELECT name,population/surfacearea as 'population_density',population,surfacearea
        FROM country
        ORDER BY
            population_density DESC,
            name ASC
        """,
        """
        SELECT name,
            population/surfacearea as 'population_density',
            population,surfacearea,
            code
        FROM country
        WHERE population_density > 2000
        ORDER BY
            code ASC
        """,
        """
        SELECT name,continent,surfacearea
        FROM country
        ORDER BY continent ASC,surfacearea DESC
        """,

        ###30-31###

        """
        SELECT name
        FROM country
        WHERE LENGTH(name) < 10 
        AND name NOT LIKE 'N%'
        """,
        """
        SELECT name,indepyear
        FROM country
        WHERE indepyear IS NULL
        """
    

        

    ]
    
    to_create_file = True
    if to_create_file:
        file_name = create_file("output.txt")
        if file_name:
            print(f"Results will be written to '{file_name}'\n")
      
    # Execute and display results for each query with automatic numbering
    for query_number, query in enumerate(queries, start=1):
        execute_and_print_query(query, query_number, db_handler,file_name)



if __name__ == '__main__':
    main()