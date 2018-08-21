package yajc;

import java.applet.Applet;
import java.awt.Button;
import java.awt.Label;
import java.awt.Rectangle;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.ObjectInputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class Yajc extends Applet implements ActionListener{

	/**
	 *
	 */
	private static final long serialVersionUID = 5049590336206846566L;
	private Button SubmitButton;
	private TextField PasswordField;
	private Label PasswordLabel;
	private Label resultLabel;
	private Credentials credentials;

  public void stop() {}

  public Yajc()
  {
	  System.out.println("Applet lancée");
    this.SubmitButton = null;
    this.PasswordField = null;
    this.PasswordLabel = null;
    this.resultLabel = null;
    this.credentials = null;
    this.SubmitButton = new Button();
    this.PasswordField = new TextField();
    this.PasswordLabel = new Label();
    this.resultLabel = new Label();
  }

  public void destroy() {}

  public void actionPerformed(ActionEvent paramActionEvent)
  {
    String str1 = encrypt(this.PasswordField.getText());
    System.out.println(str1);
    System.out.println(this.PasswordField.getText());
    String str2 = getCodeBase().toString();
    str2 = str2 + "credentials.o";
    try
    {
      URL localURL = new URL(str2);
      this.credentials = ((Credentials)loadCredentials(localURL));
    }
    catch (Exception localException)
    {
      localException.printStackTrace();
    }
    if (this.credentials.checkPassword(str1) == 1) {
      this.resultLabel.setText("Bravo, vous pouvez valider cette epreuve avec le mot de passe !");
    } else {
      this.resultLabel.setText("Eh non...");
    }
  }

  public void start() {}

  public void init()
  {
    setLayout(null);
    this.SubmitButton.setLabel("Ok");
    this.SubmitButton.addActionListener(this);
    this.SubmitButton.setBounds(new Rectangle(175, 8, 50, 20));
    this.PasswordField.setEchoChar('*');
    this.PasswordField.setSize(20, 100);
    this.PasswordField.setBounds(new Rectangle(95, 10, 75, 20));
    this.PasswordLabel.setText("Mot de passe :");
    this.PasswordLabel.setBounds(new Rectangle(10, 10, 75, 20));
    this.resultLabel.setBounds(new Rectangle(10, 35, 500, 20));
    add(this.PasswordLabel);
    add(this.PasswordField);
    add(this.SubmitButton);
    add(this.resultLabel);
  }

  public String encrypt(String paramString)
  {
    String str = new String("");
    for (int i = 0; i < paramString.length(); i++) {
      str = (char)(paramString.charAt(i) ^ 0x7C) + str;
    }
    return str;
  }

  public Object loadCredentials(URL paramURL)
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
