from sexgraph import sexgraph_db
import os
from dotenv import load_dotenv
import rsa
from uuid import uuid4, UUID


# get environmental variables
load_dotenv()
DB_CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")


def get_engine():
    return create_engine(DB_CONNECTION_STRING)


def get_new_keys(length=2048):
    public_key, private_key = rsa.newkeys(length)

    return (public_key, private_key)


def encrypt(plaintext, public_key=PUBLIC_KEY):
    return rsa.encrypt(plaintext.encode(), public_key)


def decrypt(ciphertext, private_key=PRIVATE_KEY):
    return rsa.decrypt(ciphertext, private_key).decode()


def validate_uuid(uuid_str, version=4):
    try:
        uuid_obj = UUID(uuid_str, version=version)
    except ValueError:
        return False

    return str(uuid_obj) == uuid_str


def insert_university(name, email_domain, max_num_students):
    def insert_node():
        uuid_plaintext = uuid4()
        uuid_ciphertext = encrypt(uuid_plaintext)

        # TODO: insert into database table Node

    # TODO: check that university name and email are not taken already

    # TODO: insert university

    # insert nodes for university
    for i in range(max_num_students):
        insert_node()
