// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Applet1.java

import java.applet.Applet;
import java.awt.*;
import java.util.Locale;

public class epTiensUneApplet extends Applet
{

    /**
	 * 
	 */
	private static final long serialVersionUID = 8639288708463222882L;
	public epTiensUneApplet()
    {
        passLabel = new Label();
        passwd = new TextField();
        login = new Button();
        resultLabel = new Label();
        buildGUI();
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
            if(passwd.getText().equals("facile!"))
                resultLabel.setText("C'\351tait simple, je l'avoue!");
            else
                resultLabel.setText("Cherche encore ;)");
        }
        return super.handleEvent(event);
    }

    Button login;
    Label passLabel;
    TextField passwd;
    Label resultLabel;
}
