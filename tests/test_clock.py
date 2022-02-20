import sys
import datetime
import unittest

from clock import Clock


class TestClock(unittest.TestCase):

    def test_get_instance_now(self):
        """
        Testa se a hora retornada pelo método get_now() é uma instância de datetime
        """
        now = Clock().get_now()
        now_assert = isinstance(now, datetime.datetime)
        self.assertTrue(now_assert)

    def teste_get_instance_today(self):
        """
        Testa se a data retornada pelo método get_today() é uma instância de datetime
        """
        today = Clock().get_today()
        today_assert = isinstance(today, datetime.datetime)
        self.assertTrue(today_assert)
