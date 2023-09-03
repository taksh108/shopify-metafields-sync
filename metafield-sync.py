

import requests
import json  # Add this line to import the json module
from colorama import Fore, Style

global created_count
global failed_count
created_count = 0
failed_count = 0

print("Enter Shopify API Details")

SHOP_DOMAIN = input("Enter your Shopify store domain (store.myshopify.com): ")


# Construct full API endpoint 
API_ENDPOINT = f"https://{SHOP_DOMAIN}/admin/api/2023-07/graphql.json"

API_ACCESS_TOKEN = input("Enter API access token: ")
OWNER_TYPE = input("Enter owner type (PRODUCT, SHOP etc.): ")

# # Replace with your GraphQL API endpoint
# API_ENDPOINT = "https://your-store.myshopify.com/admin/api/2023-07/graphql.json"

# # Replace with your Shopify access token
# API_ACCESS_TOKEN = ""


SOURCE_FILE_NAME = input("Source File:")
with open(SOURCE_FILE_NAME, 'r') as source_file:
    source_data = json.load(source_file)

# Source data containing metafield definitions


# Define a valid ownerType from the MetafieldOwnerType enum
# Replace with the appropriate owner type based on your use case

OWNER_TYPE = "PRODUCT"


def create_metafield_definition(definition):
    global failed_count  # Declare failed_count as a global variable
    global created_count  # Declare created_count as a global variable
    node = definition["node"]


    # Define the GraphQL mutation to create a metafield definition
    mutation = f'''
    mutation {{
        metafieldDefinitionCreate(definition: {{
            namespace: "{node["namespace"]}",
            key: "{node["key"]}",
            name: "{node["name"]}",
            type: "{node["type"]["name"]}",
            ownerType: {OWNER_TYPE},  # Use the valid ownerType here
            description: ""
        }}) {{
            userErrors {{
                field
                message
            }}
        }}
    }}
    '''

    # Create the GraphQL request payload
    payload = {
        "query": mutation
    }

    # Set the request headers
    headers = {
        "X-Shopify-Access-Token": API_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    # Send the GraphQL request

    try:
        # Send the GraphQL request
        response = requests.post(API_ENDPOINT, data=json.dumps(payload), headers=headers)

        # Handle the response
        if response.status_code == 200:
            result = response.json()
            if "errors" in result:
                print(f"{Fore.RED}API Errors:{Style.RESET_ALL}")
                failed_count += 1
                for error in result["errors"]:
                    print(f"- {error['message']}")
            else:
                metafield_definition = result["data"]["metafieldDefinitionCreate"]
                errors = metafield_definition["userErrors"]
                if errors: 
                    print(f"{Fore.RED}User Errors:{Style.RESET_ALL}")
                    for error in errors:
                        print(f"- {error['message']}")
                    failed_count += 1
                else:
                    print(f"{Fore.GREEN}Metafield created:{Style.RESET_ALL} {metafield_definition}")
                    created_count += 1
        else:
            print(f"{Fore.RED}Request Failed. Status: {response.status_code}{Style.RESET_ALL}")
    except requests.exceptions.ConnectionError as e:
        print(f"{Fore.RED}Connection Error: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

def main():
    definitions = source_data["data"]["metafieldDefinitions"]["edges"]
    for definition in definitions:
        print(f"Adding \033[1m\033[93m{definition['node']['namespace']}.{definition['node']['key']}\033[0m as a {OWNER_TYPE} metafield")
        create_metafield_definition(definition)
    # Print summary 
    print(f"Total definitions: {len(definitions)}")
    # print(f"\n{Fore.GREEN}Created:{Style.RESET_ALL} {created_count}")  
    # print(f"{Fore.RED}Failed:{Style.RESET_ALL} {failed_count}")

    print_summary()

def print_summary():
  print(f"{Fore.GREEN}Created: {created_count}{Style.RESET_ALL}")
  print(f"{Fore.RED}Failed: {failed_count}{Style.RESET_ALL}")


if __name__ == "__main__":
    created_count = 0
    failed_count = 0
    print()
    main()