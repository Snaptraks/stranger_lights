import re

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def send_message():
    return render_template("message_form.html")


@app.route("/", methods=["POST"])
def send_message_post():
    text = request.form["message"]
    if text:
        processed_text = re.sub(r"[^a-z-A-Z ]+", "", text)
        print(processed_text)
    return redirect(url_for("send_message"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
