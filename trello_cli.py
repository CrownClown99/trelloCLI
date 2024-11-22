import json
import requests
import argparse

BASE_URL = "https://api.trello.com/1"

headers = {
    'Accept': 'application/json'
}

def get_auth_params(api_key, token):
    return {
        'key': api_key,
        'token': token
    }

def create_card(list_id, name, description, labels, api_key, token):
    url = f"{BASE_URL}/cards"

    params = {
        'idList': list_id,
        'name': name,
        'desc': description,
        'idLabels': labels,
        **get_auth_params(api_key, token)
    }

    response = requests.post(url, headers=headers,params=params)

    if response.status_code == 200:
        card = json.loads(response.text)
        print(f"Card created: {card['shortUrl']}")
        return card["id"]
    else:
        print(f"Error creating card: {response.status_code} - {response.text}")
        return None
    
def add_comment(card_id, comment, api_key, token):
    url = f"{BASE_URL}/cards/{card_id}/actions/comments"

    params = {
        'text': comment,
        **get_auth_params(api_key, token)
    }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        print(f"Comment added to card {card_id}.")
    else:
        print(f"Error adding comment: {response.status_code} - {response.text}")


def main():
    parser = argparse.ArgumentParser(description="Add a card to a Trello board with labels and a comment.")
    
    parser.add_argument('--api_key', required=True, help="Trello API Key")
    parser.add_argument('--token', required=True, help="Trello API Token")
    parser.add_argument('--list_id', required=True, help="ID of the list (column) where the card will be added")
    parser.add_argument('--name', required=False, default="", help="Name of the Trello card")
    parser.add_argument('--description', required=False, default="", help="Description of the Trello card")
    parser.add_argument('--labels', required=False, default="", help="Comma-separated list of label IDs to apply to the card")
    parser.add_argument('--comment', required=False, help="A comment to add to the card after creation")

    args = parser.parse_args()

    card_id = create_card(args.list_id, args.name, args.description, args.labels, args.api_key, args.token)

    if args.comment and card_id:
        add_comment(card_id, args.comment, args.api_key, args.token)
    
if __name__ == "__main__":
    main()