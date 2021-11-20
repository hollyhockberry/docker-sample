from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from random import randrange

app = FastAPI(openapi_url="/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
def read_root():
  series = [ '', 'Stars', 'Friends', 'On parade', 'planet']
  return {"Message": f'Aikatsu {series[randrange(len(series))]}!'}


if __name__ == '__main__':
  import uvicorn
  uvicorn.run('main:app', host='0.0.0.0', port=80, reload=True)
