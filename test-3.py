from flask import Flask
app = Flask(__name__)

@app.route("/")
def my_html_page():
    html = """
    <h2>Добро пожаловать, мой друг!</h2>
    <p>Место для текста</p>
    """
    return html

if __name__ == "__main__":
    app.run()