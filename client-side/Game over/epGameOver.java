

public class epGameOver {
	final String tab = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789_$&#@";
	final int tailleTab = tab.length();
	final int checksum = 3696619;
	final String password = "souris";
	final int taillePassword = password.length();
	
	public epGameOver(){
		Stringer ster = new Stringer(tab);
		
		String s = "";
		long t = System.currentTimeMillis();
		while((s=ster.nextString()) != "@@@@@@"){
			if(hash(s) == checksum)
				System.out.println((s));
			if(ster.generated % 1000000 == 0)
				System.out.println(ster.generated+" générés, actuel '"+s+"', écoulé "+((System.currentTimeMillis()-t)/1000)+"s");
		}
		
	}
	
	private int hash(String login){
		int sum=1;
		int n=Math.max(login.length(),taillePassword);
		for (int i=0;i<n;i++) {
			int index1 = 10;
			if(i<login.length()){
				index1=tab.indexOf(login.substring(i,i+1))+10;
			}
			int index2 = 10;
			if(i<password.length()){
				index2=tab.indexOf(password.substring(i,i+1))+10;
			}
			int sum1 = (index1*n*(i+1));
			int sum2 = (index2*(i+1)*(i+1));
			sum=sum+sum1*sum2;
		}
		return sum;
	}
	
	
	public class Stringer {
		
		/**
		 * @Author Tobias Gläser
		 * used to generate brute-force strings
		 */
		
//		public final char[] CHARSET_ALL = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','_', '$', '&','#','@'};
		private boolean first = true;
		private char[] charset;
		private String string;
		private int maxid;
		public long generated = 0;
		
		public Stringer(String alphabet){
			this.charset = alphabet.toCharArray();
//			string = String.valueOf(charset[0]);
			string = "AAAAAA";
			maxid = charset.length-1;
		}
		public String nextString(){
			generated++;
			if(!first){
				this.string = addOne(string);
				return this.string;
			} else {
				first = false;
				return string;
			}
		}
		public int getCharsetCount(){
			return charset.length;
		}
		public String getCurrent(){
			return this.string;
		}
		private String addOne(String s){
			char[] old = s.toCharArray();
			int cid = getID(old[old.length-1]);
			if(cid<maxid){
				//normal case
				StringBuilder b = new StringBuilder();
				for(int i=0;i<old.length-1;i++){
					b.append(old[i]);
				}
				b.append(getById(cid+1));
				return b.toString();
			} else {
				//increase case
				boolean total = true;
				int cs = 1;
				p:
				for(;cs<old.length;cs++){
					cid = getID(old[old.length-(cs+1)]);
					if(cid<maxid){
						total = false;
						break p;
					}
				}
				if(total){
					int nl = old.length+1;
					StringBuilder b = new StringBuilder();
					for(int i=0;i<nl;i++){
						b.append(getById(0));
					}
					return b.toString();
				} else {
					StringBuilder b = new StringBuilder();
					int needed = old.length;
					int caseid = old.length-cs;
					for(int i=0;i<caseid-1;i++){
						b.append(old[i]);
						needed--;
					}
					b.append(getById(getID(old[caseid-1])+1));
					needed--;
					for(int i=0;i<needed;i++){
						b.append(getById(0));
					}
					return b.toString();
				}
			}
		}
		private char getById(int id){
			return charset[id];
		}
		private int getID(char c){
			for(int i=0;i<charset.length;i++){
				if((int)charset[i] == (int)c){
					return i;
				}
			}
			return -1;
		}
	}

}
