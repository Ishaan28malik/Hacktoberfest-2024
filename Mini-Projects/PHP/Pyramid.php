<?php
echo "\t\tHacktober Fest 2020\n";
for($i = 1; $i <= 25; $i ++) {
	$hack = array(0,"H",0,"A",0,"C",0,"K",0,"T",0,"O",0,"B",0,"E",0,"R",0,"F",0,"E",0,"S",0,"T");
	if (!($i % 2) && $i != 1)
		continue;
	print str_pad(str_repeat($hack[$i], $i),(50 - 1) * strlen($hack[$i]), " " , STR_PAD_BOTH);
	print PHP_EOL;
}

/*
                        H                        
                       AAA                       
                      CCCCC                      
                     KKKKKKK                     
                    TTTTTTTTT                    
                   OOOOOOOOOOO                   
                  BBBBBBBBBBBBB                  
                 EEEEEEEEEEEEEEE                 
                RRRRRRRRRRRRRRRRR                
               FFFFFFFFFFFFFFFFFFF               
              EEEEEEEEEEEEEEEEEEEEE              
             SSSSSSSSSSSSSSSSSSSSSSS             
            TTTTTTTTTTTTTTTTTTTTTTTTT            
*/
