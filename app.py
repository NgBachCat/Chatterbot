from flask import Flask, render_template, request, jsonify
import openai 
import os

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "your-openai-api-key-here"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    try:
        message = request.json.get("message")
        if not message:
            return jsonify({"error": "No message provided"}), 400
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )

        response_message = completion.choices[0].message['content']
        return jsonify({"content": response_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
