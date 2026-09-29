from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    company = Column(String(200), nullable=False)
    location = Column(String(200), nullable=True)
    job_type = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    application_url = Column(String(500), nullable=True)
    status = Column(String(50), default="saved")