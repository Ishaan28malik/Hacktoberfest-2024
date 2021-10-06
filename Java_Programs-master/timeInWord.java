import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class timetoword {

    // Complete the timeInWords function below.
    static String timeInWords(int h, int m) {

        String s="";
        String ones[]={ "", "one ", "two ", "three ", "four ", 
                 "five ", "six ", "seven ", "eight ", 
                 "nine ", "ten ", "eleven ", "twelve ", 
                 "thirteen ", "fourteen ", "fifteen ", 
                 "sixteen ", "seventeen ", "eighteen ", 
                 "nineteen "
               };
        String tens[] = { "", "", "twenty ", "thirty ", "forty ", 
                 "fifty " };
            if(m==00)
            s=(ones[h]+"o' clock");
            else if(m<30)
            {
                if(m==15)
                s=("quarter past "+ones[h]);
                else
                {
                    if(m==1)
                    s=(ones[m]+"minute past "+ones[h]);
                    else if(m<20)
                    s=(ones[m]+"minutes past "+ones[h]);
                    else{
                    int x=m%10;
                    m/=10;
                    
                    s=(tens[m]+""+ones[x]+"minutes past "+ones[h]);
                    }
                }
            }
            else if(m==30)
            s=("half past "+ones[h]);
            else
            {
                if(m==45)
                s=("quarter to "+ones[h+1]);
                else
                {
                    m=60-m;
                    if(m<20)
                   s=(ones[m]+"minutes to "+ones[h+1]);
                    else
                    {
                    int x=m%10;
                    m/=10;
                    
                    
                    s=(tens[m]+""+ones[x]+" minutes to "+ones[h+1]);
                    }
                }
            }
                   
return s;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
       // BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int h = scanner.nextInt();
        //scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int m = scanner.nextInt();
        //scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String result = timeInWords(h, m);

        //bufferedWriter.write(result);
        //bufferedWriter.newLine();

        //bufferedWriter.close();

        System.out.print(result);
    }
}
