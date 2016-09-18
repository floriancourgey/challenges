import java.io.Serializable;

public final class PloufCipher implements Serializable, Cloneable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	protected Plouf keyPlouf;

	public PloufCipher(Plouf paramPlouf) {
//		if (paramPlouf != null) {
			this.keyPlouf = ((Plouf) paramPlouf.clone());
//		} else {
//			this.keyPlouf = new Plouf(true);
//		}
	}

//	public Object clone() {
//		return new PloufCipher(this.keyPlouf);
//	}

	public Plouf getPlouf() {
		return (Plouf) this.keyPlouf.clone();
	}

	protected static int getCardValue(byte paramByte) {
		if (Plouf.isJoker(paramByte)) {
			return 53;
		}
		if (Plouf.isClub(paramByte)) {
			return Plouf.getFaceValue(paramByte);
		}
		if (Plouf.isDiamond(paramByte)) {
			return 13 + Plouf.getFaceValue(paramByte);
		}
		if (Plouf.isHeart(paramByte)) {
			return 26 + Plouf.getFaceValue(paramByte);
		}
		if (Plouf.isSpade(paramByte)) {
			return 39 + Plouf.getFaceValue(paramByte);
		}
		return 0;
	}

	protected static int getCharValue(char paramChar) {
		if ((paramChar >= 'A') && (paramChar <= 'Z')) {
			return paramChar - 'A' + 1;
		}
		if ((paramChar >= 'a') && (paramChar <= 'z')) {
			return paramChar - 'a' + 1;
		}
		return 0;
	}

	protected static char getValueChar(int paramInt) {
		if ((paramInt >= 1) && (paramInt <= 26)) {
			return (char) (paramInt - 1 + 65);
		}
		return '*';
	}

	protected int nextKeyStream() {
		byte b1 = -98;
		byte b2 = -97;
		System.out.println("avant"+this.keyPlouf);
		this.keyPlouf.moveDown(this.keyPlouf.findTop(b1), 1); // on fait descendre de 1 le -98
		System.out.println("avan2"+this.keyPlouf);
		this.keyPlouf.moveDown(this.keyPlouf.findTop(b2), 2); // on fait descendre de 2 le -97
		System.out.println("apres"+this.keyPlouf);
		int i = this.keyPlouf.findBottom(b1);
		System.out.println("findBottom -98 "+i);
		int j = this.keyPlouf.findBottom(b2);
		System.out.println("findBottom -97 "+j);
		this.keyPlouf.tripleCut(Math.min(i, j), Math.max(i, j) + 1);

		byte b3 = this.keyPlouf.peekBottom(0);
		this.keyPlouf.tripleCut(1, this.keyPlouf.count() - getCardValue(b3));
		this.keyPlouf.cutTop(1);
		byte b4 = this.keyPlouf.peekTop(getCardValue(this.keyPlouf.peekTop(0)));
		int k = getCardValue(b4);
		if (k == 53) {
			return nextKeyStream();
		}
		if (k > 26) {
			k -= 26;
		}
		return k;
	}

	public String encrypt(String paramString) {
		return encrypt(paramString, true);
	}

	public String encrypt(String paramString, boolean paramBoolean) {
		StringBuffer localStringBuffer = new StringBuffer();
		// pour chaque lettre du mdp
		for (int i = 0; i < paramString.length(); i++) {
			System.out.println("i("+i+")");
			int j = getCharValue(paramString.charAt(i)); // j sa pst dans l'alphabet, insensible casse
			System.out.println("\tj"+j);
			if (j > 0) {
				int nextKeyStream = nextKeyStream();
				j += nextKeyStream;
				System.out.println("\t nextKeyStream"+nextKeyStream);
				if (j > 26) {
					j -= 26;
				}
				localStringBuffer.append(getValueChar(j));
				System.out.println("\tAjout de la lettre"+getValueChar(j));
			}
		}
		// si la longueur du mdp n'est pas un multiple de 5
		// on ajoute des X jusqu'à ce que cette longueur soit un multiple
		if (paramBoolean) {
			while (localStringBuffer.length() % 5 != 0) {
				localStringBuffer.append(encrypt("X", false));
			}
		}
		return localStringBuffer.toString();
	}

	public String decrypt(String s) {
		StringBuffer localStringBuffer = new StringBuffer();
		for (int i = 0; i < s.length(); i++) {
			int j = getCharValue(s.charAt(i));
			if (j > 0) {
				j -= nextKeyStream();
				if (j > 26) {
					j += 26;
				}
				localStringBuffer.append(getValueChar(j));
			}
		}
		// if (paramBoolean) {
		while (localStringBuffer.length() % 5 != 0) {
			localStringBuffer.append(encrypt("X", false));
			// }
		}
		return localStringBuffer.toString();
	}

	public int check(String paramString) {
		return encrypt(paramString).compareTo(
				"POSGHMRROQZICZZKFUAXLPEFCORHHZSOGCW") != 0 ? 0 : 1;
	}
}
