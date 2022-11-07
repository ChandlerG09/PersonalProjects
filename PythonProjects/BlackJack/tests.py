import unittest
from Card import Card
import Game



class testCode(unittest.TestCase):
    def testDeckCreation(self):
        Game.createDecks(1)
        deck = Game.deck
        self.assertEqual(len(deck), 52)

    def testDrawCard(self):
        Game.createDecks(1)
        deck = Game.deck
        expected = deck[0]
        newDeck = Game.drawCard(deck)
        
        self.assertEqual(newDeck[-1], expected)


if __name__ == '__main__':
    unittest.main()