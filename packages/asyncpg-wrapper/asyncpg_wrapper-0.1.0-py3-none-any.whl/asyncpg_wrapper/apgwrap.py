import asyncio
import traceback
import logging
import asyncpg
from typing import List, Dict

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
            p = "("+'),('.join([','.join([value for value in record.values()]) for record in values])+")"
            query = f"INSERT INTO {table} ({', '.join(values[0].keys())}) VALUES "
            query += p
            #query += ', '.join([f"({', '.join(['$' + str(i + 1) for i in range(len(record.keys()))])})" for record in values])
            query += " ON CONFLICT DO NOTHING"
            query += " RETURNING *"

            records = [dict(record) for record in await conn.fetch(query)]
            return records
        except Exception as e:
            LOGGER.critical(e, exc_info=True)
        finally:
            await conn.close()

    async def update(self, table: str, where_stmt:str, values: Dict) -> Dict:
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


# Пример использования:
async def main():
    dsn = "postgresql://postgres:psqlpass@10.8.0.5/vindcgibdd"
    db = AsyncDB(dsn)


    #l = [{'id': 1, 'value': 'John Doe'}, {'id': 2, 'value': 'John Doe'}, {'id': 3, 'value': '13272'}, {'id': 4, 'value': '14166'}, {'id': 5, 'value': '10825'}, {'id': 6, 'value': '15030'}, {'id': 7, 'value': '12338'}, {'id': 8, 'value': '5372'}, {'id': 9, 'value': '1786'}, {'id': 10, 'value': '7138'}, {'id': 11, 'value': '3941'}, {'id': 12, 'value': '90'}, {'id': 13, 'value': '6636'}, {'id': 14, 'value': '16056'}, {'id': 15, 'value': '12277'}, {'id': 16, 'value': '14355'}, {'id': 17, 'value': '10993'}, {'id': 18, 'value': '10146'}, {'id': 19, 'value': '8956'}, {'id': 20, 'value': '9091'}, {'id': 21, 'value': '9954'}, {'id': 22, 'value': '8542'}, {'id': 23, 'value': '1339'}, {'id': 24, 'value': '195'}, {'id': 25, 'value': '9649'}, {'id': 26, 'value': '6307'}, {'id': 27, 'value': '13106'}, {'id': 28, 'value': '12744'}, {'id': 29, 'value': '3929'}, {'id': 30, 'value': '7772'}, {'id': 31, 'value': '14403'}, {'id': 32, 'value': '7476'}, {'id': 33, 'value': '13759'}, {'id': 34, 'value': '74'}, {'id': 35, 'value': '3443'}, {'id': 36, 'value': '7446'}, {'id': 37, 'value': '1193'}, {'id': 38, 'value': '8800'}, {'id': 39, 'value': '7514'}, {'id': 40, 'value': '11744'}, {'id': 41, 'value': '4845'}, {'id': 42, 'value': '1861'}, {'id': 43, 'value': '995'}, {'id': 44, 'value': '1797'}, {'id': 45, 'value': '15344'}, {'id': 46, 'value': '8395'}, {'id': 47, 'value': '11874'}, {'id': 48, 'value': '2989'}, {'id': 49, 'value': '3092'}, {'id': 50, 'value': '11058'}, {'id': 51, 'value': '13512'}, {'id': 52, 'value': '2418'}, {'id': 53, 'value': '12417'}, {'id': 54, 'value': '11178'}, {'id': 55, 'value': '11681'}, {'id': 56, 'value': '10566'}, {'id': 57, 'value': '11580'}, {'id': 58, 'value': '1644'}, {'id': 59, 'value': '13961'}, {'id': 60, 'value': '14912'}, {'id': 61, 'value': '8130'}, {'id': 62, 'value': '15148'}, {'id': 63, 'value': '9426'}, {'id': 64, 'value': '13651'}, {'id': 65, 'value': '11091'}, {'id': 66, 'value': '10128'}, {'id': 67, 'value': '14373'}, {'id': 68, 'value': '14143'}, {'id': 69, 'value': '14101'}, {'id': 70, 'value': '14779'}, {'id': 71, 'value': '437'}, {'id': 72, 'value': '8453'}, {'id': 73, 'value': '6710'}, {'id': 74, 'value': '1749'}, {'id': 75, 'value': '8021'}, {'id': 76, 'value': '8321'}, {'id': 77, 'value': '2999'}, {'id': 78, 'value': '10165'}, {'id': 79, 'value': '8935'}, {'id': 80, 'value': '16452'}, {'id': 81, 'value': '5991'}, {'id': 82, 'value': '13526'}, {'id': 83, 'value': '11880'}, {'id': 84, 'value': '8060'}, {'id': 85, 'value': '598'}, {'id': 86, 'value': '10338'}, {'id': 87, 'value': '9405'}, {'id': 88, 'value': '13582'}, {'id': 89, 'value': '9710'}, {'id': 90, 'value': '4985'}, {'id': 91, 'value': '8948'}, {'id': 92, 'value': '2126'}, {'id': 93, 'value': '15664'}, {'id': 94, 'value': '10633'}, {'id': 95, 'value': '3209'}, {'id': 96, 'value': '12362'}, {'id': 97, 'value': '1355'}, {'id': 98, 'value': '9841'}, {'id': 99, 'value': '5670'}, {'id': 100, 'value': '7515'}, {'id': 101, 'value': '12738'}, {'id': 102, 'value': '3026'}, {'id': 103, 'value': '14967'}, {'id': 104, 'value': '11185'}, {'id': 105, 'value': '9301'}, {'id': 106, 'value': '11304'}, {'id': 107, 'value': '5700'}, {'id': 108, 'value': '12404'}, {'id': 109, 'value': '6413'}, {'id': 110, 'value': '13455'}, {'id': 111, 'value': '9473'}, {'id': 112, 'value': '1941'}, {'id': 113, 'value': '12298'}, {'id': 114, 'value': '12705'}, {'id': 115, 'value': '435'}, {'id': 116, 'value': '9444'}, {'id': 117, 'value': '3665'}, {'id': 118, 'value': '613'}, {'id': 119, 'value': '6679'}, {'id': 120, 'value': '11327'}, {'id': 121, 'value': '7788'}, {'id': 122, 'value': '13206'}, {'id': 123, 'value': '14910'}, {'id': 124, 'value': '13720'}, {'id': 125, 'value': '1589'}, {'id': 126, 'value': '6482'}, {'id': 127, 'value': '7753'}, {'id': 128, 'value': '4872'}, {'id': 129, 'value': '13176'}, {'id': 130, 'value': '9239'}, {'id': 131, 'value': '7403'}, {'id': 132, 'value': '3635'}, {'id': 133, 'value': '5929'}, {'id': 134, 'value': '14584'}, {'id': 135, 'value': '11853'}, {'id': 136, 'value': '2708'}, {'id': 137, 'value': '2728'}, {'id': 138, 'value': '3828'}, {'id': 139, 'value': '3911'}, {'id': 140, 'value': '1389'}, {'id': 141, 'value': '14629'}, {'id': 142, 'value': '11666'}, {'id': 143, 'value': '10182'}, {'id': 144, 'value': '12276'}, {'id': 145, 'value': '7106'}, {'id': 146, 'value': '5513'}, {'id': 147, 'value': '2060'}, {'id': 148, 'value': '12106'}, {'id': 149, 'value': '426'}, {'id': 150, 'value': '791'}]

    # Примеры операций:
    # new_record = await db.insert('tg.tst', {'value': f'{random.randint(0,16473)}'})
    # print(new_record)

    # l = []
    # for i in range(0, 1000):
    #     l.append({'value': str(random.randint(0,16473))})
    # new_records = await db.insertmany('tg.tst', l)
    # print(new_records)

    #
    # updated_record = await db.update('tg.tst', "id=372",{'id': 372, 'value': 'UPDATED'})
    # print(updated_record)
    #
    # deleted_records = await db.delete('tg.tst')
    # print(deleted_records)

    # selected_records = await db.select('tg.tst')
    # print(json.dumps(selected_records, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    # Запуск примера:
    asyncio.run(main())
