#!/usr/bin/python

import os
import sys
import psycopg2
import boto3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()
AWS_ACCESS_KEY_ID = os.environ["MINIO_ROOT_USER"]
AWS_SECRET_ACCESS_KEY = os.environ["MINIO_ROOT_PASSWORD"]

POSTGRES_DB = os.environ["POSTGRES_DB"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
TABLE_NAME = os.environ["TABLE_NAME"]

DB_PORT = os.environ["DB_PORT"]
DB_HOST = os.environ["DB_HOST"]

S3_PORT = os.environ["S3_PORT"]
PATH = 'http://localhost:' + S3_PORT


def connect_s3(path, bucket):
    s3 = boto3.resource('s3',
                        endpoint_url=path,
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    my_bucket = s3.Bucket(bucket)

    data = []
    for obj in my_bucket.objects.all():
        body = obj.get()['Body']
        data.append(pd.read_csv(body, skiprows=1, header=None))
    return data


def copy_to_db(data_):
    db_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT, POSTGRES_DB)
    db = create_engine(db_string)
    connection = db.connect()
    for line in data_:
        db.execute(f"INSERT INTO {TABLE_NAME} VALUES ("
                   f"{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},"
                   f"{line[6]},{line[7]},{line[8]},{line[9]},{line[10]},"
                   f"{line[11]});")
    connection.close()


if __name__ == '__main__':
    # if sys.argv[1]:
    #     PATH = sys.argv[1]
    #     BUCKET = Path(PATH).name
    #     connect_s3(PATH, BUCKET)
    # PATH = 'http://localhost:9001/buckets/test_bucket/'
    # BUCKET = Path(PATH).name
    BUCKET = 'test_bucket'
    data = connect_s3(PATH, BUCKET)
    copy_to_db(data)

