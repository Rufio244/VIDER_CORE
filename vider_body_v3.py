from fastapi import FastAPI
import uvicorn
import json
import os
from datetime import datetime


app = FastAPI()

MEMORY = "vider_memory.json"


# ======================
# MEMORY
# ======================

def load_memory():

    if not os.path.exists(MEMORY):

        return []

    with open(
        MEMORY,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_memory(data):

    with open(
        MEMORY,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def remember(command,result):

    data = load_memory()

    data.append({

        "time":
        str(datetime.now()),

        "command":
        command,

        "result":
        result

    })


    save_memory(data)



# ======================
# CHANI BRAIN
# ======================

def think(command):

    return {

        "analysis":
        "กำลังวิเคราะห์",

        "plan":
        [
            "รับข้อมูล",
            "ประมวลผล",
            "เลือกการกระทำ",
            "บันทึก"
        ]

    }



# ======================
# TOOL SYSTEM
# ======================

def create_file(name):

    with open(
        name,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "# Created by VIDER"
        )


    return name



# ======================
# API BODY
# ======================

@app.get("/")
def status():

    return {

        "system":
        "VIDER BODY v3",

        "status":
        "online"

    }



@app.post("/command")
def command(data:dict):

    text=data["command"]


    brain=think(text)

    file=create_file(
        "vider_output.py"
    )


    result={

        "brain":
        brain,

        "action":
        file

    }


    remember(
        text,
        result
    )


    return result



# ======================
# RUN
# ======================

if __name__=="__main__":

    print(
        "VIDER BODY v3 ONLINE"
    )

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
