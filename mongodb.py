from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class AnimeDB:
    DATABASE_NAME = 'AnimeBase'
    COLLECTION_NAME = 'Anime'

    def __init__(self, connection_string):
        self.conn = MongoClient(connection_string, server_api=ServerApi('1'))
        self.database = self.conn.get_database(self.DATABASE_NAME)
        self.collection = self.database[self.COLLECTION_NAME]

        try:
            self.conn.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

        except Exception as e:
            print("Connection Failed due to:", e)

    def close_connection(self):
        if hasattr(self, 'conn') and self.conn is not None:
            self.conn.close()
            print("Connection Closed")


class Anime:
    def __init__(self, db):
        self.db = db

    def insert_anime_data(self):
        anime_name = input("Enter Anime Name:")
        episodes = int(input("Enter Number of Episodes:"))
        content_type = input("Season or Movie:")

        try:
            new_data = {
                "AnimeName": anime_name,
                "Episodes": episodes,
                "Type": content_type
            }

            self.db.collection.insert_one(new_data)
            print("Data inserted")

        except Exception as e:
            print(f"Error: {str(e)}")

    def get_anime_data(self):
        try:
            table_data = list(self.db.collection.find())
            return table_data

        except Exception as e:
            print("Error", e)
            return f"Error: {e}"


if __name__ == "__main__":
    connect = 'mongodb+srv://abhaypatel1552:abhaypatel1552@cluster0.gtolic6.mongodb.net/?retryWrites=true&w=majority'

    db = AnimeDB(connect)
    app = Anime(db)

    # app.insert_anime_data()
    print(app.get_anime_data())

    # Close the connection when done
    db.close_connection()
