from db import get_db
from models import User, Post


def update_user_email(db, user_id, new_email):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        print(f"User ID {user_id} email updated to {new_email}")
    else:
        print(f"User ID {user_id} not found.")


def update_post_content(db, post_id, new_content):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.content = new_content
        db.commit()
        print(f"Post ID {post_id} content updated.")
    else:
        print(f"Post ID {post_id} not found.")


def main():
    db = next(get_db())
    update_user_email(db, 1, "newemail@example.com")
    update_post_content(db, 1, "Updated content for post 1.")


if __name__ == "__main__":
    main()
