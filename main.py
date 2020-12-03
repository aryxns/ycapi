from fastapi import FastAPI, Depends, Response, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import api
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Search(BaseModel):
    search: str

app = FastAPI()
hn = api.HackerNews()

origins = [
    "https://netlify.app",
    "http://netlify.app",
    "http://ycjobs.netlify.app",
    "https://ycjobs.netlify.app/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/posts")
def posts():
    newlist = []
    for post in hn.jobs(limit=10):
        answer = {
			"title": post.title,
			"link": post.link,
			"content": post.content
		}
        newlist.append(answer)
    json_compatible_item_data = jsonable_encoder(newlist)
    return JSONResponse(json_compatible_item_data)

@app.post("/posts")
def search(item: Search):
    newlist = []
    role = item.search
    for post in hn.jobs():
        if str(role) in str(post.title):
            result = {
                "title": post.title, 
				"link" : post.link,
				"content" : post.content
            }
            newlist.append(result)
    json_compatible_item_data = jsonable_encoder(newlist)
    return JSONResponse(json_compatible_item_data) 