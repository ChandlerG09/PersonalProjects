import unittest
from Card import Card
import Game



class testCode(unittest.TestCase):
    def testDeckCreation(self):
        Game.createDecks(1)
        deck = Game.deck
        self.assertEqual(len(deck), 52)

    def testPullTopCard(self):
        pass


if __name__ == '__main__':
    unittest.main()