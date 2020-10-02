package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

var foursquare_client_id = "PQSPJYQ4ODOORBDB51EQTURIFOQT0PACPFQI2UN0G0P00DAF"
var foursquare_client_secret = "3ZUE0PGPDY2KV4UFPWEQGLZ4GNDWC2PZHFTX40CKZTCIA3LP"

func FindARestaurant(mealType string, location string) {

	latitude, longitude := GetGeocodeLocation(location)
	lat := fmt.Sprintf("%f", latitude)
	long := fmt.Sprintf("%f", longitude)

	url := "https://api.foursquare.com/v2/venues/search?client_id=" + foursquare_client_id + "&client_secret=" + foursquare_client_secret + "&v=20130815&ll=" + lat + "," + long + "&query=" + mealType

	//fmt.Println(url)
	resp, err := http.Get(url)
	if err != nil {
		panic("Error")
	}
	body, err2 := ioutil.ReadAll(resp.Body)
	var data map[string]interface{}
	json.Unmarshal(body, &data)
	if err2 != nil {
		panic("Error")
	}
	for _, v := range data["response"].(map[string]interface{}) {

		for _, v2 := range v.([]interface{}) {
			id := v2.(map[string]interface{})["id"].(string)
			rest_name := v2.(map[string]interface{})["name"]
			rest_address := v2.(map[string]interface{})["location"].(map[string]interface{})["formattedAddress"]
			Imgurl := "https://api.foursquare.com/v2/venues/" + id + "/photos?client_id=" + foursquare_client_id + "&v=20150603&client_secret=" + foursquare_client_secret
			imageResp, err3 := http.Get(Imgurl)
			RespBody, err4 := ioutil.ReadAll(imageResp.Body)
			if err3 != nil || err4 != nil {
				panic(err3)
			}
			var ImgData map[string]interface{}
			json.Unmarshal(RespBody, &ImgData)

			var prefix string
			var suffix string
			var imageURL string

			for _, v := range ImgData["response"].(map[string]interface{}) {
				items := v.(map[string]interface{})["items"]
				for _, v := range items.([]interface{}) {
					prefix = v.(map[string]interface{})["prefix"].(string)
					suffix = v.(map[string]interface{})["suffix"].(string)

					if prefix != "" && suffix != "" {
						imageURL = prefix + "300x300" + suffix
					}

				}

				if imageURL == "" {
					imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
				}

			}

			restaurantInfo := map[string]interface{}{
				"name":    rest_name,
				"address": rest_address,
				"image":   imageURL}

			fmt.Println(restaurantInfo)
			fmt.Println()
			fmt.Println()

		}
	}
}

func GetGeocodeLocation(s string) (float64, float64) {
	google_api_key := "AIzaSyAcKRO63SCy87HvebSXO0v6Gjp444PwNG8"
	locationString := strings.ReplaceAll(s, " ", "+")
	url := ("https://maps.googleapis.com/maps/api/geocode/json?address=" + locationString + "&key=" + google_api_key)
	response, err := http.Get(url)
	if err != nil {
		panic("Error retreiving response")
	}

	body, err2 := ioutil.ReadAll(response.Body)
	if err2 != nil {
		panic("Error retreiving response")
	}

	var longitude float64
	var latitude float64
	var values map[string]interface{}

	json.Unmarshal(body, &values)
	for _, v := range values["results"].([]interface{}) {
		for i2, v2 := range v.(map[string]interface{}) {
			if i2 == "geometry" {
				latitude = v2.(map[string]interface{})["location"].(map[string]interface{})["lat"].(float64)
				longitude = v2.(map[string]interface{})["location"].(map[string]interface{})["lng"].(float64)
				break
			}
		}
	}
	return latitude, longitude
}

func main() {
	FindARestaurant("Pizza", "Pune, India")
}
