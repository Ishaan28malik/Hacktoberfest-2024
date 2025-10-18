<?php

class bughunt {
  
   var $name;
   var $platform;
   var $type;
  
    function letmeIn() {
        return "Get alerted to more vulnerabilities.";
    }
    function topBounty() {
        return "XSS, RCE, SSRF, LFI, SQLI";
    }
}
  
$bughunter = new bughunt();
  
$bughunter->name="Orange TSAI";
$bughunter->platform="<b>Hackerone & Bugcrowd</b>";
$bughunter->type="RCE & SSRF";

echo "Hello there! The master of RCE is.".$bughunter->name;
echo "<br>";
echo "He joined bug bounty program in ".$bughunter->platform;
echo "<br>";
echo "The most type of vulnerability that he had reported: ".$bughunter->type;
echo "<br>";

echo "<br> Hackerone invite you: ";
echo $bughunter->letmeIn();
echo "<br>";
echo "Let the bounty flows by search this vulnerability: ";
echo $bughunter->topBounty(); 
?>

