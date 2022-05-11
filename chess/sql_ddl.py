"""
Write chess game data to PostgreSQL
"""
import sys
import psycopg2

from dotenv import dotenv_values

CONFIG = dotenv_values(".env")

DATABASE_URL = CONFIG["DATABASE_URL"]
DATABASE_PORT = CONFIG["DATABASE_PORT"]
DATABASE_USER = CONFIG["DATABASE_USER"]
DATABASE_PASSWORD = CONFIG["DATABASE_PASSWORD"]
DATABASE_DB = CONFIG["DATABASE_NAME"]


SQL_SCRIPTS_DDL = [
    "sql/create_chess_schema.sql",
    "sql/create_chess_games_table.sql",
    "sql/create_chess_games_moves_table.sql"
]

def main():
    """ Main function """

    # open ddl sql scripts
    sql_queries_ddl = []
    for sql_script in SQL_SCRIPTS_DDL:
        with open(sql_script, "r") as fp:
            query = fp.read()
            sql_queries_ddl.append(query)

    # connect to the db
    database_url = f"postgresql://{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_DB}"
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    # execute sql
    for sql_query in sql_queries_ddl:
        print(f"Executing SQL:\n{sql_query}")
        cur_response = cur.execute(sql_query)
        conn.commit()
        if cur_response:
            results = cur.fetchall()
            for result in results:
                print(result)

    # close the db connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    sys.exit(main())
