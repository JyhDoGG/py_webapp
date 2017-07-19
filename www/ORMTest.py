#!/usr/bin/env python3
#coding=utf-8

import ORM
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await ORM.create_pool(loop=loop,user='blogadmin', password='jyh001', db='blog_app')

    u = User(name='Test3', email='test3@example.com', passwd='12345678903', image='about:blank')

    await u.save()

loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()