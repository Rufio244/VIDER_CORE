import json
import os
from datetime import datetime


MEMORY = "vider_knowledge.json"


# =========================
# KNOWLEDGE MEMORY
# =========================

def load():

    if not os.path.exists(MEMORY):
        return {
            "knowledge": []
        }

    with open(
        MEMORY,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save(data):

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



def learn(topic,info):

    data = load()

    data["knowledge"].append({

        "topic":topic,

        "info":info,

        "time":
        str(datetime.now())

    })

    save(data)



def recall(word):

    data=load()

    result=[]

    for item in data["knowledge"]:

        if word.lower() in str(item).lower():

            result.append(item)


    return result



# =========================
# CHANI REASONING
# =========================

def chani(task):

    old = recall(task)


    return {

        "task":task,

        "memory_found":old,

        "plan":[

            "วิเคราะห์",

            "ค้นความรู้",

            "สร้างคำตอบ",

            "เรียนรู้เพิ่ม"

        ]

    }



# =========================
# AI CONNECTOR PLACEHOLDER
# =========================

def ai_connector(prompt):

    # จุดนี้เอาไว้เชื่อม AI API จริง

    return {

        "response":

        "AI connector พร้อมเชื่อมต่อ"

    }



# =========================
# VIDER LOOP
# =========================

print("""
====================
 VIDER v5 ONLINE
====================
""")


while True:


    command=input(
        "\nVIDER > "
    )


    if command=="exit":

        break


    brain=chani(command)


    ai=ai_connector(command)


    learn(
        command,
        ai
    )


    print(
        json.dumps(
            {
                "brain":brain,
                "ai":ai
            },
            ensure_ascii=False,
            indent=4
        )
    )
