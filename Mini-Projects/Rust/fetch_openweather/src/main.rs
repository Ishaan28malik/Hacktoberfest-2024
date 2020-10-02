#[macro_use]
extern crate dotenv_codegen;
use dotenv::dotenv;
use std::io::stdin;
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    dotenv().ok();
    let _apikey: String = dotenv!("OPENWEATHERMAP_APIKEY").to_string();

    println!("Input City :");
    let mut city = String::new();
    stdin().read_line(&mut city).ok().expect("No city");

    let client = reqwest::Client::new();
    let weather = client.get("http://api.openweathermap.org/data/2.5/forecast")
        .query(&[("q",&city),("appid",&_apikey)])
        .send()
        .await?
        .text()
        .await?;

    let res: Value = serde_json::from_str(&weather).unwrap();
    let date = &res["list"][0]["dt_txt"];
    let description = &res["list"][0]["weather"][0]["description"];
    println!("the weather in {} at {} is {}", city, date, description);

    Ok(())
}
