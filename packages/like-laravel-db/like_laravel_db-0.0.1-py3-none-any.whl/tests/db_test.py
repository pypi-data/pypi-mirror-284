import sys

sys.path.append("../")
import unittest
import like_laravel_db


class DbTestCase(unittest.TestCase):
    def test_first(self):
        like_laravel_db.db()
