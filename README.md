# Weather Chatbot with Pydantic AI

A command-line weather chatbot that provides current temperature information for any location using latitude and longitude coordinates. The chatbot is powered by Gemini 1.5 Flash and uses the Open-Meteo API for weather data.

## Features

- Interactive CLI interface
- Real-time weather data retrieval
- Temperature information in Fahrenheit
- Powered by Google's Gemini 1.5 Flash AI model

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-chatbot-pydantic-ai.git
   cd weather-chatbot-pydantic-ai
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Export the Gemini API Key
For the chatbot to access the Gemini API, you need to set the API key as an environment variable.
    ```bash
   export GEMINI_API_KEY="YOUR_API_KEY"
   ```

## Running the Chatbot

1. Make sure your virtual environment is activated
2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

## Usage

1. When prompted, enter a query about the weather for a specific location using latitude and longitude
2. Example queries:
   - "What's the temperature at latitude 40.7128 and longitude -74.0060?"
   - "Tell me the current temperature in New York (40.7128, -74.0060)"
3. Type 'quit', 'exit', or 'bye' to end the conversation

## API Information

This project uses:
- Open-Meteo API for weather data (free, no API key required)
- Google's Gemini 1.5 Flash model for natural language processing

## License

[Add your license information here]