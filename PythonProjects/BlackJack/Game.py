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
    print(str(card.strNum))

def findChoices(val1, val2):
    choices = ['hit', 'stay', 'double']
    if val1 == val2:
        choices.append('split')
    return choices

def checkSum(tempDeck):
    sum = 0
    numAces = 0
    for card in tempDeck:
        if card.strNum == 'Ace':
            numAces+= 1
        
        sum += card.value
    
    while numAces != 0 and sum > 21:
        if sum > 21:
            numAces -= 1
            sum -= 10
    
    return sum

def askPlayer():
    return input('\nWhat would you like to do? ')

def hit():
    drawCard(playerHand)
    if checkSum(playerHand) > 21:
        print('\nPlayer Busts, Dealer Wins\n\n')
    else:
        handleChoice()

def dealerDraw():
    while checkSum(dealerHand) < 17: #Hit until dealer has at least 17
        drawCard(dealerHand)
        if checkSum(dealerHand) - 1 > 21: #soft 17, hit again
            drawCard(dealerHand)



def handleChoice():
    resp = askPlayer().lower()

    if resp.upper() == 'EXIT':
        print('Exiting Game...')
        return EXIT
    
    if resp not in findChoices(playerHand[0].strNum, playerHand[1].strNum):
        print('Sorry, you cannot do that action right now')
    else:
        if resp == 'hit':
            hit()
        if resp == 'stay':
            dealerDraw()
            
    
def playGame():
    
    flag = True

    while flag:
        print('\n\nWelcome to command line BlackJack!\n')
        print('Type EXIT at any point to quit the game\n\n')
        numDecks = input('How many decks of cards would you like to play with? ')
        if numDecks.upper() == 'EXIT':
            flag = False
            continue
        
        print('\nCreating ' + str(numDecks) + ' deck(s)\n')
        createDecks(int(numDecks))
        print('Shuffling the Deck(s)')
        shuffleDeck()

        threshold = 0.75 * len(deck)

        #Remove the top card
        deck.pop(0)

        #Go through 75% of the shoe to simulate actual play
        while(len(deck) >= threshold):
            
            drawFirstCards()
            print('\n\nYour cards are: ')
            for card in playerHand:
                printCard(card)

            print('\nDealer is showing ' + str(dealerHand[0].strNum))

            
            
            n = handleChoice()
            if n == EXIT:
                flag = False
                break
            
            
        

def main():
    playGame()

if __name__ == "__main__":
    main()