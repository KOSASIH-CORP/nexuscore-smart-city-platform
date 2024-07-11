from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:password@host:port/dbname')
Session = sessionmaker(bind=engine)

class SafetyAnalyticsRepository:
    def __init__(self):
        self.session = Session()

    def create_safety_analytics(self, safety_analytics: SafetyAnalytics):
        self.session.add(safety_analytics)
        self.session.commit()

    def get_safety_analytics(self, id: int):
        return self.session.query(SafetyAnalytics).filter_by(id=id).first()
