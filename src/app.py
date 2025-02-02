##### ref: https://github.com/TatchNicolas/sls-mangum-fastapi/blob/master/exam_results/main.py
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

##errorssssss
#####testsss
app = FastAPI()


class HelloParam(BaseModel):
    name: str


@app.get("/hello")
def get_hello(name: str = None):
    print("test")
    """
    getで返事するsssssssssssssssssssssssssssssssssssssssssssssssssssss
    """
    if name:
        message = f"[GET]hello, {name}!"
    else:
        message = f"[GET]hello, visitor!"

    return {"message": message}


@app.post("/hello_post")
def post_hello(param: HelloParam):
    """
    postで返事するss
    """
    if param.name:
        message = f"[POST]hello, {param.name}!"
    else:
        message = f"[POST]hello, visitor!"

    return {"message": message}


handler = Mangum(app)
