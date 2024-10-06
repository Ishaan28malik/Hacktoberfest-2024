import java.util.Scanner;

class SlidingWindow{

  public String minimumWindowSubstring(char[] ch1,char[] ch2){
    int A=0,B=0,C=0,count=0,length=Integer.MAX_VALUE,flag=0;
    String str="";
    for(int window=1;window<=ch1.length;window++){
      for(int start=0;start<=(ch1.length-window);start++){
        int end=(window+start)-1;
        A=0;B=0;C=0;flag=0;count=0;
        if(ch2.length<=(end-start)){
          for(int i=0;i<ch2.length;i++){
            flag=0;
            for(int j=start;j<=end;j++){
              if(ch1[j]==ch2[i]){
                flag=1;
                count++;
              }
            }
            if(flag==0){
              count=0;
              break;
            }
        }
          if(length>(end-start) && count>=ch2.length){
            length=(end-start);
			      str="";
            for(int i=start;i<=end;i++){
              str=str+ch1[i];
            }
            count=0;
          }
      }  
  }
}
    return str;
}

  public static void main(String[] args){

	SlidingWindow sw=new SlidingWindow();

    Scanner sc=new Scanner(System.in);
    System.out.print("Enter String1: ");
    String s1=sc.nextLine();
    System.out.print("Enter String2: ");
    String s2=sc.nextLine();
    char[] ch1=s1.toCharArray();
    char[] ch2=s2.toCharArray();
    System.out.println("Minimum Substring(Using Window): "+sw.minimumWindowSubstring(ch1,ch2));
  }
}
