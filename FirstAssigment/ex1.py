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
        file = open(file_name, 'w') 
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
        SELECT Name
        FROM City
        """,
        
        """
        SELECT Name
        FROM Country
        """,
        
        """
        SELECT Name
        FROM City
        WHERE Countrycode = 'NLD' 
        """,
        """
        SELECT Name
        FROM Country
        WHERE code IN ('LBR','IOT','TKL')
        """,
        """
        SELECT Name
        FROM City
        WHERE Population > 4000000
        """,
        """
        SELECT Name
        FROM City
        WHERE (Population > 3000000 AND Countrycode = 'BRA')
        """,
        """
        SELECT Name
        FROM City
        WHERE Population BETWEEN 150000 AND 170000
        """,
        """
        SELECT Name
        FROM Country
        WHERE Indepyear IN (1970,1980,1990)
        """,
        """
        SELECT Name
        FROM Country
        WHERE Indepyear = (1980 AND 1990) 
        """,
        """
        SELECT Name
        FROM Country
        WHERE Indepyear BETWEEN 1980 AND 1990
        """,

        ###11-20###

        """
        SELECT Name
        FROM Country
        WHERE ((Indepyear IS 1980) AND (continent = 'Africa'))
        """,
        """
        SELECT Name
        FROM Country
        WHERE ((Indepyear IS 1980) OR (continent = 'Africa'))
        """,
        """
        SELECT Name
        FROM Country
        WHERE continent IS 'Asia'
        """,
        """
        SELECT Name
        FROM Country
        WHERE continent IS NOT 'Asia'
        """,
        """
        SELECT Name
        FROM Country
        WHERE continent NOT IN ('Asia','Europe')
        """,
        """
        SELECT Name
        FROM City
        WHERE Name LIKE 'H%'
        """,
        """
        SELECT Name
        FROM City
        WHERE Name NOT LIKE '%e%'
        """,
        """
        SELECT DISTINCT Language
        FROM Countrylanguage
        ORDER BY Language
        """,
        """
        SELECT Name,Indepyear
        FROM Country
        ORDER BY
        Indepyear ASC,
        Name ASC
        """,
        """
        SELECT Name,lifeexpectancy
        FROM Country
        ORDER BY
            lifeexpectancy DESC,
            Name ASC
        """,

        ###21-30###

        """
        SELECT Name,GNP
        FROM Country
        ORDER BY
            GNP DESC,
            Name ASC
        LIMIT 10
        """,
        """
        SELECT Name,GNP
        FROM Country
        ORDER BY
            GNP DESC,
            Name ASC
        LIMIT 10 OFFSET 10
        """,
        """
        SELECT Name,GNP
        FROM Country
        ORDER BY
            GNP ASC,
            Name ASC
        LIMIT 10 
        """,
        ##didnt understand this question, what does "יבשת והאזור בסוגריים" means?
        """
        SELECT Name Country_Name,
            Continent || '-' || Region AS 'continent-region'
        FROM Country
        ORDER BY
            Country_Name ASC
        """,
        """
        SELECT Name,
        round(Population/1000000,2) as 'Population in millions'
        FROM Country
        WHERE Name LIKE 'Z%'
        
        """,
        """
        SELECT Name,GNP,GNPOLD
        FROM Country
        WHERE GNP > (GNPOLD*2)
        """,
        """
        SELECT Name,Population/Surfacearea as 'Population_density',Population,Surfacearea
        FROM Country
        ORDER BY
            Population_density DESC,
            Name ASC
        """,
        """
        SELECT Name,
            Population/Surfacearea as 'Population_density',
            Population,Surfacearea,
            code
        FROM Country
        WHERE Population_density > 2000
        ORDER BY
            code ASC
        """,
        """
        SELECT Name,Continent,Surfacearea
        FROM Country
        ORDER BY Continent ASC,Surfacearea DESC
        """,

        ###30-31###

        """
        SELECT Name
        FROM Country
        WHERE LENGTH(Name) < 10 
        AND Name NOT LIKE 'N%'
        """,
        """
        SELECT Name,Indepyear
        FROM Country
        WHERE Indepyear IS NULL
        """
    

        

    ]
    
    to_create_file = False
    if to_create_file:#error handling inside the function
        file_name = create_file("output.txt")
        if file_name:
            print(f"Results will be written to '{file_name}'\n")
      
    # Execute and display results for each query with automatic numbering
    for query_number, query in enumerate(queries, start=1):
        execute_and_print_query(query, query_number, db_handler,file_name)



if __name__ == '__main__':
    main()