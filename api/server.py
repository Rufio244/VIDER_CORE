from fastapi import FastAPI
from brain.chani import think
from brain.planner import create_plan
from memory.storage import save


app=FastAPI()


@app.get("/")
def home():

    return {
        "system":"VIDER CORE",
        "status":"online"
    }


@app.post("/command")
def command(data:dict):

    text=data["command"]

    brain=think(text)

    plan=create_plan(text)

    save(
        "command",
        text
    )


    return {
        "brain":brain,
        "plan":plan
    }
