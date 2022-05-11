"""
Write chess game data to PostgreSQL
"""
import sys
import psycopg2


DATABASE_URL="localhost"
DATABASE_PORT=5432
DATABASE_USER="admin"
DATABASE_PASSWORD="JZNjCXF#s6SEUf"
DATABASE_DB="analytics"


SQL_SCRIPTS = [
    "sql/create_chess_games_table.sql"
]

def main():
    """ Main function """

    # open sql scripts
    sql_queries = []
    for sql_script in SQL_SCRIPTS:
        with open(sql_script, "r") as fp:
            query = fp.read()
            sql_queries.append(query)

    # connect to the db
    database_url = f"postgresql://{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_DB}"
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    # execute sql
    for sql_query in sql_queries:
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
