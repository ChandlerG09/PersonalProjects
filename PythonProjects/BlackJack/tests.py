import unittest
from Card import Card
import Game

cards = []
cards.append("")
cards.append(Card(11, 'Ace', "Spade"))
for i in range(2, 11):
    cards.append(Card(i, str(i), "Spade"))
    playerDeck = []
    dealerDeck = []

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

    def testDealerBlackJack(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.dealerHand.append(cards[1]) #Ace
        Game.dealerHand.append(cards[10]) #10
        Game.playerHand.append(cards[10]) #10
        Game.playerHand.append(cards[10]) #10

        self.assertEqual(Game.checkSum(Game.dealerHand), 21)

    def testSoft17(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.dealerHand.append(cards[1])
        Game.dealerHand.append(cards[6]) #Ace and 6
        self.assertEqual(Game.checkSum(Game.dealerHand), 17) #Soft 17
        Game.dealerHand.append(cards[9]) #Draw a 9
        self.assertEqual(Game.checkSum(Game.dealerHand), 16) #Hard 16

    def testPlayerWins(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.dealerHand.append(cards[9])
        Game.dealerHand.append(cards[10])
        Game.playerHand.append(cards[10])
        Game.playerHand.append(cards[10])
        self.assertEqual(Game.determineResult(Game.checkSum(Game.playerHand), Game.checkSum(Game.dealerHand)), 1)

    def testDealerWin(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.dealerHand.append(cards[10])
        Game.dealerHand.append(cards[10])
        Game.playerHand.append(cards[8])
        Game.playerHand.append(cards[10])
        self.assertEqual(Game.determineResult(Game.checkSum(Game.playerHand), Game.checkSum(Game.dealerHand)), Game.DEALERWIN)

    def testPush(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.dealerHand.append(cards[9])
        Game.dealerHand.append(cards[8])
        Game.playerHand.append(cards[7])
        Game.playerHand.append(cards[10])
        self.assertEqual(Game.determineResult(Game.checkSum(Game.playerHand), Game.checkSum(Game.dealerHand)), Game.PUSH)

    def testPlayerBust(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.deck.append(cards[5])
        Game.dealerHand.append(cards[5])
        Game.dealerHand.append(cards[5])
        Game.playerHand.append(cards[10])
        Game.playerHand.append(cards[10])
        self.assertEqual(Game.hit(), Game.DEALERWIN)

    def testDealerHitsSoft17Gets17(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.deck.append(cards[10]) #10
        Game.deck.append(cards[10]) #10

        Game.dealerHand.append(cards[1]) #Ace
        Game.dealerHand.append(cards[6]) #6

        Game.playerHand.append(cards[9]) #9
        Game.playerHand.append(cards[8]) #8

        Game.dealerDraw() #Dealer should draw the Ace

        self.assertEqual(Game.checkSum(Game.dealerHand), 17) #Sum should be 17 after hitting soft 17

    def testDealerHitsSoft17GetsAce(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.deck.append(cards[1]) #10
        Game.deck.append(cards[10]) #10

        Game.dealerHand.append(cards[1]) #Ace
        Game.dealerHand.append(cards[6]) #6

        Game.playerHand.append(cards[9]) #9
        Game.playerHand.append(cards[8]) #8

        Game.dealerDraw() #Dealer should draw the Ace

        self.assertEqual(Game.checkSum(Game.dealerHand), 18) #Sum should be 17 after hitting soft 17

    def testMultipleAces(self):
        Game.discardDecks()
        Game.deck.clear()
        Game.deck.append(cards[1]) #Ace

        Game.dealerHand.append(cards[2]) #2
        Game.dealerHand.append(cards[6]) #6

        Game.playerHand.append(cards[1]) #Ace
        Game.playerHand.append(cards[5]) #5

        self.assertEqual(Game.checkSum(Game.playerHand), 16)

        Game.playerHand.append(cards[1]) #Ace

        self.assertEqual(Game.checkSum(Game.playerHand), 17)

        Game.playerHand.append(cards[1]) #Ace

        self.assertEqual(Game.checkSum(Game.playerHand), 18)


if __name__ == '__main__':
    unittest.main()