from db import get_db
from models import User, Post

def get_all_users(db):
    users = db.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def get_all_posts(db):
    posts = db.query(Post).join(User).all()
    for post in posts:
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}, Author: {post.author.username}")

def get_posts_by_user(db, user_id):
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    for post in posts:
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")

def main():
    db = next(get_db())
    print("All Users:")
    get_all_users(db)
    print("\nAll Posts:")
    get_all_posts(db)
    print("\nPosts by User with ID 1:")
    get_posts_by_user(db, 1)

if __name__ == "__main__":
    main()
