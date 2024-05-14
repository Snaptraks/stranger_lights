import os
import re
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
MESSAGE_FILE = Path(__file__).parent / "messages/messages.txt"


def save_message_to_file(message: str) -> None:
    with open(MESSAGE_FILE, "a") as f:
        f.write(f"{message}\n")


@app.route("/")
def send_message():
    return render_template("message_form.html")


@app.route("/", methods=["POST"])
def send_message_post():
    text = request.form["message"]
    if text:
        # remove non-letter characters
        processed_text = re.sub(r"[^a-z-A-Z ]+", "", text)
        save_message_to_file(processed_text)
        flash("Message sent!")

    return redirect(url_for("send_message"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
