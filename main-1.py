from flask import Flask
app = Flask(__name__)

@app.route("/")
def my_flask_test():
    html = """
    <h1>Тестовый запуск локального сервера</h1>
    <p>Это простая веб-страница</p>
    """
    return html

if __name__ == "__main__":
    app.run()
