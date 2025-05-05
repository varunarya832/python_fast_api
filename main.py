from fastapi import FastAPI
from level_1 import router as level_1_router
from level_2 import router as level_2_router

app = FastAPI()


app.include_router(level_1_router, prefix="/level_1", tags=["level_1"])
app.include_router(level_2_router, prefix="/level_2", tags=["level_2"])

@app.get("/")
def read_root():
    return {"message": "MAIN_API"}