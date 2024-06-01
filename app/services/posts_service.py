# from app.models.posts_model import Post
# from app import db

# def create_post(title, content, user_id):
#     post = Post(title=title, content=content, user_id=user_id)
#     db.session.add(post)
#     db.session.commit()
#     return post

# def get_posts_by_user_id(user_id):
#     return Post.query.filter_by(user_id=user_id).all()
