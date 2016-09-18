// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Applet3.java

import java.applet.Applet;
import java.awt.*;
import java.util.Locale;

public class epJamaisDeuxSansTrois extends Applet
{

    /**
	 * 
	 */
	private static final long serialVersionUID = 5613580709260533906L;
	public epJamaisDeuxSansTrois()
    {
        passLabel = new Label();
        passwd = new TextField();
        login = new TextField();
        loginButton = new Button();
        resultLabel = new Label();
        loginLabel = new Label();
        buildGUI();
    }

    private void buildGUI()
    {
        setLayout(null);
        loginLabel.setText("Login : ");
        loginLabel.setBounds(new Rectangle(10, 10, 75, 20));
        passLabel.setText("Mot de passe : ");
        passLabel.setBounds(new Rectangle(10, 40, 75, 20));
        loginButton.setLabel("OK");
        loginButton.setBounds(new Rectangle(175, 38, 50, 20));
        passwd.setBounds(new Rectangle(95, 40, 75, 20));
        login.setBounds(new Rectangle(95, 10, 75, 20));
        resultLabel.setAlignment(2);
        resultLabel.setLocale(Locale.getDefault());
        resultLabel.setBounds(new Rectangle(10, 65, 215, 20));
        add(passLabel);
        add(passwd);
        add(login);
        add(loginButton);
        add(loginLabel);
        add(resultLabel);
    }

    @SuppressWarnings("deprecation")
	public boolean handleEvent(Event event)
    {
        if(event.id == 1001 && event.target == loginButton)
        {
            String login = "";
            int sequence[] = {
                108, 117, 99
            };
            for(int i = 0; i < sequence.length; i++)
            {
                char c = (char)sequence[i];
                login = login + c;
            }

            String pwd = "";
            for(int i = login.length() - 1; i >= 0; i--)
                pwd = pwd + login.charAt(i);

            if(passwd.getText().equals(pwd))
                resultLabel.setText("C'\351tait simple, je l'avoue!");
            else
                resultLabel.setText("Cherche encore ;)");
        }
        return super.handleEvent(event);
    }

    TextField login;
    Button loginButton;
    Label loginLabel;
    Label passLabel;
    TextField passwd;
    Label resultLabel;
}
