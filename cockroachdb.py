import psycopg2
from urllib.parse import urlparse
from psycopg2 import extensions
from psycopg2 import sql
import os
from dotenv import load_dotenv


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
        self.conn = conn
        self.cur = conn.cursor()

        try:
            create_table_query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS mal_data (
                    mal_id INT8 NOT NULL,
                    english_title VARCHAR(300) NOT NULL,
                    japanese_title VARCHAR(300) NOT NULL,
                    episodes INT8 NOT NULL,
                    type VARCHAR(10) NOT NULL,
                    image_url VARCHAR(600) NOT NULL,
                    page_url VARCHAR(600) NOT NULL,
                    score FLOAT
                );
            """)

            self.cur.execute(create_table_query)
            conn.commit()

        except Exception as e:
            print("Error:", e)

    def insert_data(self, data):
        # Insert data into the table
        try:
            mal_data = data[0]

            flag = Anime.cross_check_values(self, mal_data["Anime_ID"])

            if flag == 0:
                insert_data_query = """INSERT INTO public.mal_data (mal_id, english_title, japanese_title, episodes, 
                type, image_url, page_url, score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

                self.cur.execute(insert_data_query, (mal_data["Anime_ID"], mal_data["English_Title"],
                                                     mal_data["Japanese_Title"], mal_data["Episodes"],
                                                     mal_data["Anime_Type"], mal_data["Anime_Image"],
                                                     mal_data["Anime_URL"], mal_data["Anime_Score"]))
                self.conn.commit()

        except Exception as e:
            return f"Error: {e}"

    def retrieve_data(self):
        try:
            select_data_query = """
                SELECT * FROM public.mal_data ORDER BY english_title ASC;
            """

            self.cur.execute(select_data_query)

            fetch_data = []

            # Fetch all rows
            rows = self.cur.fetchall()

            for row in rows:
                data = {
                    "English_Title": row[1],
                    "Japanese_Title": row[2],
                    "Anime_Type": row[4],
                    "Episodes": row[3],
                    "Anime_ID": row[0],
                    "Anime_URL": row[6],
                    "Anime_Image": row[5],
                    "Anime_Score": row[7]
                }
                fetch_data.append(data)

            return fetch_data

        except Exception as e:
            return f"Error: {e}"

    def cross_check_values(self, mal_id):
        try:
            select_data_query = f"""
                SELECT * FROM public.mal_data WHERE mal_id = {mal_id};
            """

            self.cur.execute(select_data_query)

            flag = 0
            if self.cur.fetchone():
                flag += 1

            return flag

        except Exception as e:
            return f"Error: {e}"

    def close_cursor(self):
        if hasattr(self, 'cur') and self.cur is not None:
            self.cur.close()
