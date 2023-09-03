

<p align="center">
  This script allows you to create multiple metafield definitions on a Shopify store via the GraphQL Admin API.
</p>



## Prerequisites

Before using the script, make sure you have the following:

- Shopify store domain (e.g., `store.myshopify.com`)
- API access token with sufficient permissions
- Source data query to fetch metafield definitions (can be obtained from the GraphiQL App)


## Install

Clone the repo and install requirements using pip
1. Clone this repository to your local machine:
```bash
git clone https://github.com/taksh108/shopify-metafields-sync.git
cd shopify-metafield-sync

```
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

2. Run the script using Python:
```bash
python metafield-sync.py
```

3. Follow the prompts to enter your Shopify API details, including the store domain, API access token, and owner type (e.g., PRODUCT).

4. Select a source JSON file containing your GraphQL query to fetch metafield definitions. This file should be in the same directory as the script or specify the full path to the file.

5. The script will create metafield definitions in your Shopify store based on the source data.

## Source Data
The source data query should be a GraphQL query that can be executed through the Shopify GraphiQL App or any other GraphQL client. An example source data query is provided below:
```qraphql
query {
  metafieldDefinitions(first: 250, ownerType: PRODUCT) {
    edges {
      node {
        namespace
        key
        name
        type {
          name
          category
        }
      }
    }
  }
}

```

## Key Features ✨


### 1. Metafield Definition Synchronization

- Create or update metafield definitions in your Shopify store using a structured JSON source.
- Customizable GraphQL query to fetch metafield definitions, allowing flexibility in data sources.

### 2. User-Friendly Prompts &  Colorful Output

- The script guides you through the setup process with easy-to-follow prompts.
- Enter your Shopify store domain, API access token, and owner type interactively.
- Informative console output with color-coded messages.
- Successful operations are highlighted in green, while errors are highlighted in red.

### 3. Error Handling & Summary

- Comprehensive error handling to catch and display API errors, connection issues, or unexpected errors during execution.

- After execution, the script provides a summary report displaying the number of successfully created metafields and any failures.

### 4. Open Source

- This script is open-source and can be customized to suit your specific needs.
- Contributions and feedback are welcome from the GitHub community.


## File Structure
`metafield-sync.py`: The Python script for synchronizing metafield definitions.
`source-query.json`: An example source data file in JSON format.
`requirements.txt`: A list of required Python packages.
## Feedback and Contributions
Feel free to open issues or contribute to this repository. We welcome your feedback and improvements!

*Note:* This script is provided as-is and may require customization for your specific use case. Use it responsibly and ensure you have appropriate permissions and backups before running it on your Shopify store.

