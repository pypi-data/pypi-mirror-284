import random

from faker import Faker
from loguru import logger
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

from pgman.utils import make_result, getfv, reduce_sql


class PostgreSQL:
    def __init__(self, host="localhost", port=5432, db=None, user=None, password=None):
        self.pool = pool.ThreadedConnectionPool(
            minconn=1, maxconn=5,
            host=host, port=port, dbname=db,
            user=user, password=password
        )

    def _open(self, dict_cursor=True):
        """打开连接"""
        con = self.pool.getconn()
        cur = con.cursor(cursor_factory=RealDictCursor) if dict_cursor else con.cursor()
        return cur, con

    def _close(self, cur, con):
        """关闭连接"""
        if cur:
            cur.close()
        if con:
            self.pool.putconn(con)

    def exe_sql(self, sql: str, args: tuple = None, query_all: bool = None, to_dict=True, serious=False) -> dict:
        cur, con = None, None
        try:
            cur, con = self._open(to_dict)
            sql, args = reduce_sql(sql), args or None
            cur.execute(sql, args)
            con.commit()
            if query_all is None:
                result = None
            else:
                if query_all:
                    result = [dict(v) if to_dict else v for v in cur.fetchall()]
                else:
                    result = dict(cur.fetchone()) if to_dict else cur.fetchone
            return make_result(status=1, affect=cur.rowcount, result=result)
        except Exception as e:
            logger.error("{} | {}".format(str(e).rstrip(), type(e)))
            if serious:
                raise e
            return make_result(status=0, affect=0, error=str(e))
        finally:
            self._close(cur, con)

    def exem_sql(self, sql: str, args=None, serious=False) -> int:
        cur, con = None, None
        try:
            cur, con = self._open()
            sql, args = reduce_sql(sql), args or None
            cur.executemany(sql, args)
            con.commit()
            return cur.rowcount
        except Exception as e:
            logger.error("{} | {}".format(str(e).rstrip(), type(e)))
            if serious:
                raise e
            return 0
        finally:
            self._close(cur, con)

    def _add_one(self, table: str, one: dict) -> int:
        """添加一条数据"""
        fields, values = getfv(one)
        sql = 'insert into {}({}) value({})'.format(table, fields, values)
        args = tuple(one.values())
        res = self.exe_sql(sql, args=args)
        return res['affect']

    def _add_many(self, table: str, many: list) -> int:
        """添加多条数据"""
        fields, values = getfv(many)
        sql = 'insert into {}({}) values({})'.format(table, fields, values)
        args = [tuple(item.values()) for item in many]
        affect = self.exem_sql(sql, args=args)
        return affect

    def add(self, table: str, data: dict | list):
        """智能添加数据"""
        if isinstance(data, dict):
            return self._add_one(table, data)
        elif isinstance(data, list):
            return self._add_many(table, data)
        else:
            raise Exception("The data parameter can only be a dict or list")

    def make_table(self, table="people", count=10000):
        """制造一张测试表"""
        sql = """
            CREATE TABLE {} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                gender CHAR(1),
                age INT,
                phone VARCHAR(11),
                ssn VARCHAR(18),
                job VARCHAR(200),
                salary INT,
                company VARCHAR(200),
                address VARCHAR(200),
                mark CHAR(1)
            );
        """.format(table)
        self.exe_sql(sql, serious=True)
        logger.info("表创建成功 | {}".format(table))

        faker = Faker("zh_cn")
        once = 1000
        new = 0

        def make_one():
            one = {
                'name': faker.name(),
                'gender': random.choice(['男', '女']),
                'age': faker.random.randint(18, 60),
                'phone': faker.phone_number(),
                'ssn': faker.ssn(),
                'job': faker.job(),
                'salary': faker.random_number(digits=4),
                'company': faker.company(),
                'address': faker.address(),
                'mark': faker.random_letter()
            }
            return one

        def todb():
            many = [make_one() for _ in range(once)]
            add = self.add(table, many)
            nonlocal new
            new += add
            logger.success("{} | 插入{}条 | 累计{}条".format(table, add, new))

        for _ in range(count // once):
            todb()

        if _ := new % once:
            todb()
