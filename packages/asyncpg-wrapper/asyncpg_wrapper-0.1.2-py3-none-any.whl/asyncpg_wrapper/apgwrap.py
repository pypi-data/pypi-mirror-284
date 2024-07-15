import asyncio
import logging
from typing import List, Dict
import asyncpg

__all__ = 'AsyncDB'
LOGGER = logging.getLogger(__name__)


class AsyncDB:
    def __init__(self, dsn: str):
        self.dsn = dsn

    async def insert(self, table: str, values: Dict) -> Dict:
        conn = await asyncpg.connect(self.dsn)
        try:
            query = f"INSERT INTO {table} ({', '.join(values.keys())}) VALUES ({', '.join(['$' + str(i + 1) for i in range(len(values))])}) RETURNING *"
            record = await conn.fetchrow(query, *values.values())
            return dict(record) if record else None
        except Exception as e:
            LOGGER.critical(e, exc_info=True)
        finally:
            await conn.close()

    async def insertmany(self, table: str, values: List[Dict]) -> List[Dict]:
        conn = await asyncpg.connect(self.dsn)
        try:
            if len(values) > 1000:
                raise ValueError('Values count must be less or equal than 1000.')
            # Подготавливаем SQL-запрос для вставки множества записей
            p = "(" + '),('.join([','.join([value for value in record.values()]) for record in values]) + ")"
            query = f"INSERT INTO {table} ({', '.join(values[0].keys())}) VALUES "
            query += p
            # query += ', '.join([f"({', '.join(['$' + str(i + 1) for i in range(len(record.keys()))])})" for record in values])
            query += " ON CONFLICT DO NOTHING"
            query += " RETURNING *"

            records = [dict(record) for record in await conn.fetch(query)]
            return records
        except Exception as e:
            LOGGER.critical(e, exc_info=True)
        finally:
            await conn.close()

    async def update(self, table: str, where_stmt: str, values: Dict) -> Dict:
        conn = await asyncpg.connect(self.dsn)
        try:
            set_clause = ', '.join([f"{key} = ${i + 1}" for i, key in enumerate(values.keys())])
            query = f"UPDATE {table} SET {set_clause} WHERE {where_stmt} RETURNING *"
            record = await conn.fetchrow(query, *values.values())
            return dict(record) if record else None
        except Exception as e:
            LOGGER.critical(e, exc_info=True)
        finally:
            await conn.close()

    async def delete(self, table: str, where_stmt: str | None = None) -> List[Dict]:
        conn = await asyncpg.connect(self.dsn)
        try:
            if where_stmt:
                query = f"DELETE FROM {table} WHERE {where_stmt} RETURNING *"
            else:
                query = f"DELETE FROM {table} RETURNING *"
            records = await conn.fetch(query)
            return [dict(record) for record in records]
        except Exception as e:
            LOGGER.critical(e, exc_info=True)
        finally:
            await conn.close()

    async def select(self, table: str, where_stmt: str | None = None) -> List[Dict]:
        conn = await asyncpg.connect(self.dsn)
        try:
            if where_stmt:
                query = f"SELECT * FROM {table} WHERE {where_stmt}"
            else:
                query = f"SELECT * FROM {table}"
            records = await conn.fetch(query)
            return [dict(record) for record in records]
        except Exception as e:
            LOGGER.critical(e, exc_info=True)
        finally:
            await conn.close()
