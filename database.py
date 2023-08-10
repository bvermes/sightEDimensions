import psycopg2
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

load_dotenv()

url = "POSTGRE_URL"
CREATE_DIMENSIONS_TABLE = """
CREATE TABLE IF NOT EXISTS dimensions(
    id SERIAL PRIMARY KEY,
    x INTEGER,
    y INTEGER,
    z INTEGER,
    t INTEGER,
    value INTEGER
    );
"""

SELECT_ALL_DIMENSIONS = """SELECT * FROM dimensions;"""
INSERT_DIMENSION = """INSERT INTO dimensions (x, y, z, t, value) VALUES (%s, %s, %s, %s, %s);"""

connection = psycopg2.connect(url)


def create_table():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_DIMENSIONS_TABLE)


def get_dimensions():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_DIMENSIONS)
            return cursor.fetchall()


def get_specific_column(x):
    SELECT_SPECIFIC_COLUMNS= f"SELECT {x} FROM dimensions"
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_SPECIFIC_COLUMNS)
            return cursor.fetchall()


def loaddata(xml_text):
    # Parse the XML data
    tree = ET.ElementTree(ET.fromstring(xml_text))
    root = tree.getroot()
    with connection:
        with connection.cursor() as cursor:
            for row in root.findall('row'):
                # Extract data from the XML elements
                x = row.find('x').text
                y = row.find('y').text
                z = row.find('z').text
                t = row.find('t').text
                value = row.find('values').text
                values = (x, y, z, t, value)
                cursor.execute(INSERT_DIMENSION, values)
                connection.commit()

