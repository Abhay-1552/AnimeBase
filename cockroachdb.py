import psycopg2
from psycopg2 import sql
from urllib.parse import urlparse
from psycopg2 import extensions
from content_scraping import Info
from mal_api import MAL


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
                    Type VARCHAR(10) NOT NULL,
                    Image VARCHAR(600) NOT NULL,
                    Content VARCHAR(600) NOT NULL
                )
            """)

            self.cur.execute(create_table_query)
            conn.commit()

        except Exception as e:
            print("Error:", e)

    def insert_data(self, conn, anime_name, episodes, anime_type):
        # Insert data into the table
        try:
            url_name = str(anime_name).replace(' ', '_')
            app = Info(url_name)
            content_link, image_link = app.anime_info()

            insert_data_query = """
                INSERT INTO Anime (AnimeName, Episodes, Type, Image, Content) VALUES (%s, %s, %s, %s, %s);
            """

            self.cur.execute(insert_data_query, (anime_name, episodes, anime_type, image_link, content_link))
            conn.commit()

        except Exception as e:
            return f"Error: {e}"

    def retrieve_data(self):
        try:
            select_data_query = """
                SELECT AnimeName, Episodes, Type, Image, Content FROM Anime ORDER BY AnimeName ASC;
            """

            self.cur.execute(select_data_query)

            fetch_data = []

            # Fetch all rows
            rows = self.cur.fetchall()

            for row in rows:
                data = {
                    "AnimeName": row[0],
                    "Episodes": row[1],
                    "Type": row[2],
                    "Image": row[3],
                    "Content": row[4]
                }
                fetch_data.append(data)

            return fetch_data

        except Exception as e:
            return f"Error: {e}"

    def close_cursor(self):
        if hasattr(self, 'cur') and self.cur is not None:
            self.cur.close()
