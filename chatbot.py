from pydantic_ai import Agent, RunContext
import requests

agent = Agent(
    'google-gla:gemini-1.5-flash',
    system_prompt='You are a weather assistant. You will be given a latitude and longitude and you will need to return the current temperature in that location.',
)

@agent.tool
def get_weather(ctx: RunContext[str], latitude: str, longitude: str) -> str:
    """
    Retrieves the current temperature for a given latitude and longitude.
    """
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&current_weather=true&temperature_unit=fahrenheit"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        current_temperature = data['current_weather']['temperature']
        return f"The current temperature is {current_temperature}°F."
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except (KeyError, TypeError) as e:
        return f"Error parsing weather data: {e}"

def start_cli_conversation():
    print("🤖 Weather Chatbot 🌤️")
    print(agent.system_prompt)
    print("-" * 20)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break

        try:
            result = agent.run_sync(user_input)
            print(f"🤖 Assistant: {result.data}")
        except Exception as e:
            print(f"Error during processing: {e}")

if __name__ == "__main__":
    start_cli_conversation()