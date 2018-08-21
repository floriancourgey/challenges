import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

import org.jibble.pircbot.PircBot;

public class epAsciiArt {
	public epAsciiArt() throws Exception{
		// Now start our bot up.
        MyBot bot = new MyBot();
        
        // Enable debugging output.
        bot.setVerbose(true);
        
        // Connect to the IRC server.
        bot.connect("irc.worldnet.net");

        // Join the #pircbot channel.
        bot.joinChannel("#acme-irc-challs");
	}
	
	public class MyBot extends PircBot {
	    
	    public MyBot() {
	        this.setName("MyBot");
	    }
	    
	    @Override
	    protected void onConnect(){
	    	super.onConnect();
	        sendMessage("Daneel", ".challenge_asciiart start");
	    }
	    
	    @Override
	    protected void onPrivateMessage(String sender, String login, String hostname, String message){
	    	if(message.contains("texte") || message.contains("passe")){
	    		disconnect();
	    		return;
	    	}
	    	
	    	HashMap<Character, Character[][]> dico = new HashMap<Character, Character[][]>();
			
			BufferedReader reader = null;
			try {
				File file = new File("src/epAsciiArt.txt");
				boolean firstTime = true;
				int indexLigne = 0;
				char lettreEnCours = ' ';
				Character[][] lettre = null;
				Character[] ligne = null;
			    reader = new BufferedReader(new FileReader(file));
			    String text = null;
			    while ((text = reader.readLine()) != null) {
//			    	System.out.println(text);
			    	if(text.length() != 1){
			    		if(ligne == null){
			    			ligne = new Character[text.length()];
			    		}
			    		if(lettre == null){
			    			lettre = new Character[6][ligne.length];
			    		}
			    		for(int i=0 ; i<text.length() ; i++){
				        	ligne[i] = text.charAt(i);
				        }
			    		lettre[indexLigne++] = ligne;
			    		ligne = null;
			    	} else {
			    		if(firstTime){
			    			lettreEnCours = text.charAt(0);
			    			firstTime = false;
			    		} else {
			    			dico.put(lettreEnCours, lettre);
			    			indexLigne = 0;
			    			lettre = null;
			    			ligne = null;
			    			lettreEnCours = text.charAt(0);
			    		}
//			    		System.out.println("Nouvelle lettre "+text);
			    	}
			    }
			    dico.put(lettreEnCours, lettre);
			} catch (FileNotFoundException e) {
			    e.printStackTrace();
			} catch (IOException e) {
			    e.printStackTrace();
			} finally {
			    try {
			        if (reader != null) {
			            reader.close();
			        }
			    } catch (IOException e) {
			    	e.printStackTrace();
			    }
			}
			
			
			
//			Iterator<Entry<Character, Character[][]>> it1 = dico.entrySet().iterator();
//		    while (it1.hasNext()) {
//		        Map.Entry<Character, Character[][]> pairs = (Map.Entry<Character, Character[][]>)it1.next();
//		        System.out.println(pairs.getKey());
//		        Character[][] value = pairs.getValue();
//		        for(int i=0 ; i<6 ; i++){
//					Character[] ligne = value[i];
//					for(int j=0 ; j<ligne.length ; j++){
//						System.out.print(ligne[j]);
//					}
//					System.out.println();
//				}
//		    }
			
			String recu = message;
			recu = recu.replace("0", "");
//			recu = recu.replace("\\", ">");
			double t = (recu.length()/6);
			if (t == (int)t){
				int taille = (int)t;
				System.out.println(recu.length()+" "+taille);
				// création matrice
				System.out.println("Message :");
				char[][] matrice = new char[6][taille];
				for(int i=0 ; i<6 ; i++){
					for(int j=0 ; j<taille ; j++){
						matrice[i][j] = recu.charAt(i*taille + j);
						System.out.print(matrice[i][j]);
					}
					System.out.println();
				}
				// création lettres
				System.out.println("Lettres découpées :");
				int lastIndex = 0;
				int indexLettre = 0;
				ArrayList<Character[][]> l = new ArrayList<>();
				for(int j=0 ; j<taille ; j++){
					boolean flagEspace = true;
					for(int i=0 ; i<6 ; i++){
						char c = matrice[i][j];
						if(c != ' '){
							flagEspace = false;
						}
					}
					if(flagEspace){
						Character[][] tab = new Character[6][j-lastIndex];
						int indexColonne = 0;
						System.out.println("XXX");
						for(int y=0 ; y<6 ; y++){
							for(int z=lastIndex ; z<j ; z++, indexColonne++){
//								System.out.println(y+"-"+indexColonne);
								tab[y][indexColonne] = matrice[y][z];
								System.out.print(matrice[y][z]);
							}
							indexColonne = 0;
							System.out.println();
						}
						lastIndex = j+1;
						l.add(indexLettre, tab);
					} else {
						
					}
				}
				
				
				// pour chaque caractère
				String lettresTrouvees = "";
				for (Character[][] lettre : l) {
					// pour chaque lettre du dico
					Iterator<Entry<Character, Character[][]>> it = dico.entrySet().iterator();
					boolean flag = true;
				    while (it.hasNext()) {
				        Map.Entry<Character, Character[][]> pairs = (Map.Entry<Character, Character[][]>)it.next();
				        Character[][] value = pairs.getValue();
				        flag = true;
				        // pour chaque ligne de la lettre du dico
				        for(int i=0 ; i<6 ; i++){
							Character[] ligne = value[i];
							for(int j=0 ; j<ligne.length ; j++){
								if (Arrays.equals(lettre[i], ligne)){
						        	
						        } else {
						        	flag = false;
						        	break;
						        }
							}
						}
				        if(flag){
				        	lettresTrouvees += pairs.getKey();
							System.out.println("Lettre trouvée : "+pairs.getKey());
							break;
						}
				    }
				    if(!flag){
				    	lettresTrouvees += ".";
				    }
				}
				lettresTrouvees = new StringBuilder(lettresTrouvees).reverse().toString();
				if(!lettresTrouvees.contains(".")){
					System.out.println("toutes les lettre on été trouvées : "+lettresTrouvees);
					sendMessage("Daneel",".challenge_asciiart "+lettresTrouvees);
				} else {
					System.out.println("Message non déchiffré pleinement ("+lettresTrouvees+")");
					disconnect();
				}
			} else {
				System.out.println("Indivisible");
				disconnect();
			}
	    }
	}
}


