# from flask import Blueprint, request, jsonify
# from app.services.posts_service import create_post, get_posts_by_user_id

# post_bp = Blueprint('post_bp', __name__)

# @post_bp.route('/posts', methods=['POST'])
# def create_post_route():
#     data = request.get_json()
#     title = data.get('title')
#     content = data.get('content')
#     user_id = data.get('user_id')
#     post = create_post(title, content, user_id)
#     return jsonify({"id": post.id, "title": post.title, "content": post.content, "user_id": post.user_id}), 201

# @post_bp.route('/users/<int:user_id>/posts', methods=['GET'])
# def get_posts_by_user_route(user_id):
#     posts = get_posts_by_user_id(user_id)
#     return jsonify([{"id": post.id, "title": post.title, "content": post.content} for post in posts])
