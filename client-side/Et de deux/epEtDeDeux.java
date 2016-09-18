// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Applet2.java

import java.applet.Applet;
import java.awt.*;
import java.util.Locale;

public class epEtDeDeux extends Applet
{

    /**
	 * 
	 */
	private static final long serialVersionUID = 5109581813045808197L;
	public epEtDeDeux()
    {
        passLabel = new Label();
        passwd = new TextField();
        login = new Button();
        resultLabel = new Label();
        buildGUI();
        initPwd();
    }

    private void buildGUI()
    {
        setLayout(null);
        passLabel.setText("Mot de passe : ");
        passLabel.setBounds(new Rectangle(10, 10, 75, 20));
        login.setLabel("OK");
        login.setBounds(new Rectangle(175, 8, 50, 20));
        passwd.setSize(20, 100);
        passwd.setBounds(new Rectangle(95, 10, 75, 20));
        resultLabel.setAlignment(2);
        resultLabel.setLocale(Locale.getDefault());
        resultLabel.setBounds(new Rectangle(10, 35, 215, 20));
        add(passLabel);
        add(passwd);
        add(login);
        add(resultLabel);
    }

    @SuppressWarnings("deprecation")
	public boolean handleEvent(Event event)
    {
        if(event.id == 1001 && event.target == login)
        {
            if(passwd.getText().equals(pwd))
                resultLabel.setText("C'\351tait simple, je l'avoue!");
            else
                resultLabel.setText("Cherche encore ;)");
        }
        return super.handleEvent(event);
    }

    private void initPwd()
    {
        pwd = "";
        int sequence[] = {
            109, 119, 97, 105
        };
        for(int i = 0; i < sequence.length; i++)
        {
            char c = (char)sequence[i];
            pwd += c;
        }

    }

    Button login;
    Label passLabel;
    TextField passwd;
    String pwd;
    Label resultLabel;
}
