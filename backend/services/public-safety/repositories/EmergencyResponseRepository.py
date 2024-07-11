from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:password@host:port/dbname')
Session = sessionmaker(bind=engine)

class EmergencyResponseRepository:
    def __init__(self):
        self.session = Session()

    def create_emergency_response(self, emergency_response: EmergencyResponse):
        self.session.add(emergency_response)
        self.session.commit()

    def get_emergency_response(self, id: int):
        return self.session.query(EmergencyResponse).filter_by(id=id).first()
