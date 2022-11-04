public class Card {
    private int value, cardId;
    private String suit;

    public Card(){
        this.value = 0;
        this.cardId = -1;
        this.suit = "";
    }
    public Card(int value, int cardId, String suit){
        this.value = value;
        this.cardId = cardId;
        this.suit = suit;
    }

    public int getValue() {
        return value;
    }

    public int getCardId() {
        return cardId;
    }

    public String getSuit() {
        return suit;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public void setCardId(int cardId) {
        this.cardId = cardId;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
}
