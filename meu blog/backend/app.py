# backend/app.py

# edição no github
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, uuid

from models import Post, SessionLocal

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/posts", methods=["POST"])
def create_post():
    session = SessionLocal()

    title = request.form.get("title")
    content = request.form.get("content")
    file = request.files.get("image")

    image_url = None
    if file:
        filename = f"{uuid.uuid4().hex}_{file.filename}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        image_url = f"/static/uploads/{filename}"

    new_post = Post(title=title, content=content, image=image_url)
    session.add(new_post)
    session.commit()

    return jsonify({
        "id": new_post.id,
        "title": new_post.title,
        "content": new_post.content,
        "image": new_post.image
    }), 201

@app.route("/posts", methods=["GET"])
def get_posts():
    session = SessionLocal()
    posts = session.query(Post).all()
    return jsonify([
        {
            "id": p.id,
            "title": p.title,
            "content": p.content,
            "image": p.image
        } for p in posts
    ])

@app.route("/static/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
