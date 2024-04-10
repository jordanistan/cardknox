import requests
from faker import Faker
from requests_slack import SlackClient
from flask import Flask, render_template

app = Flask(__name__)

# Initialize a new Slack client
client = SlackClient(token='YOUR-TOKEN')

# Generate fake user data using Faker
fake = Faker()

# Generate fake transactions
def generate_fake_transactions():
    transactions = []
    for _ in range(50):
        amount = fake.random_number(digits=3)  # Generating random amount
        card_type = fake.credit_card_provider()  # Generating random card type
        card_holder_name = fake.name()  # Generating random card holder name
        transactions.append({'amount': amount, 'card': {'cardType': card_type, 'cardHolderName': card_holder_name}})
    return transactions

# Get the API URL for CardKnox's transactions endpoint
url = 'https://api.cardknox.com/v1/transactions'

# Dummy auth info
auth_info = {'Authorization': 'Bearer YOUR-ACCESS-TOKEN'}

# Make a GET request to the CardKnox API endpoint with parameters for transaction amount and limit
@app.route('/')
def dashboard():
    transactions = generate_fake_transactions()
    for transaction in transactions:
        if transaction['amount'] > 100 and transaction['card']['cardType'] == 'visa':
            print(f'Transaction found: {transaction["amount"]} by {transaction["card"]["cardHolderName"]}')
            slack_message = f"Fraud detected, transaction amount {transaction['amount']} by {transaction['card']['cardHolderName']}. Please review."
            client.chat.post_message(slack_channel='YOUR-CHANNEL', text=slack_message)
        else:
            print('Transaction not found.')
    return render_template('dashboard.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
