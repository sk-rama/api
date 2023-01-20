import sqlalchemy as db
from .database import Base

class Counter(Base):
    __tablename__ = 'counter'

    id = db.Column(db.String, primary_key=True)
    counter = db.Column(db.Integer)
    ip_created = db.Column(db.String)
    ip_updated = db.Column(db.String)

    def __repr__(self):
        return(f"Counter(id={self.id}, counter={self.counter}), ip_created={self.ip_created}, ip_updated={self.ip_updated}\n")