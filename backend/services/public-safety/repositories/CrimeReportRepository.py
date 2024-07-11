from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:password@host:port/dbname')
Session = sessionmaker(bind=engine)

class CrimeReportRepository:
    def __init__(self):
        self.session = Session()

    def create_crime_report(self, crime_report: CrimeReport):
        self.session.add(crime_report)
        self.session.commit()

    def get_crime_report(self, id: int):
        return self.session.query(CrimeReport).filter_by(id=id).first()
