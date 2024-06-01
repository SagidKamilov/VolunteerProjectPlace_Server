#System
from typing import List, Union

#Other libraries
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

#Local
from src.repository.general_sql_repository import GeneralSQLRepository
from src.model.order import Order


class OrderRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Order):
        super().__init__(session=session, model=model)