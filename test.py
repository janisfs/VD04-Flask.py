from flask import Flask
app = Flask(__name__)

@app.route("/")
def privet_mir():
    return "Hello, My World!"

@app.route("/new/")
@app.route("/newpage/")
@app.route("/новая страница/")
def my_new():
    return "Hello, My new page!"

if __name__ == "__main__":
    app.run()
