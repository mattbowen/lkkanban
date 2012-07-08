import unittest
from lkkanban.httpapi import HttpApi


class TestHttpApi(unittest.TestCase):
    def setUp(self):
        self.local = HttpApi('foo', 'username', 'passwd', 'fixtures')
        self.remote = HttpApi('foo', 'username', 'passwd')

    def test_get_endpoint_all_boards(self):
        expected_endpoint = 'http://foo.leankitkanban.com/Kanban/Api/Boards'
        actual_endpoint = self.remote._get_endpoint('Boards')
        self.assertEqual(expected_endpoint, actual_endpoint)

    def test_get_endpoint_addcard(self):
        expected_endpoint = \
            "http://foo.leankitkanban.com/Kanban/Api/Board/100/AddCards"
        actual_endpoint = self.remote._get_endpoint('AddCards', 100)
        self.assertEqual(expected_endpoint, actual_endpoint)

    def test_get_endpoint_specific_board(self):
        expected_endpoint = \
            "http://foo.leankitkanban.com/Kanban/Api/Boards/100"
        actual_endpoint = self.remote._get_endpoint('Boards', 100)
        self.assertEqual(expected_endpoint, actual_endpoint)
