import logging
from contextlib import contextmanager
from typing import NewType

from sqlmodel.ext.asyncio.session import AsyncSession

from edgegap_database._configuration import DatabaseConfiguration

from ._async_engine import AsyncDatabaseEngine
from ._async_session_factory import AsyncSessionFactory

logger = logging.getLogger(__name__)

AsyncReadSession = NewType('ReadSession', AsyncSession)
AsyncWriteSession = NewType('WriteSession', AsyncSession)


class AsyncDatabaseSession:
    @staticmethod
    @contextmanager
    def get_session(configuration: DatabaseConfiguration):
        engine = AsyncDatabaseEngine(configuration).get_write_engine()
        session = AsyncSession(engine)

        try:
            yield session
        finally:
            session.close()

    @staticmethod
    @contextmanager
    def get_write_session(configuration: DatabaseConfiguration, session_factory: AsyncSessionFactory):
        engine = AsyncDatabaseEngine(configuration).get_write_engine()
        session = session_factory.create_session(engine)

        try:
            yield session
        finally:
            session.close()

    @staticmethod
    @contextmanager
    def get_read_session(configuration: DatabaseConfiguration, session_factory: AsyncSessionFactory):
        engine = AsyncDatabaseEngine(configuration).get_read_engine()
        session = session_factory.create_session(engine)

        try:
            yield session
        finally:
            session.close()
