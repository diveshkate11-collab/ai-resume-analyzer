from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func

from app.database.base import Base


class Resume(Base):
    """
    Resume database model.
    """

    __tablename__ = "resumes"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    filename = Column(
        String,
        nullable=False,
    )

    filepath = Column(
        String,
        nullable=False,
    )

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )