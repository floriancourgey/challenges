import org.jibble.pircbot.PircBot;

public class epIrcCaesar {
	public epIrcCaesar() throws Exception{
		// Now start our bot up.
        MyBot bot = new MyBot();
        
        // Enable debugging output.
        bot.setVerbose(true);
        
        // Connect to the IRC server.
        bot.connect("irc.worldnet.net");

        // Join the #pircbot channel.
        bot.joinChannel("#nc-irc-challs");
	}
	
	public class MyBot extends PircBot {
	    
	    public MyBot() {
	        this.setName("MyBot");
	    }
	    
	    @Override
	    protected void onConnect(){
	    	super.onConnect();
	        sendMessage("Daneel", ".challenge_caesar start");
	    }
	    
	    @Override
	    protected void onPrivateMessage(String sender, String login, String hostname, String message){
	    	if(message.contains("texte") || message.contains("passe")){
	    		disconnect();
	    		return;
	    	}
	    	
	    	String retour = "";
	    	for(int i=0 ; i<message.length() ; i++){
	    		int ascii = (int)(message.charAt(i));
	    		int asciiDecode = ascii - 3;
	    		if(asciiDecode < 97){
	    			asciiDecode += 26;
	    		}
	    		char reponse = (char)asciiDecode;
	    		retour += reponse;
	    		System.out.println("lettre("+message.charAt(i)+")ascii("+ascii+")asciiDecode("+asciiDecode+")lettreDecodee("+reponse+")");
	    	}
	    	System.out.println("avant("+message+")apres("+retour+")");
	    	sendMessage("Daneel", ".challenge_caesar "+retour);
	    }
	    
	}
}


