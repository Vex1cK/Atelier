from database import Base, str_255
from sqlalchemy import String, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum
from typing import Annotated, Optional
import datetime

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at_utc = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at_utc = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)]
created_at_msk = Annotated[datetime.datetime, mapped_column(server_default=func.now())]
updated_at_msk = Annotated[datetime.datetime, mapped_column(server_default=func.now(), onupdate=datetime.datetime.now)]

class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    name: Mapped[str]


class Workload(Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class ResumesOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    title: Mapped[str_255]
    salary: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete="CASCADE"))
    created_at: Mapped[created_at_msk]
    updated_at: Mapped[updated_at_msk]
