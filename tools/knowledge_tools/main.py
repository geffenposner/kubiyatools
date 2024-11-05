import argparse
import os
import requests

def create_knowledge(
        title: str,
        description: str,
        tags: list[str],
        content: str,
        teammates_with_access: list[str],
        user_groups_with_access: list[str],
):
    print({
            "name": title,
            "description": description,
            "labels": tags,
            "content": content,
            "type": "knowledge",
            "source": "manual",
            "properties": {},
            "supported_agents": teammates_with_access,
            "groups": user_groups_with_access,
        })


    print("Sending request to Kubiya API...")
    response = requests.post(
        'https://api.kubiya.ai/api/v1/knowledge',
        headers={
            'Authorization': f'UserKey {os.environ["geff_test"]}',
            'Content-Type': 'application/json'
        },
        json={
            "name": title,
            "description": description,
            "labels": tags,
            "content": content,
            "type": "knowledge",
            "source": "manual",
            "properties": {},
            "supported_agents": teammates_with_access,
            "groups": user_groups_with_access,
            "supported_agents_groups": [],
            "owner": "5851e879-552a-4209-bd60-f33f11525d82",
            "uuid": ""
        }
    )
    print(response.json())
    if response.status_code >= 400:
        print(f"Error: {response.status_code} {response.text}")
        return
    
    base_url = "https://app.kubiya.ai/knowledge"
    try:
        knowledge_id = response.json()["uuid"]
        url = f"{base_url}/{knowledge_id}"
        print("Knowledge created successfully! Link: ", url)
    except Exception:
        print(f"Knowledge created successfully! You can find it in {base_url}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a piece of Kubiya knowledge with {content}!")
    parser.add_argument("title", help="title of the piece of knowledge")
    parser.add_argument("description", help="description of the piece of knowledge")
    parser.add_argument("tags", help="tags related to the piece of knowledge. multiple tags should be comma separated")
    parser.add_argument("content", help="content of the piece of knowledge")
    # parser.add_argument("teammates_with_access", help="Kubiya teammates with access to the piece of knowledge")
    # parser.add_argument("user_groups_with_access", help="groups of Kubiya users with access to the piece of knowledge")

    # Parse command-line arguments
    args = parser.parse_args()

    # Get coordinates for the given city
    title = args.title
    description = args.description
    tags = args.tags.split(",") if args.tags else []
    content = args.content
    teammates_with_access = ["7ab4303c-f594-4100-a766-d0adfe3dfd2d"]
    user_groups_with_access = ["a1c68f8f-5090-46a8-9ce0-dd71ac4630f8"]
    # teammates_with_access = args.teammates_with_access.split(",") if args.teammates_with_access else ["7ab4303c-f594-4100-a766-d0adfe3dfd2d"]
    # user_groups_with_access = args.user_groups_with_access.split(",") if args.user_groups_with_access else ["a1c68f8f-5090-46a8-9ce0-dd71ac4630f8"]

    create_knowledge(
        title=title,
        description=description,
        tags=tags,
        content=content,
        teammates_with_access=teammates_with_access,
        user_groups_with_access=user_groups_with_access,
    )
