from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json["message"]
    bot_response = generate_response(user_message)
    return jsonify({"response": bot_response})

def generate_response(user_message):
    import openai
    openai.api_key = "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"
    model = "text-davinci-003"
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=user_message,
            max_tokens=50
        )
        
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't process your request at the moment."
    return user_message




if __name__ == "__main__":
    app.run(debug=True)
