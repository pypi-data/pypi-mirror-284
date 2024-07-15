# 更新日志

- 第一版
- 添加数据时，表名称加入双引号，避免跟关键字冲突

# 连接PostgreSQL

```python


from pgman import PostgreSQL

pg = PostgreSQL(db="test", user="wauo", password="123456")

name = "people"
pg.make_table(name)

res = pg.exe_sql("select * from people limit 10", query_all=True)
print(res)
```
