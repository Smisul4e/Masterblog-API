from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаване на CORS за всички маршрути

POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Title and content are required"}), 400

    new_id = max(post['id'] for post in POSTS) + 1
    new_post = {
        "id": new_id,
        "title": data['title'],
        "content": data['content']
    }
    POSTS.append(new_post)

    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global POSTS
    post = next((post for post in POSTS if post['id'] == post_id), None)

    if post is None:
        return jsonify({"error": "Post not found"}), 404

    POSTS = [post for post in POSTS if post['id'] != post_id]

    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post = next((post for post in POSTS if post['id'] == post_id), None)

    if post is None:
        return jsonify({"error": "Post not found"}), 404

    if 'title' in data:
        post['title'] = data['title']
    if 'content' in data:
        post['content'] = data['content']

    return jsonify(post), 200


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title = request.args.get('title')
    content = request.args.get('content')
    results = [post for post in POSTS if
               (title and title.lower() in post['title'].lower()) or
               (content and content.lower() in post['content'].lower())]
    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
