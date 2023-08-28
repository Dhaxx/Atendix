from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=879)