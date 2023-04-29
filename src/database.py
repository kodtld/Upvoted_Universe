import sqlite3
import pickle

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS converted_videos 
            (id INTEGER PRIMARY KEY, post_id TEXT, title TEXT, author TEXT, comments BLOB, instagram BOOLEAN)''')

        self.conn.commit()

    def add_converted_post(self, post):
        serialized_comments = pickle.dumps(post['comments'])
        self.cursor.execute("INSERT INTO converted_videos (post_id, title, author, comments, instagram) VALUES (?, ?, ?, ?, ?)",
            (post['id'], post['title'], post['author'], serialized_comments, post['instagram']))
        self.conn.commit()

    def get_converted_posts(self):
        self.cursor.execute("SELECT * FROM converted_videos")
        rows = self.cursor.fetchall()
        converted_posts = []
        for row in rows:
            post = {
                'id': row[1],
                'title': row[2],
                'author': row[3],
                'comments': pickle.loads(row[4]),
                'instagram': row[5]
            }
            converted_posts.append(post)
        return converted_posts

    def print_converted_posts(self):
        converted_posts = self.get_converted_posts()
        if len(converted_posts) == 0:
            print("No converted posts found.")
        else:
            print("\nConverted posts:")
            for post in converted_posts:
                print(f"Post ID: {post['id']}, Title: {post['title']}, Author: {post['author']}, Instagram: {post['instagram']}\n")

    def delete_post(self, post_id):
        self.cursor.execute("DELETE FROM converted_videos WHERE post_id = ?", (post_id,))
        self.conn.commit()

    def update_instagram_field(self, post_id):
        self.cursor.execute("UPDATE converted_videos SET instagram = ? WHERE post_id = ?", (True, post_id))
        self.conn.commit()
