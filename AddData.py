from db import get_db
from models import User, Post


def add_users(db):
    users = [
        User(username="user1", email="user1@example.com", password="password1"),
        User(username="user2", email="user2@example.com", password="password12"),
        User(username="user3", email="user3@example.com", password="password123")
    ]
    db.add_all(users)
    db.commit()


def add_posts(db):
    posts = [
        Post(title="Post 1", content="Content of post 1", user_id=1),
        Post(title="Post 2", content="Content of post 2", user_id=2),
        Post(title="Post 3", content="Content of post 3", user_id=1)
    ]
    db.add_all(posts)
    db.commit()


def main():
    db = next(get_db())
    add_users(db)
    add_posts(db)
    print("Users and Posts have been added.")


if __name__ == "__main__":
    main()
