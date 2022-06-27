"""
    DEMO APP TO FETCH A JSON ENDPOINT AND STORE DATA IN MYSQL DATABASE
"""

import requests
from mysql.connector import connect, Error


def main():
    """ MAIN FUNCTION: FOR LOCAL SCOPING """

    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    insert_posts_query = """
            INSERT INTO posts
            (user_id, title, body)
            VALUES ( %s, %s, %s )
        """
    insert_posts_records = [
        (post['userId'], post['title'], post['body']) for post in response.json()
    ]
    # print(insert_posts_query)
    # print(insert_posts_records)

    try:
        with connect(
            host="localhost",
            user="root",
            password="",
            database="posts",
        ) as connection:
            print("Connection to DB succeeded!")
            with connection.cursor() as cursor:
                cursor.executemany(insert_posts_query, insert_posts_records)
                connection.commit()
    except Error as err_msg:
        print(err_msg)


if __name__ == '__main__':
    main()
