import java.io.File;



public class epBrainFuck {
	public static void main(String[] args){
		BrainfuckEngine bf = new BrainfuckEngine(25);
		try {
			bf.interpret(new File("src/epBrainFuck.bf"));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	
}
