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
    import requests

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
    headers = {"Authorization": f"Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": user_message,
    })
    return output[0]['generated_text']

if __name__ == "__main__":
    app.run(debug=True)

