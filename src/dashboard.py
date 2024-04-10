import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('security_data.json', 'r') as file:
        data = json.load(file)
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
