# quote-of-the-day-api

A tiny Flask API that serves random inspirational quotes from a built-in collection

## Features

- Simple REST API endpoint for retrieving random quotes
- Built-in collection of inspirational quotes
- Lightweight Flask-based implementation

## Installation

```bash
pip install flask
```

## Usage

Start the API server:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET `/quote`

Returns a random inspirational quote.

**Response Example:**
```json
{
  "quote": "The only way to do great work is to love what you do.",
  "author": "Steve Jobs"
}
```

## Contributing

Feel free to submit issues or pull requests to improve the quote collection or add new features!

## License

MIT
