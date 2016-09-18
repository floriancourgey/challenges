package epYetAnotherJavaChallenge;

import java.io.Serializable;

public class Credentials implements Serializable{

	private static final long serialVersionUID = 8034176813483358648L;
	private String login = "";
	private String password = "";
  
	public Credentials(String paramString1, String paramString2)
	  {
	    this.login = paramString1;
	    this.password = paramString2;
	  }
	  
	  public String getLogin()
	  {
	    return this.login;
	  }
	  
	  public void setLogin(String paramString)
	  {
	    this.login = paramString;
	  }
	  
	  public String getPassword()
	  {
	    return this.password;
	  }
	  
	  public void setPassword(String paramString)
	  {
	    this.password = paramString;
	  }
	  
	  public int checkPassword(String paramString)
	  {
	    if (paramString.compareTo(this.password) == 0) {
	      return 1;
	    }
	    return 0;
	  }
}
