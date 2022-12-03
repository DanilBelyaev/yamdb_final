import csv
import datetime
import sqlite3

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        created_date = datetime.datetime.now()

        with open('static/data/users.csv', encoding="utf8") as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['id'], i['username'], i['email'], i['role'], i['bio'],
                      i['first_name'], i['last_name'], '', False, False, False,
                      created_date) for i in dr]
        insert_records = '''INSERT INTO main.reviews_user
                         (id, username, email, role, bio, first_name,
                         last_name, password, is_superuser, is_staff,
                         is_active, date_joined)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
        cursor.executemany(insert_records, to_db)

        with open('static/data/genre.csv', encoding="utf8") as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['id'], i['name'], i['slug']) for i in dr]

        insert_records = '''INSERT INTO main.reviews_genre (id, name, slug) '
                        VALUES (?, ?, ?);'''
        cursor.executemany(insert_records, to_db)

        with open('static/data/category.csv', encoding="utf8") as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['id'], i['name'], i['slug']) for i in dr]
        insert_records = '''INSERT INTO main.reviews_category
                         (id, name, slug) VALUES (?, ?, ?);'''
        cursor.executemany(insert_records, to_db)

        with open('static/data/titles.csv', encoding="utf8") as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['id'], i['name'], i['year'],
                      i['category'], '') for i in dr]
        insert_records = '''INSERT INTO main.reviews_title (id, name, year,
                         category_id, description) VALUES (?, ?, ?, ?, ?);'''
        cursor.executemany(insert_records, to_db)

        with open('static/data/genre_title.csv', encoding="utf8") as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['id'], i['title_id'], i['genre_id']) for i in dr]
        insert_records = '''INSERT INTO main.reviews_title_genre
                         (id, title_id, genre_id) VALUES (?, ?, ?);'''
        cursor.executemany(insert_records, to_db)

        with open('static/data/review.csv', encoding="utf8") as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['id'], i['text'], i['score'], i['pub_date'],
                      i['author']) for i in dr]
        insert_records = '''INSERT INTO main.reviews_review (id, text,
                         score, pub_date, author_id) VALUES (?, ?, ?, ?, ?);'''
        cursor.executemany(insert_records, to_db)

        with open('static/data/comments.csv', encoding="utf8") as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['id'], i['text'], i['pub_date'], i['author'],
                      i['review_id']) for i in dr]
        insert_records = '''INSERT INTO main.reviews_comment (id, text,
                         pub_date, author_id, review_id)
                         VALUES (?, ?, ?, ?, ?);'''
        cursor.executemany(insert_records, to_db)

        connection.commit()
        connection.close()
