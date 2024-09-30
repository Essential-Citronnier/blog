from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import markdown
from pathlib import Path

app = FastAPI()

# Set up static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Path to the folder where Markdown files are stored
POSTS_PATH = Path("data")

# Modify the get_blog_posts function
def get_blog_posts():
    posts = []
    for markdown_file in POSTS_PATH.glob("**/*.md"):  # Recursive search
        # Extract post id from folder structure and filename
        relative_path = markdown_file.relative_to(POSTS_PATH)
        post_id = str(relative_path).replace("/", "_")  # Keep dots in the filename intact
        title = markdown_file.stem.replace("-", " ").title()
        folder = str(relative_path.parent) if relative_path.parent != Path() else None
        
        posts.append({
            "id": post_id, 
            "title": title,
            "folder": folder  # Add folder info for grouping in the list
        })
    return posts

# Read the content of a specific Markdown file
def get_post_content(post_id):
    # Reconstruct the path while keeping dots in filenames
    post_path = POSTS_PATH / post_id.replace("_", "/")  # Reconstruct path
    post_path = post_path.with_suffix(".md")  # Ensure it has the .md suffix
    
    if post_path.exists():
        with open(post_path, "r", encoding="utf-8") as f:
            return markdown.markdown(f.read())
    return None

@app.get("/")
def read_blog(request: Request):
    posts = get_blog_posts()
    # Group posts by folders
    grouped_posts = {}
    for post in posts:
        folder = post["folder"] or "Root"  # Group posts in "Root" if no folder
        if folder not in grouped_posts:
            grouped_posts[folder] = []
        grouped_posts[folder].append(post)
    
    return templates.TemplateResponse("index.html", {"request": request, "grouped_posts": grouped_posts})

@app.get("/post/{post_id}")
def read_post(request: Request, post_id: str):
    post_content = get_post_content(post_id)
    if post_content is None:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    
    title = post_id.split("_")[-1].replace("-", " ").title()
    return templates.TemplateResponse("post.html", {"request": request, "post_content": post_content, "title": title})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
