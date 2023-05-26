
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    '''
    This is a first docstring.
    '''
    return {'message': 'Hello, stranger'}

@app.get('/{name}')
def get_name(name: str):
    '''
    This is a second docstring.
    '''
    return {'message': f'Hello, {name}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
