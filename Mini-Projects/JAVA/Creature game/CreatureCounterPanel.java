import java.awt.*;
import java.awt.event.*;

import javax.imageio.ImageIO;
import javax.swing.*;

public class CreatureCounterPanel extends JPanel
{
	private static  int count;
	private JButton creature;
	private JLabel label;
	//-----------------------------------------------------------------
	//Constructor: Sets up the GUI.
	//-----------------------------------------------------------------
	public CreatureCounterPanel(int x,int y,int gCount)
	{
		this.setLayout(null);
		if(gCount==0)
			count =0;
		
		label = new JLabel("Score: "+ count);
		label.setForeground(Color.RED);
		label.setFont(new Font("Serif", Font.PLAIN, 30));
		this.add(label);
		Dimension size = label.getPreferredSize();
	    label.setBounds(0, 0, size.width, size.height);
		
		
		
		label.setLayout(null);
		creature = new JButton();
		ImageIcon demon = new ImageIcon("demo.gif");
		creature.setIcon(demon);
		creature.setLayout(null);
		creature.setLocation(x,y);
		
		creature.setSize(220,300);
		creature.addActionListener(new CreatureListener());
		add(creature);
		
		setPreferredSize(new Dimension(1000, 1000));
		setBackground(Color.black);
		
	}
	//*****************************************************************
	//Represents a listener for button push (action) events.
	//*****************************************************************
	private class CreatureListener implements ActionListener
	{
	//--------------------------------------------------------------
	//Updates the counter and label when the button is pushed.
	//--------------------------------------------------------------
		public void actionPerformed(ActionEvent event)
		{
			count++;								// score increses as creature is caught
			label.setText("Score: " + count);	
		}
	}
}