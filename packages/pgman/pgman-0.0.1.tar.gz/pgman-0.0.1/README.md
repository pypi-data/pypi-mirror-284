# 连接PostgreSQL

```python
from pgman.connector import PostgreSQL

pg = PostgreSQL(db="test", user="wauo", password="123456")

name = "people"
pg.make_table(name)

res = pg.exe_sql("select * from people limit 10", query_all=True)
print(res)
```
