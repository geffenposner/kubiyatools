import os
import requests

def list_my_knowledge():

    owner_id = '5851e879-552a-4209-bd60-f33f11525d82'


    print("Sending request to Kubiya API...")
    response = requests.get(
        'https://api.kubiya.ai/api/v1/knowledge',
        headers={
            'Authorization': f'UserKey {os.environ["geff_test"]}',
            'Content-Type': 'application/json'
        },
        json={}
    )
    
    if response.status_code >= 400:
        print(f"Error: {response.status_code} {response.text}")
        return
    

    data = response.json()
    filtered_data = [item for item in data if item.get('owner') == owner_id]

    for item in filtered_data:
            print({
                "name": item.get("name"),
                "description": item.get("description"),
                "uuid": item.get("uuid")
            })

if __name__ == "__main__":

    list_my_knowledge()
