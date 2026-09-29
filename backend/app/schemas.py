from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    location: str | None = None
    job_type: str | None = None
    description: str | None = None
    application_url: str | None = None
    status: str = "saved"


class JobResponse(JobCreate):
    id: int

    class Config:
        from_attributes = True