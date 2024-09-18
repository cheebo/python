from unittest import TestCase
from ticket import is_lucky_ticket

class Test(TestCase):
    def test_ticket_lucky(self):
        self.assertTrue(is_lucky_ticket(123123))
        self.assertTrue(is_lucky_ticket(0))
        self.assertTrue(is_lucky_ticket(111111))

    def test_ticket_un_lucky(self):
        self.assertFalse(is_lucky_ticket(121212))
        self.assertFalse(is_lucky_ticket(111000))
