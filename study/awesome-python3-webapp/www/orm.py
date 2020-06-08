#!/usr/bin/python3
# _*_coding:utf-8_*_

import asyncio, logging, alomysql


def log(sql, args=()):
    logging.ingo("SQL: %s"%sql)


async def create_poll(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
            host=kw.get('host','localhost'),
            prot=kw.get('port',3306)
            user=kw['user'],
            password=kw['password'],
            db=kw['db']
            charset=kw.get('charset','utf8'),
            autocommit=kw.get('maxsize',10),
            minsize=kw.get('minsize',1)
            loop=loop
    )


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DicCursor)
        await cur.execute(sql.replace('?','%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s'%len(rs))
        return rs


async def execute(sql, args):
    log(sql)
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?','%s'), args)
            affected = cur.rowcout
            await cur.close()
        except BaseException as e:
            raise
        return affected































    
