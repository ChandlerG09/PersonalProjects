from Card import Card
import random
import time
import os

EXIT = -1
PLAYERWIN = 1
DEALERWIN = 2
PUSH = 3

deck = []
playerHand = []
dealerHand = []

def createDecks(numDecks):
    i = 0

    for k in range(numDecks):
        for i in range(4):
            for j in range(1, 14):
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
    discardDecks()
    for i in range(2):
        playerHand.append(deck.pop(0))
        dealerHand.append(deck.pop(0))

    if checkSum(dealerHand) == 21:
        os.system('clear')
        return DEALERWIN

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
    print('Dealer is showing\n' + dealerHand[0].strNum)
    return input('\nWhat would you like to do? ')

def discardDecks():
    playerHand.clear()
    dealerHand.clear()

def hit():
    drawCard(playerHand)
    print('Your cards are:')
    printHand(playerHand)
    print('')
    if checkSum(playerHand) > 21:
        print('\nPlayer Busts, Dealer Wins\n')
        return DEALERWIN
    else:
        handleChoice()

def softOrHard(tempDeck):
    pass

def printBoth():
    os.system('clear')
    print('Your sum is: ' + str(checkSum(playerHand)) + ' with cards:')
    printHand(playerHand)
    print('\nDealer has sum of ' + str(checkSum(dealerHand)) + ' with cards:')
    printHand(dealerHand)
    
def printHand(tempDeck):
    cards = []
    for card in tempDeck:
        cards.append(card.strNum)
    
    print(*cards)
    return cards

def determineResult(playerSum, dealerSum):

    playerDif = 21 - playerSum
    dealerDif = 21 - dealerSum

    printBoth()

    if playerDif < dealerDif or dealerSum > 21:
        print('\nYou won!\n')
        return PLAYERWIN
    if playerDif > dealerDif and dealerSum < 21:
        print('\nDealer won.\n')
        return DEALERWIN
    if playerDif == dealerDif:
        print('\nYou pushed\n')
        return PUSH

def findAces(tempDeck):
    numAces = 0
    for card in tempDeck:
        if card.strNum == 'Ace':
            numAces += 1
    return numAces

def findAceIndex(tempDeck):
    for i in range(len(tempDeck)):
        if tempDeck[i].strNum == 'Ace':
            return i

def removeAceAndSum(tempDeck):
    tmp = tempDeck.copy()
    tmp.pop(findAceIndex(dealerHand))

    return checkSum(tmp)

def dealerDraw():
    while checkSum(dealerHand) <= 17: #Hit until dealer has at least 17
        if findAces(dealerHand) == 1 and removeAceAndSum(dealerHand) == 6: #soft 17, hit again
            print('Soft 17 found')
            drawCard(dealerHand)
            time.sleep(1)
            printBoth()
            continue
        if checkSum(dealerHand) < 17:
            drawCard(dealerHand)
            printBoth()
            time.sleep(1)
        else:
            break
    determineResult(checkSum(playerHand), checkSum(dealerHand))

def split():
    pass

def double():
    drawCard(playerHand)
    print('Your cards are:')
    printHand(playerHand)
    print('')
    if checkSum(playerHand) > 21:
        print('\nPlayer Busts, Dealer Wins\n')
        return DEALERWIN

def handleChoice():
    resp = askPlayer().lower()
    os.system('clear')
    if resp.upper() == 'EXIT':
        print('Exiting Game...')
        return EXIT
    
    if resp not in findChoices(playerHand[0].strNum, playerHand[1].strNum):
        print('Sorry, you cannot do that action right now')
        handleChoice()
    else:
        if resp == 'hit':
            hit()
        if resp == 'stay':
            dealerDraw()
        if resp == "split":
            split()
        if resp == "double":
            double()

    return 0
            
    
def playGame():
    
    flag = True

    while flag:
        os.system('clear')
        print('Welcome to command line BlackJack!\n')
        print('Type EXIT at any point to quit the game\n\n')
        numDecks = input('How many decks of cards would you like to play with? ')
        if numDecks.upper() == 'EXIT':
            os.system('clear')
            flag = False
            continue
        os.system('clear')
        print('\nCreating ' + str(numDecks) + ' deck(s)')
        createDecks(int(numDecks))
        print('Shuffling the Deck(s)...\n')
        shuffleDeck()
        print('Shuffled')
        time.sleep(1)
        os.system('clear')
        

        threshold = 0.25 * len(deck)

        #Remove the top card
        deck.pop(0)

        #Go through 75% of the shoe to simulate actual play
        while(len(deck) >= threshold):
            
            if drawFirstCards() != 'BJ':
                print('Your cards are:')
                printHand(playerHand)
                print('')

                n = handleChoice()
                if n == EXIT:
                    os.system('clear')
                    flag = False
                    break

                resp = input('Press enter to start next hand or EXIT to quit: ')
                if resp.upper() == 'EXIT':
                    os.system('clear')
                    flag = False
                    break
                os.system('clear')
            else:
                print('Your cards are:')
                printHand(playerHand)
                print('')
                print("Dealers cards are")
                printHand(dealerHand)
                print('\nDealer has BlackJack')
                #discardDecks()
                resp = input('Press enter to start next hand or EXIT to quit: ')
                if resp.upper() == 'EXIT':
                    os.system('clear')
                    flag = False
                    break
                os.system('clear')
            
            
        

def main():
    playGame()

if __name__ == "__main__":
    main()