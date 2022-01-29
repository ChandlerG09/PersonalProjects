public class main {
    public static void main(String[] argc){
        Game g1 = new Game();
        g1.createDeck();
        Card[] deck = g1.getDeck();
        g1.shuffleDeck(deck);

        for(int i = 0; i<53; i++){
            g1.printCard(deck[i]);
            System.out.println();
        }

    }
}
