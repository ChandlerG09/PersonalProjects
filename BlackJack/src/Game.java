import java.util.Random;

public class Game {
    private final Card[] deck = new Card[52];

    public Card[] getDeck(){
        return deck;
    }

    /**
     * This method is used to create a deck of cards (unshuffled)
     */
    public void createDeck(){
        Card card = new Card();

        //Loop create all 52 cards
        for (int i = 0; i <=51 ; i++) {

            //Assign Card ID
            card.setCardId(i);
            if (i <= 3) {
                switch (i) {
                    case 0 -> card.setSuit("Spade");
                    case 1 -> card.setSuit("Club");
                    case 2 -> card.setSuit("Heart");
                    case 3 -> card.setSuit("Diamond");
                }
            }

            //Loop to assign values
            for(int t =1; t<=14; t++) {
                card.setCardId(i);
                if (t > 10)
                    card.setValue(10);
                card.setValue(t);
                deck[i] = card;
                i++;
            }
        }
    }

    /**
     * Shuffles the deck of cards
     * @param deck the deck of cards to be shuffled
     */
    public void shuffleDeck(Card[] deck){
        Random num = new Random();
        Card[] shuffledDeck = new Card[52];
        int pos;
        boolean inserted;

        //Place the cards in random order
        for(int i = 0; i< 52; i++){
            inserted = false;

            //Keep trying to insert until successful
            while(!inserted) {
                pos = num.nextInt(52);

                if (shuffledDeck[pos] != null) {
                    shuffledDeck[pos] = deck[i];
                    inserted = true;
                }
            }
        }
    }

    public void printCard(Card card){
        System.out.print("Card: " + card.getValue() + " of " + card.getSuit());
    }


}
