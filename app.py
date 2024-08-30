from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Запрос случайной цитаты из API
    response = requests.get('https://api.quotable.io/random')
    quote_data = response.json()
    quote = quote_data['content']
    author = quote_data['author']

    return render_template('index.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)