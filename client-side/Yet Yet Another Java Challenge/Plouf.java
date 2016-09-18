import java.io.Serializable;
import java.util.Random;

public class Plouf implements Serializable, Cloneable {
	private static final long serialVersionUID = 2054058973818839106L;
	
	protected static final byte MASK_SUIT = -16;
	protected static final byte MASK_VALUE = 15;
	protected static final byte MASK_BLACK = 32;
	protected static final byte MASK_RED = 64;
	protected static final byte MASK_JOKER = -128;
	public static final byte CLUBS = 32;
	public static final byte DIAMONDS = 64;
	public static final byte HEARTS = 80;
	public static final byte SPADES = 48;
	public static final byte JOKER = -112;
	public static final byte ACE = 1;
	public static final byte DEUCE = 2;
	public static final byte THREE = 3;
	public static final byte FOUR = 4;
	public static final byte FIVE = 5;
	public static final byte SIX = 6;
	public static final byte SEVEN = 7;
	public static final byte EIGHT = 8;
	public static final byte NINE = 9;
	public static final byte TEN = 10;
	public static final byte JACK = 11;
	public static final byte QUEEN = 12;
	public static final byte KING = 13;
	public static final byte JOKER_A = 14;
	public static final byte JOKER_B = 15;
	protected byte[] cards;
	protected int marker;
/*
	public Plouf() {
		this(true);
	}
*/
	/**
	 * 
	 * @param joker, présence ou non de joker
	 */
/*
	public Plouf(boolean joker) {
		this.marker = (joker ? 54 : 52);
		this.cards = new byte[54];
		for (int i = 0; i < 4; i++) {
			int j = -112;
			switch (i) {
			case 0:
				j = CLUBS;
				break;
			case 1:
				j = DIAMONDS;
				break;
			case 2:
				j = HEARTS;
				break;
			case 3:
				j = SPADES;
				break;
			}
			for (int k = 0; k < 13; k++) {
				this.cards[(this.marker - 1 - (13 * i + k))] = ((byte) (j | k + 1));
			}
		}
		this.cards[(joker ? 1 : this.marker + 1)] = -98;
		this.cards[(joker ? 0 : this.marker)] = -97;
	}
*/
	public Plouf(byte[] paramArrayOfByte) {
		this.marker = paramArrayOfByte.length;
		this.cards = new byte[this.marker];
		for (int i = 0; i < paramArrayOfByte.length; i++) {
			this.cards[i] = paramArrayOfByte[i];
		}
	}

	protected Plouf(Plouf paramPlouf) {
		this.marker = paramPlouf.marker;
		this.cards = new byte[paramPlouf.cards.length];
		for (int i = 0; i < 54; i++) {
			this.cards[i] = paramPlouf.cards[i];
		}
	}

	public Object clone() {
		return new Plouf(this);
	}

	public void shuffle() {
		shuffle(new Random());
	}

	public void shuffle(Random paramRandom) {
		for (int i = 0; i < this.marker; i++) {
			int j = Math.abs(paramRandom.nextInt() % this.marker);
			int k = this.cards[i];
			this.cards[i] = this.cards[j];
			this.cards[j] = (byte) k;
		}
	}

	public byte deal() {
		return this.marker > 0 ? this.cards[(--this.marker)] : 0;
	}

	public void collect() {
		this.marker = this.cards.length;
	}

	protected void basicCut(int paramInt1, int paramInt2) {
		if ((paramInt1 > 0) && (paramInt1 < paramInt2)) {
			byte[] arrayOfByte = new byte[paramInt2];
			int i;
			for (i = 0; i < paramInt1; i++) {
				arrayOfByte[(i + (paramInt2 - paramInt1))] = this.cards[i];
			}
			for (i = paramInt1; i < paramInt2; i++) {
				arrayOfByte[(i - paramInt1)] = this.cards[i];
			}
			for (i = 0; i < paramInt2; i++) {
				this.cards[i] = arrayOfByte[i];
			}
		}
	}

	public void cutTop(int paramInt) {
		basicCut(this.marker - paramInt, this.marker);
	}

	public void cutBottom(int paramInt) {
		basicCut(paramInt, this.marker);
	}

	public void tripleCut(int paramInt1, int paramInt2) {
		if ((0 <= paramInt1) && (paramInt1 <= paramInt2)
				&& (paramInt2 <= this.marker)) {
			basicCut(paramInt1, paramInt2);
			basicCut(paramInt2, this.marker);
		}
	}

	public void moveDown(int paramInt) {
		moveDown(paramInt, 1);
	}

