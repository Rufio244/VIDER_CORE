import os
import json
import time
from datetime import datetime


MEMORY = "vider_v8_memory.json"


# =====================
# MEMORY
# =====================

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



def remember(event,data):

    mem=load_memory()

    mem.append({

        "time":
        str(datetime.now()),

        "event":
        event,

        "data":
        data

    })

    save_memory(mem)



# =====================
# GITHUB CONNECTOR
# =====================

def github_check():

    if os.path.exists(".git"):

        return "Git repository detected"

    return "No git repository"



# =====================
# API CONNECTOR
# =====================

def api_connector():

    return {

        "network":
        "ready",

        "tools":
        [
            "API",
            "Webhook"
        ]

    }



# =====================
# TASK SYSTEM
# =====================

tasks=[]


def add_task(task):

    tasks.append({

        "task":task,

        "time":
        str(datetime.now())

    })



def run_tasks():

    results=[]

    for t in tasks:

        results.append(
            "completed: "+t["task"]
        )

    tasks.clear()

    return results



# =====================
# VIDER BODY
# =====================

print("""
====================
 VIDER v8 ONLINE
====================
""")


while True:


    cmd=input(
        "\nVIDER > "
    )


    if cmd=="exit":

        break



    if cmd=="status":

        result={

            "github":
            github_check(),

            "api":
            api_connector(),

            "tasks":
            len(tasks)

        }



    elif cmd.startswith("task "):

        task=cmd.replace(
            "task ",
            ""
        )

        add_task(task)

        result="Task added"



    elif cmd=="run":

        result=run_tasks()



    else:

        result="Unknown command"



    remember(
        cmd,
        result
    )


    print(result)
