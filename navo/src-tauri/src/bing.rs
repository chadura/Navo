let mut default = HashMap::new();
default.insert("api_key".to_string(), "your_secret_api_key".to_string());
default.insert("engine".to_string(), "bing".to_string());
// initialize the search engine
let client = Client::new(default);

// let's search for coffee in Austin, TX
let mut parameter = HashMap::new();
parameter.insert("q".to_string(), "coffee".to_string());
// copy search parameter for the html search
use serpapi::serpapi::Client;
use std::collections::HashMap;
use std::env;

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
    println!(" - raw HTML size {} bytes\n", raw.len());
    println!(
        " - async search completed with {}\n",
        results["search_parameters"]["engine"]
    );
}

print!("ok");
Ok(())
