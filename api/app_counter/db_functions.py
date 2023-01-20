from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
from typing import List

from . import models_db


def get_counter(db_session, id:str):
    result = db_session.query(models_db.Counter).filter(models_db.Counter.id==id).first()
    return result

def set_counter(db_session, id:str, step:int, ip:str):
    db_query = get_counter(db_session, id)
    if db_query:    # Check if db_query is not None (null)
        number = db_query.counter + step
        db_query.counter = number
        db_query.ip_updated = ip
        db_session.commit()
        # print(f'dotaz neni prazdnej a vysledek je {db_query}')
        return db_query
    else:
        new_db_obj = models_db.Counter(id=id, counter=step, ip_created=ip, ip_updated=ip)
        db_session.add(new_db_obj)
        db_session.commit()
        # print(f'dotaz byl prazdnej a vysledek je {new_db_obj}')
        return db_query
    

