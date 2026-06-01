from app.db.session import Base
from app.db.session import engine

import app.db.base


def init_db():
    Base.metadata.create_all(
        bind=engine,
    )
