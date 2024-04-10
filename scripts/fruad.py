# In this script, we're using the `requests` library to make a GET request to the CardKnox API endpoint `/transactions`, with parameters
# `filter[transactionAmount] = 200` and `limit = 50`. The auth information is provided as HTTP basic authentication. We then loop through the response,
# checking if each transaction meets our filter criteria of amount greater than $100 and a Visa card type. If it does, we send the message to Slack
# using the `send_slack` function from the `requests-slack` library.

import requests
from requests_slack import SlackClient

# Initialize a new Slack client
client = SlackClient(token='YOUR-TOKEN')

# Get the API URL for CardKnox's transactions endpoint
url = 'https://api.cardknox.com/v1/transactions'

# Set up authentication using an OAuth 2.0 access token
auth_info = {'Authorization': 'Bearer YOUR-ACCESS-TOKEN'}

# Make a GET request to the CardKnox API endpoint with parameters for transaction amount and limit
params = {
 'filter[transactionAmount]': '200',
 'limit': 50,
 'include_cardholder_data': True
}
response = requests.get(url, auth=auth_info, params=params)
if response.status_code == 200:
 transactions = response.json()['transactions']
 for transaction in transactions:
 if transaction['amount'] > 100 and transaction['card']['cardType'] == 'visa':
 print(f'Transaction found: {transaction["amount"]} by {transaction["card"]["cardHolderName"]}')
 slack_message = f"Fraud detected, transaction amount {transaction['amount']} by {transaction['card']['cardHolderName']}. Please review."
 client.chat.post_message(slack_channel='YOUR-CHANNEL', text=slack_message)
 else:
 print('Transaction not found.')
