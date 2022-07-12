#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
@Author :shouke
'''

from django.conf import settings

DATABASE_MAPPING = settings.APP_DATABASE_MAPPING

DATABASES_NOT_ALLOW_MIGRATE = settings.APPS_NOT_ALLOW_MIGRATE


class DatabaseRouters(object):
    def db_for_read(self, model, **hints):
        """"指定mode进行读取操作时应使用的数据库, 如果返回None则表示使用默认数据库"""

        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None


    def db_for_write(self, model, **hints):
        """指定mode进行写入操作时应使用的数据库, 如果返回None则表示使用默认数据库"""

        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None


    def allow_relation(self, obj1, obj2, **hints):
        """控制是否允许obj1和obj2建立关联关系,供外键和多对多操作使用，如果返回True则表示允许，如果返回False则阻止建立关联关系,如果返回None则表示仅允许在相同数据库内的对象建立关联关系(备注：笔者亲测，执行save()保存包含关联外键对象，或者通过某个对象获取关联外键对象，该函数都不会被执行     
        """

        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
         return None


    def allow_migrate(self, db, app_label, model=None, **hints):
        """指定是否允许在别名为db的数据库上运行迁移操作。如果允许运行，则返回True；否则返回False、None"""

        if app_labelin DATABASES_NOT_ALLOW_MIGRATE:
            return False
        else:
            return True