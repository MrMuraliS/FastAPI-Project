from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return {"message": "Hello World"}


@app.get('/blog/')
def blog(limit: int = 10, unpublished: bool = True):
    if unpublished:
        return f"{limit} unpublished posts"
    else:
        return f"{limit} published posts"


@app.get('/blog/unpublished/{count}/{num}')
def unpub(count: int, num: int = 7, temp: str = 'ignore'):
    return f"Unpublished list goes here {count} and {temp=}"


@app.get('/blog/{id}/comments')
def comment(id: int):
    return {"blog_id": id, "Comment": "This is a new comment for this"}


@app.get('/app/{id}')
def application(id):
    return {'ID': id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False


@app.post('/CreateBlog')
def create_blog(data: Blog):
    return f"The blog is created with the title {data.title}"
