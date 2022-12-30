# !/usr/bin/env python
# -*- coding=utf-8 -*-
from src.utils.query_sql import query_sql

sql = "CREATE TABLE cards (\
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '编号',\
    name VARCHAR(255) NOT NULL COMMENT '名称',\
    description TEXT NOT NULL COMMENT '描述',\
    type VARCHAR(255) NOT NULL COMMENT '类型',\
    attribute VARCHAR(255) NOT NULL COMMENT '属性',\
    `level` INT COMMENT '等级',\
    `rank` INT COMMENT '阶级',\
    `attack` INT COMMENT '攻击力',\
    `defense` INT COMMENT '守备力',\
    rarity VARCHAR(255) NOT NULL COMMENT '稀有度',\
    price INT COMMENT '价格',\
    image_url VARCHAR(255) NOT NULL COMMENT '卡图地址',\
    created_at DATETIME NOT NULL COMMENT '创建时间',\
    updated_at DATETIME NOT NULL COMMENT '更新时间'\
);\
"

result = query_sql(sql)
print(result)
