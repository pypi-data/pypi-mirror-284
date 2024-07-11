# -*- coding: utf-8 -*-

from sqlman import Handler

cfg = {
    'username': 'admin',
    'password': 'admin@1',
    'db': 'test'
}
handler = Handler(**cfg)
print(handler.get_tables())
TEST = handler["test"]
print(TEST.get_tables())
TEST.scan(once=3, rest=2)
# for name in handler.get_tables():
#     handler.pick_table(name).remove()


from sqlman.handler import *
# tc1 = handler.pick_table('testaa')

from feapder.db.mysqldb import MysqlDB
db = MysqlDB(ip="localhost", port=3306, db="aaa", user_name="root", user_pass="root@0")
print(db)