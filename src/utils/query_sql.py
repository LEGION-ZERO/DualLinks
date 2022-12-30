# !/usr/bin/env python
# -*- coding=utf-8 -*-
import pymysql
import psycopg2
import global_conf


def query_sql(sql: str):
    """
    根据数据库类型及sql查询结果
    :param sql: 要查询的sql语句
    :return: 查询结果
    """
    # 连接到数据库
    db_type = global_conf.get_conf_from_file("database.yml", "database.db_type", "mysql")
    host = global_conf.get_conf_from_file("database.yml", "database.host", "127.0.0.1")
    user = global_conf.get_conf_from_file("database.yml", "database.user", "root")
    password = global_conf.get_conf_from_file("database.yml", "database.password", "root")
    db = global_conf.get_conf_from_file("database.yml", "database.db_name", "test")

    if db_type == 'mysql':
        conn = pymysql.connect(host=host, user=user, password=password, db=db)
    elif db_type == 'postgres':
        conn = psycopg2.connect(host=host, user=user, password=password, dbname=db)
    else:
        # 如果数据库类型未被识别，则抛出错误
        raise ValueError("未识别的数据库类型: {}".format(db_type))

    # 创建游标
    cursor = conn.cursor()

    # 执行查询语句
    cursor.execute(sql)

    # 获取查询结果
    result = cursor.fetchall()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()

    return result
