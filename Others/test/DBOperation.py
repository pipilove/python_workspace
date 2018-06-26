#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'python连接mysql数据库操作'
__author__ = ''
__mtime__ = '5/12/2018-012'
__email__ = 'pipijob@126.com'
"""
try:
    import MySQLdb  # py2
except:
    import pymysql  # py3
import traceback

epslon = '1e-5'
py_version = 3


class MySQLOpt():
    def __init__(self):
        self.connectDB()
        # print('Database Connected!!!')

    def __del__(self):
        self.closeDB()
        # print('Database Closed!!!')

    def test(self):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchone()

        print("Database version : %s " % data)

    def connectDB(self):
        # 打开数据库连接
        try:
            if py_version == 2:
                self.db = MySQLdb.connect("localhost", "root", "249784435", "simplecms", charset='utf8')
            else:
                self.db = pymysql.connect("localhost", "root", "249784435", "simplecms", charset='utf8')
        except:
            print('no such database')
            # print(traceback.format_exc())

    def closeDB(self):
        # 关闭数据库连接
        self.db.close()

    def createTable(self, table_name, table_field, drop=False):
        '''
        创建表
        :param table_name:
        :param table_field:
        :param drop:
        :return:
        '''
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # 如果数据表已经存在使用 execute() 方法删除表。
        if drop:
            cursor.execute("drop table if exists " + table_name)

        sql = "CREATE TABLE " + table_name + " (" + table_field + ")"
        try:
            cursor.execute(sql)
        except:
            print(traceback.format_exc())

    def insertField(self, table_name, values):
        '''
        插入数据
        :param table_name:
        :param values:
        :return:
        '''
        cursor = self.db.cursor()

        sql = "INSERT INTO " + table_name + " VALUES (" + values + ")"
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            # Rollback in case there is any error
            print('rollback')
            print(traceback.format_exc())
            self.db.rollback()

    def updateField(self, table_name, orders):
        '''
        更新数据
        :param table_name:
        :param orders:
        :return:
        '''
        cursor = self.db.cursor()

        sql = "UPDATE " + table_name + " " + orders
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            # Rollback in case there is any error
            print('rollback')
            print(traceback.format_exc())
            self.db.rollback()

    def deleteField(self, table_name, orders=''):
        '''
        删除数据
        :param table_name:
        :param orders:
        :return:
        '''
        cursor = self.db.cursor()

        sql = "DELETE FROM " + table_name + " " + orders
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            # Rollback in case there is any error
            print('rollback')
            print(traceback.format_exc())
            self.db.rollback()

    def showTable(self, table_name, orders=''):
        '''
        显示数据
        :param table_name:
        :param orders:
        :return:
        '''
        cursor = self.db.cursor()
        sql = "select * from " + table_name + ' ' + orders
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
        except:
            print("Error: unable to fecth data")
            print(traceback.format_exc())


if __name__ == '__main__':
    sql = MySQLOpt()

    table_name = 'version_grade'
    table_field = """
                 SHA1  CHAR(20) NOT NULL,
                 SHA2  CHAR(20) NOT NULL,
                 time  CHAR(20),
                 grade1 FLOAT,
                 grade2 FLOAT
                 """
    # sql.createTable(table_name, table_field, drop=True)

    sql.insertField(table_name, values="'123', '234', '20180101', 0.21, 0.21")
    sql.updateField(table_name, orders='SET grade1 = grade1 + 0.1 where ABS(grade1- 0.21) < ' + epslon)

    # sql.deleteField(table_name, orders='WHERE grade1 like 0.21')
    # sql.deleteField(table_name)

    sql.showTable(table_name)
