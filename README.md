# Quote of the Day API

A tiny Flask API that serves random inspirational quotes from a built-in collection.

## Features

- 🎯 Simple REST API
- 📚 Built-in collection of 8 inspirational quotes
- 🎲 Random quote selection
- 🚀 Lightweight and easy to deploy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd quote-of-the-day-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Flask application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### `GET /`
Returns API information and available endpoints.

**Example Response:**
```json
{
  "message": "Welcome to Quote of the Day API!",
  "endpoints": {
    "/": "API information",
    "/quote": "Get a random inspirational quote",
    "/quotes": "Get all quotes"
  }
}
```

### `GET /quote`
Returns a random inspirational quote.

**Example Response:**
```json
{
  "text": "The only way to do great work is to love what you do.",
  "author": "Steve Jobs"
}
```

### `GET /quotes`
Returns all quotes in the collection.

**Example Response:**
```json
{
  "count": 8,
  "quotes": [...]
}
```

## Testing

You can test the API using curl:
```bash
# Get a random quote
curl http://localhost:5000/quote

# Get all quotes
curl http://localhost:5000/quotes
```

## License

MIT License - Feel free to use this project for learning and inspiration!
