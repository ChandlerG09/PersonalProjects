from Card import Card
import random

deck = []

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

def playGame():
    flag = True

    while flag:
        print('Welcome to command line BlackJack!')
        print('Type EXIT at any point to quit the game')
        numDecks = input('How many decks of cards would you like to play with?')
        if numDecks == 'EXIT':
            flag = False
            continue
        
        print('Creating ' + str(numDecks) + ' deck(s)')
        createDecks(int(numDecks))
        print('Shuffling the Deck(s)')
        shuffleDeck()

        while(len(deck) != threshold):
            pass
        

def main():
    playGame()

if __name__ == "__main__":
    main()