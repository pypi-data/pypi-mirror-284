from typing import Union
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from aiohttp_simple.template.data_model import Paginate

from aiohttp_simple.utils.contextvar import mysqlClient

class BaseService:
    def __init__(self):
        self.engine = mysqlClient.get()

    def async_session(self) -> AsyncSession:
        return sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)()  # type: ignore

    def generate_query(self, base_sql, paginate: Paginate):
        query_sql = base_sql.offset(paginate.offset).limit(paginate.limit)
        total_sql = select(func.count()).select_from(base_sql)
        return query_sql, total_sql
    
    def query_result_to_dict(self, queryResult, first=False) -> Union[dict, list[dict]]:
        if first:
            queryData = queryResult.one_or_none()
        else:
            queryData = queryResult.all()
        if not queryData:
            return queryData
        if first:
            return dict(zip(queryResult.keys(),queryData))
        return list(map(lambda row: dict(zip(queryResult.keys(),row)), queryData))
