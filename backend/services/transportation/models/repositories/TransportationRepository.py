from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:password@host:port/dbname')
Session = sessionmaker(bind=engine)

class TransportationRepository:
    def __init__(self):
        self.session = Session()

    def create_transportation(self, transportation: Transportation):
        self.session.add(transportation)
        self.session.commit()

    def get_transportation(self, id: int):
        return self.session.query(Transportation).filter_by(id=id).first()
