#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
=================================================
redis.StrictRedis Class Library
-------------------------------------------------
作者：[郭磊]
手机：[15210720528]
Email：[174000902@qq.com]
Github：https://github.com/guolei19850528/guolei_py3_database
=================================================
"""

from typing import Iterable

import redis
from addict import Dict


class Database(object):
    """
    Database Class
    """

    def __init__(
            self,
            connect_args: Iterable = (),
            connect_kwargs: dict = Dict({}),
    ):
        """
        Database Construct function
        :param connect_args: redis.StrictRedis connect_args
        :param connect_kwargs: redis.StrictRedis connect_kwargs
        """
        self._connect_args = connect_args
        self._connect_kwargs = connect_kwargs
        self._connect: redis.StrictRedis = None

    @property
    def connect_args(self) -> Iterable:
        """
        redis.StrictRedis connect_args
        :return:
        """
        return self._connect_args

    @connect_args.setter
    def connect_args(self, value: Iterable):
        """
        redis.StrictRedis connect_args
        :param value:
        :return:
        """
        self._connect_args = value

    @property
    def connect_kwargs(self) -> dict:
        """
        redis.StrictRedis connect_kwargs
        :return:
        """
        return self._connect_kwargs

    @connect_kwargs.setter
    def connect_kwargs(self, value: dict):
        """
        redis.StrictRedis connect_kwargs
        :param value:
        :return:
        """
        self._connect_kwargs = value

    @property
    def connect(self) -> redis.StrictRedis:
        """
        redis.StrictRedis connect
        :return:
        """
        return self._connect

    def open_connect(self) -> bool:
        """
        open redis.StrictRedis connect
        :return:
        """
        self.connect_kwargs = Dict(self.connect_kwargs)
        self._connect = redis.StrictRedis(*self.connect_args, **self.connect_kwargs)
        return True

    def close_connect(self) -> bool:
        """
        close redis.StrictRedis  connect
        :return:
        """
        if isinstance(self.connect, redis.StrictRedis):
            self.connect.close()
            return True
        return False
