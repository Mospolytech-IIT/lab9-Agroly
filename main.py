from fastapi import FastAPI, Depends, HTTPException, Request,Form
from sqlalchemy.orm import Session
from db import engine, Base, get_db
from models import User, Post
from CRUD import create_user, get_users, create_post, get_posts, update_user, delete_user, update_post, delete_post, \
    get_user, get_post
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()


templates = Jinja2Templates(directory="templates")


# Главная страница со списком пользователей
@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    users = get_users(db)
    return templates.TemplateResponse("index.html", {"request": request, "users": users})


# Страница с постами пользователя
@app.get("/posts/{user_id}", response_class=HTMLResponse)
def post_list(request: Request, user_id: int, db: Session = Depends(get_db)):
    posts = get_posts(db)
    return templates.TemplateResponse("post_list.html", {"request": request, "posts": posts, "user_id": user_id})


# Страница создания нового пользователя
@app.get("/create_user", response_class=HTMLResponse)
def create_user_page(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})


@app.post("/create_user")
def create_user_action(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = create_user(db, username, email, password)
    return {"message": "User created successfully!"}



# Страница создания нового поста
@app.get("/create_post/{user_id}", response_class=HTMLResponse)
def create_post_page(request: Request, user_id: int):
    return templates.TemplateResponse("create_post.html", {"request": request, "user_id": user_id})


@app.post("/create_post/{user_id}")
def create_post_action(
    user_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    post = create_post(db, title, content, user_id)
    return {"message": "Post created successfully!"}


# Страница редактирования пользователя
@app.get("/edit_user/{user_id}", response_class=HTMLResponse)
def edit_user_page(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})


@app.post("/edit_user/{user_id}")
def edit_user_action(
    user_id: int,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = update_user(db, user_id, email, password)
    if user:
        return {"message": "User updated successfully!"}
    raise HTTPException(status_code=404, detail="User not found")



# Страница редактирования поста
@app.get("/edit_post/{post_id}", response_class=HTMLResponse)
def edit_post_page(request: Request, post_id: int, db: Session = Depends(get_db)):
    post = get_post(db, post_id)
    return templates.TemplateResponse("edit_post.html", {"request": request, "post": post})


@app.post("/edit_post/{post_id}")
def edit_post_action(
    post_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    post = update_post(db, post_id, title, content)
    if post:
        return {"message": "Post updated successfully!"}
    raise HTTPException(status_code=404, detail="Post not found")



# Удаление пользователя
@app.post("/delete_user/{user_id}")
def delete_user_action(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if user:
        return {"message": "User deleted successfully!"}
    raise HTTPException(status_code=404, detail="User not found")


# Удаление поста
@app.post("/delete_post/{post_id}")
def delete_post_action(post_id: int, db: Session = Depends(get_db)):
    post = delete_post(db, post_id)
    if post:
        return {"message": "Post deleted successfully!"}
    raise HTTPException(status_code=404, detail="Post not found")
