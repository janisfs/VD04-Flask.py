from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/<password>/")
def hello_world(password=None):
    if password == "12345":
        return f"Добро пожаловать, мой друг!"
    else:
        return f"Неверный пароль!"

if __name__ == "__main__":
    app.run()