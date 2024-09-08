from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>Тестовый запуск локального сервера</h1>
    <p>А это просто текст</p>
    """
    return html

if __name__ == "__main__":
    app.run()