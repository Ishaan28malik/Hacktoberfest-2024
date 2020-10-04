import java.util.Random;
import java.util.concurrent.TimeUnit;

import javax.swing.JFrame;


public class CreatureCounter {
	
	static int gCount;
	public static void main(String[] args)
	{
		JFrame frame = new JFrame("Catch Demogorgan");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gCount=0;
		while(true)
		{
			Random rand = new Random(); 
	        // Generate random integers in range 0 to 999 for coordinates of demon
	        int x = 1+rand.nextInt(600)+rand.nextInt(300); 
	        int y = 1+rand.nextInt(600)+rand.nextInt(600); 
	        int t = rand.nextInt(5);	// random time duration of creature at the coordinates
	        CreatureCounterPanel p=new CreatureCounterPanel(x,y,gCount);	// gCount number of times creature changed position
	        frame.getContentPane().add(p);
			frame.pack();
			frame.setVisible(true);
			try
			{
				TimeUnit.SECONDS.sleep(t);
			}
			catch(InterruptedException ex)
			{
			    System.out.println(ex);
			}
			
			frame.getContentPane().remove(p);	// deleting previous position of demon
			frame.revalidate();
			frame.repaint();
			gCount++;
		}
	}
}
