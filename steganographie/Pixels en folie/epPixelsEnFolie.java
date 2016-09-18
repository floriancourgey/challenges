import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.TreeMap;

import javax.imageio.ImageIO;


public class epPixelsEnFolie {
	public static void main(String[] args){
		
		
		
		//		RGB		Fréquence
		TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();
		
		BufferedImage img = null;
		try {
		    img = ImageIO.read(new File("src/epPixelsEnFolie.png"));
		    
		    int w = img.getWidth();
			int h = img.getHeight();
			

			for( int i = 0; i < w; i++ ){
			    for( int j = 0; j < h; j++ ){
			        int rgb = img.getRGB( i, j );
//			        System.out.println(rgb);
			        if(map.containsKey(rgb)){
			        	Integer frequence = map.get(rgb);
			        	frequence++;
			        	map.put(rgb, frequence);
			        } else {
			        	map.put(rgb, 1);
			        }
			    }
			}
			
			System.out.println(map.size()+" lettres");
			for(Map.Entry<Integer,Integer> entry : map.entrySet()) {
				Integer key = entry.getKey();
				  Integer value = entry.getValue();
				  System.out.println(key + " => " + value +" -} "+String.format("%1$,.2f", (double)value/(w*h)*100)+"% -> "+"#"+Integer.toHexString(key).substring(2));
				}
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}
}
