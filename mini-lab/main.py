from flask import Flask, render_template
from routes import upload_bp

app = Flask(__name__)
app.register_blueprint(upload_bp)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

