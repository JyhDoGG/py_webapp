#!/usr/bin/env python3
#coding=utf-8

import ORM
from models import User, Blog, Comment

def test():
    yield from ORM.create_pool(user='blogadmin', password='jyh001', database='blog_app')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass
