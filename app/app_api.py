from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World !!!"}

# uvicorn app_api:app --reload

# 1. User shall be able to see a list of all rooms
@app.get("/rooms")
async def get_rooms():
    return {"rooms": ["Room 1", "Room 2", "Room 3"]}

# 2. User shall be able to create a room
@app.post("/create_room")
async def create_room(room_id: str):
    return {"message": f"Room <{room_id}> created successfully"}

# 3. User shall be able to join a room
@app.post("/join_room")
async def join_room(room_id: str):
    return {"message": f"Room <{room_id}> joined successfully"}