import unittest
from wit_query_agent import wit_query_agent

class TestWitQueryAgent(unittest.TestCase):

    def test_send(self):
        agent = wit_query_agent()
        agent.send("I have weak stomach")


if __name__ == '__main__':
    unittest.main()