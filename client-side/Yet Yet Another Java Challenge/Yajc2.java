import java.awt.event.ActionEvent;
import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class Yajc2 {
  private Plouf plouf;
  private PloufCipher ploufCipher;
  
  public Yajc2(){
    this.plouf = null;
    this.ploufCipher = null;
    
//    System.out.println(new Plouf(true));
//    System.out.println(new Plouf(false));
    /*
    POSGHMRROQZICZZKFUAXLPEFCORHHZSOGCW
    */
    try{
		  String mdp = "lebonheurestunexercicesolitaire";
		  FileInputStream fin = new FileInputStream("plouf");
		  ObjectInputStream ois = new ObjectInputStream(fin);
		  this.plouf = (Plouf) ois.readObject();
		  ois.close();
		  System.out.println(this.plouf);
		  this.ploufCipher = new PloufCipher(this.plouf);
		  System.out.println("mdp ("+mdp+")");
		  System.out.println("mdp encrypté("+ploufCipher.encrypt(mdp)+")");
		  System.out.println("mdp cherché (POSGHMRROQZICZZKFUAXLPEFCORHHZSOGCW)");
		  System.out.println("mdp décrypté("+mdp);
//		  System.out.println("mdp decrypt�("+ploufCipher.decrypt(mdp)+")");
//		  if (this.ploufCipher.check(mdp) == 1) {
//		      System.out.println("Bravo");
//		  } else {
//			  System.out.println("Echec");
//		  }
	  } catch (Exception e){
		  e.printStackTrace();
	  }
  }
  
  public void actionPerformed(ActionEvent paramActionEvent){
	  
//    String str1 = this.PasswordField.getText();
//    String str2 = getCodeBase().toString();
//    str2 = str2 + "plouf";
//    try
//    {
//      URL localURL = new URL(str2);
//      this.plouf = ((Plouf)loadPlouf(localURL));
//      this.ploufCipher = new PloufCipher(this.plouf);
//    }
//    catch (Exception localException)
//    {
//      localException.printStackTrace();
//    }
//    if (this.ploufCipher.check(str1) == 1) {
//      this.resultLabel.setText("Bravo, vous pouvez valider cette epreuve avec le mot de passe !");
//    } else {
//      this.resultLabel.setText("Eh non...");
//    }
  }
  
  public Object loadPlouf(URL paramURL)
  {
    Object localObject = null;
    try
    {
      HttpURLConnection localHttpURLConnection = (HttpURLConnection)paramURL.openConnection();
      ObjectInputStream localObjectInputStream = new ObjectInputStream(localHttpURLConnection.getInputStream());
      localObject = localObjectInputStream.readObject();
      localObjectInputStream.close();
      localHttpURLConnection.disconnect();
    }
    catch (Exception localException)
    {
      localException.printStackTrace();
    }
    return localObject;
  }
}
