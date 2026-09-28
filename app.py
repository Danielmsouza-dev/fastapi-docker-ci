from fastapi import FastAPI


app = FastAPI(title="FastAPI Docker CI")


@app.get("/health")
def health_check():
    return {"status": "ok"}
