
# Trello CLI Card Adder

This Python CLI tool adds a card to a Trello board with labels and an optional comment. It interacts directly with Trello's REST API using the `requests` library.

## Requirements

- Python 3.x

-  `requests` library

## Setup

1. Get your Trello API Key and Token by visiting the [Trello API Key Generator](https://trello.com/app-key).

2. Clone the repository or download the script.

3. Install dependencies by running:

```bash
pip install requests
```

## Usage
  
Run the script with the following command:

```bash

python  trello_cli.py  --api_key  YOUR_API_KEY  --token  YOUR_TOKEN  --list_id  YOUR_LIST_ID  --name  "Card Name"  --description  "Card Description"  --labels  "Label ID 1,Label ID 2"  --comment  "Your comment"
```

## Acknowledgment

- <https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post>
- <https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-actions-comments-post>
- <https://trello.com/b/hqaDibUF/testing> and <https://trello.com/b/hqaDibUF/testing.json> (My testing board)

## Future Developments

- Add error handling for common API errors for invalid IDs.
- Allow creating new lists if the target list does not exist.
- Add functionality to retrieve list names dynamically from Trello API.

## Completion Estimation

2 - 3 hours