	public void moveDown(int paramInt1, int paramInt2) {
		int i = this.marker - 1 - paramInt1;
		while (paramInt2 > 0) {
			int j;
			if ((i > 0) && (i < this.marker)) {
				j = this.cards[i];
				this.cards[i] = this.cards[(i - 1)];
				this.cards[(i - 1)] = (byte) j;
				i--;
			} else if (i == 0) {
				for (int k = 0; k < this.marker - 2; k++) {
					j = this.cards[k];
					this.cards[k] = this.cards[(k + 1)];
					this.cards[(k + 1)] = (byte) j;
					i++;
				}
			}
			paramInt2--;
		}
	}

	public int count() {
		return this.marker;
	}

	public byte peekTop(int paramInt) {
		if ((paramInt >= 0) && (paramInt < this.marker)) {
			return this.cards[(this.marker - 1 - paramInt)];
		}
		return 0;
	}

	public byte peekBottom(int paramInt) {
		if ((paramInt >= 0) && (paramInt < this.marker)) {
			return this.cards[paramInt];
		}
		return 0;
	}

	public int findTop(byte paramByte) {
		int i = 0;
		while (i < this.marker) {
			if (this.cards[i] == paramByte) {
				return this.marker - 1 - i;
			}
			i++;
		}
		return -1;
	}

	public int findBottom(byte paramByte) {
		int i = 0;
		while (i < this.marker) {
			if (this.cards[i] == paramByte) {
				return i;
			}
			i++;
		}
		return -1;
	}

	public static boolean isClub(byte paramByte) {
		return (paramByte & 0xFFFFFFF0) == 32;
	}

	public static boolean isDiamond(byte paramByte) {
		return (paramByte & 0xFFFFFFF0) == 64;
	}

	public static boolean isHeart(byte paramByte) {
		return (paramByte & 0xFFFFFFF0) == 80;
	}

	public static boolean isSpade(byte paramByte) {
		return (paramByte & 0xFFFFFFF0) == 48;
	}

	public static boolean isBlack(byte paramByte) {
		return (paramByte & 0x20) != 0;
	}

	public static boolean isRed(byte paramByte) {
		return (paramByte & 0x40) != 0;
	}

	public static boolean isJoker(byte paramByte) {
		return (paramByte & 0xFFFFFF80) != 0;
	}

	public static boolean isJokerA(byte paramByte) {
		return paramByte == -98;
	}

	public static boolean isJokerB(byte paramByte) {
		return paramByte == -97;
	}

	public static boolean isAce(byte paramByte) {
		return (paramByte & 0xF) == 1;
	}

	public static boolean isDuece(byte paramByte) {
		return (paramByte & 0xF) == 2;
	}

	public static boolean isTwo(byte paramByte) {
		return isDuece(paramByte);
	}

	public static boolean isThree(byte paramByte) {
		return (paramByte & 0xF) == 3;
	}

	public static boolean isFour(byte paramByte) {
		return (paramByte & 0xF) == 4;
	}

	public static boolean isFive(byte paramByte) {
		return (paramByte & 0xF) == 5;
	}

	public static boolean isSix(byte paramByte) {
		return (paramByte & 0xF) == 6;
	}

	public static boolean isSeven(byte paramByte) {
		return (paramByte & 0xF) == 7;
	}

	public static boolean isEight(byte paramByte) {
		return (paramByte & 0xF) == 8;
	}

	public static boolean isNine(byte paramByte) {
		return (paramByte & 0xF) == 9;
	}

	public static boolean isTen(byte paramByte) {
		return (paramByte & 0xF) == 10;
	}

	public static boolean isJack(byte paramByte) {
		return (paramByte & 0xF) == 11;
	}

	public static boolean isQueen(byte paramByte) {
		return (paramByte & 0xF) == 12;
	}

	public static boolean isKing(byte paramByte) {
		return (paramByte & 0xF) == 13;
	}

	public static int getFaceValue(byte paramByte) {
		return paramByte & 0xF;
	}
	
	@Override
	public String toString() {
		String retour = "";
		for (int i = 0; i < cards.length; i++) {
			String couleur = "";
			String carte = "";
			byte binaire = cards[i];
			byte minus = 0;
			if(isJokerA(binaire)){
				carte = "JoA";
			} else if(isJokerB(binaire)){
				carte = "JoB";
			} else {
				if(isClub(binaire)){
					couleur = "Tr";
					minus = CLUBS;
				} else if(isDiamond(binaire)){
					couleur = "Ca";
					minus = DIAMONDS;
				} else if(isHeart(binaire)){
					couleur = "Co";
					minus = HEARTS;
				} else if(isSpade(binaire)){
					couleur = "Pi";
					minus = SPADES;
				}
				if(isAce(binaire)){
					carte = "As"+couleur;
				} else if(isJack(binaire)){
					carte = "As"+couleur;
				} else if(isQueen(binaire)){
					carte = "Re"+couleur;
				} else if(isKing(binaire)){
					carte = "Ro"+couleur;
				} else {
					carte = (binaire-minus) + couleur;					
				}
				
			}
			retour += carte+",";
		}
		retour += "marker(" + marker + ")";
		return retour;
	}
}
