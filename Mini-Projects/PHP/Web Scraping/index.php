<?php
require 'simple_html_dom.php';

function file_get_contents_curl($url)
{
    $ch = curl_init();

    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_URL, $url);

    $data = curl_exec($ch);
    curl_close($ch);

    return $data;
}

$link = "";
$titleArray = array();
$iconArray = array();

for ($i = 0; $i < 22; $i++) {
    if ($i == 0) {
        $link = 'https://www.the-mainboard.com/index.php?sport-teams';
    } else {
        $page_number = $i + 1;
        $link = 'https://www.the-mainboard.com/index.php?sport-teams/&page=' . $page_number;
    }

    $html = file_get_html($link);

    foreach ($html->find('.section .memberList') as $list) {

        $name = $list->find('h3.title');
        foreach ($name as $item) {
            array_push($titleArray, $item->innertext);
        }

        $icon = $list->find('img');
        foreach ($icon as $item) {
            array_push($iconArray, $item->src);
        }

    }
}

$servername = "localhost";
$username = "debian-sys-maint";
$password = "CMh8AaggOu6EyKho";
$dbName = "scrapingDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$length = sizeof($titleArray);
for ($i = 0; $i < $length; $i++) {
    $title = $titleArray[$i];

    $icon = $iconArray[$i];
    $new_icon = explode("/", $icon)[4];

    $url = "https://www.the-mainboard.com/data/brivium/SportTeamIcons/0/" . $new_icon;
    $image_path = $new_icon;

    $data = file_get_contents_curl($url);
    file_put_contents($image_path, $data);

    $sql = "INSERT INTO FanOfTMBData (title, icon) VALUES ('$title', '$new_icon')";

    if ($conn->query($sql) === true) {
        echo $title . " " . $new_icon . " record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}



$conn->close();
