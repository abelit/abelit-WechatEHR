# -*- encoding: utf-8 -*-
'''
@File    :   manage.py
@Time    :   2020/12/15 15:07:33
@Author  :   Abelit 
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
@Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from wechatehr.db import db

# from main import create_app
from wechatehr import create_app

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

# add db migration command
manager.add_command('db', MigrateCommand)

# add custom command
@manager.option("-n", "--name", dest="name", default="www.baidu.com")
def foo(name):
    print("foo!")
    print(name)

@manager.option("-n", "--name", dest="name", default="www.baidu.com")
def bar(name):
    print("bar!")
    print(name)

if __name__ == '__main__':
    manager.run()