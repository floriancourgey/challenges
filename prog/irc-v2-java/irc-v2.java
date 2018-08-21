import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import org.jibble.pircbot.PircBot;

public class epKickMe {
	
	public BigInteger answer;
	
	
	public epKickMe() throws Exception{
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
		
		String channel = "";
		boolean hasJoined = false;
	    
	    public MyBot() {
	        this.setName("MyBot13456");
	    }
	    
	    @Override
	    protected void onJoin(String channel, String sender, String login, String hostname){
	    	super.onJoin(channel, sender, login, hostname);
	    	if(!hasJoined){
		    	hasJoined = true;
		        sendMessage("Daneel", ".challenge_kickme start");
	    	} else {
	    		
	    	}
	    }
	    @Override
	    protected void onChannelInfo(String channel, int userCount, String topic){
	    	if(!hasJoined){
	    		return;
	    	}
	    	
	    	if(channel.contains("#KM_")){
	    		this.channel = channel;
	    		System.out.println(channel);
	    		joinChannel(channel);
	    	}
	    }
	    
	    @Override
	    protected void onPrivateMessage(String sender, String login, String hostname, String message){
	    	if(message.contains("en cours") || message.contains("passe") || message.contains("texte")){
	    		disconnect();
	    		return;
	    	}
//	    	if(message.contains("hash")){
	    		listChannels();
	    		// résolution de l'épreuve
	    		String sub = message.substring(message.indexOf("du ")+3, message.indexOf("ème"));
	    		BigInteger res = fastFibonacciDoubling(Integer.parseInt(sub));
	    		String rep = res.toString();
	    		
				try {
					MessageDigest md = MessageDigest.getInstance("MD5");
			        md.update(rep.getBytes());
			        byte byteData[] = md.digest();
			        StringBuffer sb = new StringBuffer();
			        for (int i = 0; i < byteData.length; i++) {
			        	sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16).substring(1));
			        }
		    		sendMessage("Daneel", ".challenge_kickme "+sb.toString());
		    		System.out.println(sub+"\n"+res+"\n"+sb.toString());
				} catch (NoSuchAlgorithmException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	    		
	    		
//	    	}
	    }
	    
	    protected void onOp(String channel,
                String sourceNick,
                String sourceLogin,
                String sourceHostname,
                String recipient){
	    	System.out.println("LOURD");
	    	kick(this.channel,"Daneel");
	    }
	    
	    /* 
		 * Fast doubling method. Faster than the matrix method.
		 * F(2n) = F(n) * (2*F(n+1) - F(n)).
		 * F(2n+1) = F(n+1)^2 + F(n)^2.
		 * This implementation is the non-recursive version. See the web page and
		 * the other programming language implementations for the recursive version.
		 */
		private BigInteger fastFibonacciDoubling(int n) {
			BigInteger a = BigInteger.ZERO;
			BigInteger b = BigInteger.ONE;
			int m = 0;
			for (int i = 31 - Integer.numberOfLeadingZeros(n); i >= 0; i--) {
				// Loop invariant: a = F(m), b = F(m+1)
				assert a.equals(slowFibonacci(m));
				assert b.equals(slowFibonacci(m+1));
				
				// Double it
				BigInteger d = multiply(a, b.shiftLeft(1).subtract(a));
				BigInteger e = multiply(a, a).add(multiply(b, b));
				a = d;
				b = e;
				m *= 2;
				assert a.equals(slowFibonacci(m));
				assert b.equals(slowFibonacci(m+1));
				
				// Advance by one conditionally
				if (((n >>> i) & 1) != 0) {
					BigInteger c = a.add(b);
					a = b;
					b = c;
					m++;
					assert a.equals(slowFibonacci(m));
					assert b.equals(slowFibonacci(m+1));
				}
			}
			return a;
		}
		
		// Multiplies two BigIntegers. This function makes it easy to swap in a faster algorithm like Karatsuba multiplication.
		private BigInteger multiply(BigInteger x, BigInteger y) {
			return x.multiply(y);
		}
		
		/* 
		 * Simple slow method, using dynamic programming.
		 * F(n+2) = F(n+1) + F(n).
		 */
		private BigInteger slowFibonacci(int n) {
			BigInteger a = BigInteger.ZERO;
			BigInteger b = BigInteger.ONE;
			for (int i = 0; i < n; i++) {
				BigInteger c = a.add(b);
				a = b;
				b = c;
			}
			return a;
		}
	    
	}
	
}


