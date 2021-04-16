from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Learning heroku in praxis"
    
@app.route('/someendpoints')
def firstendpoint():
    return "this is my first path on heroku"


if __name__ == "__main__":
    app.run()