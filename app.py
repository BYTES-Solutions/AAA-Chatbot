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
    
    return user_message

if __name__ == "__main__":
    app.run(debug=True)
