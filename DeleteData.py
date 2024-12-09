from db import get_db
from models import User, Post


def delete_post(db, post_id):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        print(f"Post ID {post_id} deleted.")
    else:
        print(f"Post ID {post_id} not found.")


def delete_user_and_posts(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.query(Post).filter(Post.user_id == user_id).delete()
        db.delete(user)
        db.commit()
        print(f"User ID {user_id} and their posts have been deleted.")
    else:
        print(f"User ID {user_id} not found.")


def main():
    db = next(get_db())
    delete_post(db, 1)
    delete_user_and_posts(db, 2)


if __name__ == "__main__":
    main()
