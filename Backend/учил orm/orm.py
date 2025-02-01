from database import session_factory, Base, engine
from sqlalchemy import text
from models import WorkersOrm


def create_tables():
    engine.echo = True
    # Base.metadata.tables['resumes'].drop(engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def insert_workers():
    with session_factory() as ses:
        vova = WorkersOrm(name="Vova")
        misha = WorkersOrm(name="Misha")
        ses.add_all([vova, misha])
        ses.commit()
