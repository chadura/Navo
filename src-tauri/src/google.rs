use serpapi::serpapi::Client;
use std::collections::HashMap;
use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Read your private API Key from an environment variable.
    // Copy/paste from [https://serpapi.com/dashboard] to your shell:
    // ```bash
    // export API_key="paste_your_private_api_key"
    // ```
    let api_key = match env::var_os("API_KEY") {
        Some(v) => v.into_string().unwrap(),
        None => panic!("$API_KEY environment variable is not set!"),
    };

    println!("let's initiliaze the client to search on google");
    let mut default = HashMap::new();
    default.insert("api_key".to_string(), api_key);
    default.insert("engine".to_string(), "google".to_string());
    // initialize the search engine
    let client = Client::new(default);

    // let's search for coffee in Austin, TX
    let mut parameter = HashMap::new();
    parameter.insert("q".to_string(), "coffee".to_string());
    parameter.insert("engine".to_string(), "google".to_string());
    // copy search parameter for the html search
    let mut html_parameter = HashMap::new();
    html_parameter.clone_from(&parameter);

    // search returns a JSON as serde_json::Value which can be accessed like a HashMap.
    println!("waiting...");
    let results = client.search(parameter).await?;
    let organic_results = results["organic_results"].as_array().unwrap();
    println!("results received");
    println!("--- JSON ---");
    let status = &results["search_metadata"]["status"];
    if status != "Success" {
        println!("search failed with status: {}", status);
    } else {
        println!("search is successfull");

        println!(" - number of organic_results: {}", organic_results.len());
        println!(
            " - organic_results first result description: {}",
            results["organic_results"][0]
        );

        // search returns text
        println!("--- HTML search ---");
        let raw = client.html(html_parameter).await.expect("html content");
        println!(" - raw HTML size {} bytes\n", raw.len());
        println!(
            " - async search completed with {}\n",
            results["search_parameters"]["engine"]
        );
    }

    print!("ok");
    Ok(())
}