from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.vehicles import vehicle

app = FastAPI()

def cors_headers(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
        )
    return app

app.include_router(vehicle)

@app.get("/")
def root():
    return {"message": "Smart-city Vehicle","Authors":"AI Vision Intern Widya Robotics"}

# @app.get("/")
# def read_smthing():
#     return {"message":"Hello World!"}