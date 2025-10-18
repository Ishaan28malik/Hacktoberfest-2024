<?php

function bugHunt($name, $platform, $type){
    echo "The most popular bug hunter is" . $name. "<br>";	
    echo "He joined bug bounty program in" . $platform. "<br>";
    echo "The most type of vulnerability that he had reported: " . $type. "<br>";
}

bugHunt(
    " <h1>@todayisnew</h1>",
    " <b>Hackerone</b><br>",
    " <ol>
        <li>Cross-site Scripting</li>
        <li>RCE</li>
        <li>SQLI</li>
        <li>SSRF</li>
    </ol>"
);

?>