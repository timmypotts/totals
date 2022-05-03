import sqlalchemy

db = sqlalchemy.create_engine('postgresql://postgres:a0E24me@localhost:5432/mlb')

field = Table('user', metadata_obj)