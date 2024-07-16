from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Това ще разреши CORS за всички маршрути

POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
]

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
