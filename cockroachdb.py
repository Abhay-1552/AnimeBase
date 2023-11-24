import psycopg2
from psycopg2 import sql
from urllib.parse import urlparse
from psycopg2 import extensions


class AnimeDB:
    def __init__(self, db_url):
        self.url = urlparse(db_url)

        # Connect to the CockroachDB database using the URL
        self.conn = psycopg2.connect(
            database=self.url.path[1:],
            user=self.url.username,
            password=self.url.password,
            host=self.url.hostname,
            port=self.url.port
        )

        try:
            if self.conn.status == extensions.STATUS_READY:
                print("Connection Successful!")

        except Exception as e:
            print("Connection Failed:", e)

    def close_connection(self):
        if hasattr(self, 'conn') and self.conn is not None:
            self.conn.close()
            print("Connection Closed")


class Anime:
    def __init__(self, conn):
        # Create a cursor object to execute SQL queries
        self.cur = conn.cursor()

        try:
            create_table_query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS Anime (
                    id SERIAL PRIMARY KEY,
                    AnimeName VARCHAR(300) NOT NULL,
                    Episodes INT NOT NULL,
                    Type VARCHAR(10) NOT NULL
                )
            """)

            self.cur.execute(create_table_query)
            conn.commit()

        except Exception as e:
            print("Error:", e)

    def insert_data(self, conn, anime_name, episodes, anime_type):
        # Insert data into the table
        try:
            insert_data_query = """
                INSERT INTO Anime (AnimeName, Episodes, Type) VALUES (%s, %s, %s);
            """

            self.cur.execute(insert_data_query, (anime_name, episodes, anime_type))
            conn.commit()

        except Exception as e:
            print("Error:", e)

    def retrieve_data(self, conn):
        try:
            select_data_query = """
                SELECT AnimeName, Episodes, Type FROM Anime;
            """

            self.cur.execute(select_data_query)

            # Fetch all rows
            rows = self.cur.fetchall()

            for row in rows:
                print(row)

        except Exception as e:
            print("Error:", e)

    def close_cursor(self):
        if hasattr(self, 'cur') and self.cur is not None:
            self.cur.close()


if __name__ == '__main__':
    # Replace this value with your CockroachDB connection URL
    db_url = "postgresql://Abhay:Lo4jQy5LkBDj33DUzqf2tQ@cloudy-tang-7295.8nk.cockroachlabs.cloud:26257/AnimeBase?sslmode=verify-full"

    anime_db = AnimeDB(db_url)

    anime = Anime(anime_db.conn)

    # Example: Insert data
    # anime.insert_data(anime_db.conn, "Naruto", 220, "Shounen")

    # Example: Retrieve and print data
    anime.retrieve_data(anime_db.conn)

    # Close cursor and connection
    anime.close_cursor()
    anime_db.close_connection()
