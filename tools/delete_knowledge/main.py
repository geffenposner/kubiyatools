import argparse
import os
import requests

def view_knowledge(uuid: str):

    base_url = "https://api.kubiya.ai/api/v1/knowledge"
    knowledge_id = uuid
    url = f"{base_url}/{knowledge_id}"


    print("Sending request to Kubiya API...")
    response = requests.get(
        url,
        headers={
            'Authorization': f'UserKey {os.environ["geff_test"]}',
            'Content-Type': 'application/json'
        },
        json={}
    )
    
    if response.status_code >= 400:
        print(f"Error: {response.status_code} {response.text}")
        return
    

    print(response.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="View the piece of Kubiya knowledge with {uuid}")
    parser.add_argument("uuid", help="uuid of the piece of knowledge")

    # Parse command-line arguments
    args = parser.parse_args()

    # Get coordinates for the given city
    uuid = args.uuid
    view_knowledge(uuid=uuid)
