from flask import Flask, jsonify
import random

app = Flask(__name__)

# Built-in collection of inspirational quotes
QUOTES = [
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    },
    {
        "text": "Innovation distinguishes between a leader and a follower.",
        "author": "Steve Jobs"
    },
    {
        "text": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon"
    },
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt"
    },
    {
        "text": "It is during our darkest moments that we must focus to see the light.",
        "author": "Aristotle"
    },
    {
        "text": "The only impossible journey is the one you never begin.",
        "author": "Tony Robbins"
    },
    {
        "text": "In the middle of difficulty lies opportunity.",
        "author": "Albert Einstein"
    },
    {
        "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "Winston Churchill"
    }
]

@app.route('/')
def home():
    """Home endpoint with API information."""
    return jsonify({
        "message": "Welcome to Quote of the Day API!",
        "endpoints": {
            "/": "API information",
            "/quote": "Get a random inspirational quote",
            "/quotes": "Get all quotes"
        }
    })

@app.route('/quote')
def get_quote():
    """Return a random quote from the collection."""
    quote = random.choice(QUOTES)
    return jsonify(quote)

@app.route('/quotes')
def get_all_quotes():
    """Return all quotes in the collection."""
    return jsonify({
        "count": len(QUOTES),
        "quotes": QUOTES
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
