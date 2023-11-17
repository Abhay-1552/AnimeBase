import mysql.connector


class Anime:
    def __init__(self):
        # Connection Establishment
        self.conn = mysql.connector.connect(host='localhost', user='root', password='Abh@y1552')
        self.cursor = self.conn.cursor()

        # Creating Database and Table
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS AnimeBase;")
            self.cursor.execute("USE AnimeBase;")
            self.cursor.execute("""
            
            CREATE TABLE IF NOT EXISTS Anime (
            IndexNo INT AUTO_INCREMENT PRIMARY KEY,
            AnimeName VARCHAR(300) NOT NULL,
            Episodes INT NOT NULL,
            Season BIT NOT NULL DEFAULT 0,
            Movie BIT NOT NULL DEFAULT 0);
            
            """)
            print("done")

        except Exception as e:
            print("Error:", e)

    def insert_anime_data(self):
        self.AnimeName = input("Enter Anime Name:")
        self.Episodes = int(input("Enter Number of Episodes:"))
        self.Season = int(input("Enter 1 if it is Season else 0:"))
        self.Movie = int(input("Enter 1 if it is Movie else 0:"))

        try:
            self.cursor.execute(f"""
            
            INSERT INTO anime (AnimeName, Episodes, Season, Movie) 
            VALUES ('{self.AnimeName}', {self.Episodes}, {self.Season}, {self.Movie});
            
            """)

            # Commit the transaction
            self.conn.commit()
            print("Data inserted")

        except Exception as e:
            print(f"Error: {str(e)}")

    def close_connection(self):
        self.conn.close()

    def show_table(self):
        self.cursor.execute("SELECT * FROM Anime;")

        for data in self.cursor:
            print(data)


if __name__ == "__main__":
    app = Anime()
    # app.insert_anime_data()
    # app.show_table()
