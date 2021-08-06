import pickle
import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.post('/model', status_code=200)
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int, Message: str):
    with open('model/Titanic.pkl', 'rb') as fid: 

        titanic = pickle.load(fid)
        survived = titanic.predict([[Sex, Age, Lifeboat, Pclass]])[0]

        if survived == 1:
            survived = True
        else:
            survived = False

    return  {
            'survived': survived,
            'status': 200,
            'message': Message
            }


@app.get('/model/')
def get():
    return {'hello':'world'}

if __name__ == '__main__':
    uvicorn.run(app, port=80, host="0.0.0.0")

