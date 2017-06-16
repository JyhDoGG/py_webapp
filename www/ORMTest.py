#!/usr/bin/env python3
#coding=utf-8

from ORM import Model, StringField, IntegerField

class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()

user=User(id=123,name='Jyh')

