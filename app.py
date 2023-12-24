from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/webhook', methods=['POST'])
def webhook():
    # Extract the incoming message data from Twilio
    data = request.form
    user_message = data.get('Body', '').strip()

    # TODO: Implement the logic to interact with the OpenAI language model
    # You can use the OpenAI API to generate responses
    # Replace the following line with your actual implementation
    bot_response = get_bot_response(user_message)

    # Respond to Twilio
    response = {
        "from": "whatsapp:+14155238886",  # Your Twilio WhatsApp number
        "to": "whatsapp:+2349027462016",
        "body": bot_response
    }
    return jsonify(response)

def get_bot_response(user_message):
    # Make a request to OpenAI's GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine
        prompt=user_message,
        max_tokens=150  # Adjust as needed
    )

    # Extract the AI-generated text from the response
    return response['choices'][0]['text']

if __name__ == "__main__":
    app.run(debug=True)
