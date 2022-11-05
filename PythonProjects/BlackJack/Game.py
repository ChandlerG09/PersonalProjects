from Card import Card
import random

EXIT = 1

deck = []
playerHand = []
dealerHand = []

def createDecks(numDecks):
    i = 0

    for k in range(numDecks):
        for i in range(4):
            for j in range(1, 15):
                if j <= 10 and j != 1:
                    val = j
                    cardval = str(val)
                else:
                    val = 10
                    cardval = str(val)
                if j == 1:
                    cardval = 'Ace'
                    val = 11

                if i == 0:
                    myCard = Card(val, cardval, 'Spades')
                if i == 1:
                    myCard = Card(val, cardval, 'Hearts')
                if i == 2:
                    myCard = Card(val, cardval, 'Clubs')
                if i == 3:
                    myCard = Card(val, cardval, 'Diamonds')

                deck.append(myCard)

def printDeck():
    for card in deck:
        print(card.strNum + ' of ' + card.suit)

def shuffleDeck():
    random.shuffle(deck)

def drawFirstCards():
    for i in range(2):
        playerHand.append(deck.pop(0))
        dealerHand.append(deck.pop(0))

def drawCard(tempDeck):
    tempDeck.append(deck.pop(0))
    return tempDeck

def printCard(card):
    print(str(card.value))

def findChoices(val1, val2):
    choices = ['Hit', 'Stay', 'Double']
    if val1 == val2:
        choices.append('Split')
    pass

def handleChoice(resp):
    if resp == 'EXIT':
        print('Exiting Game...')
        return EXIT
    
    if resp not in findChoices(playerHand[0].strNum, playerHand[1].strNum):
        print('Sorry, you cannot do that action right now')
    else:
        pass
    
def playGame():
    
    flag = True

    while flag:
        print('Welcome to command line BlackJack!')
        print('Type EXIT at any point to quit the game')
        numDecks = input('How many decks of cards would you like to play with? ')
        if numDecks == 'EXIT':
            flag = False
            continue
        
        print('Creating ' + str(numDecks) + ' deck(s)')
        createDecks(int(numDecks))
        print('Shuffling the Deck(s)')
        shuffleDeck()

        threshold = 0.75 * len(deck)

        #Remove the top card
        deck.pop(0)

        #Go through 75% of the shoe to simulate actual play
        while(len(deck) >= threshold):
            
            drawFirstCards()
            print('Your cards are: ')
            for card in playerHand:
                printCard(card)

            print('Dealer is showing ' + str(dealerHand[0].strNum))

            
            resp = input('What would you like to do? ')
            
            
        

def main():
    playGame()

if __name__ == "__main__":
    main()