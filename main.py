from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": }


@app.get("/predict")
def predict(number: int):
    result = 'even' if number % 2 == 0 else 'odd'
    return {"number": number, "result": result }