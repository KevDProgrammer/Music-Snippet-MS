from flask import Flask, render_template, request
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("MusicTester.html")

@app.route("/connect.js")
def connect_js():
    return send_from_directory("templates", "connect.js")

@app.route("/music", methods=["POST"])
def music_manager():
    data = request.get_json() # retireved from connect.js
    action = data["action"]
    title = data["title"]

    with open("request.txt", "w") as f: # return the selected song back
        f.write(f"action={action}\n")
        f.write(f"title={title}")

    return "flask execuded" # confirm it works

if __name__ == "__main__":
    app.run(debug=True)