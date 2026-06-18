import os
import json
import subprocess
from datetime import datetime


MEMORY = "vider_v4_memory.json"


# ======================
# MEMORY
# ======================

def load_memory():

    if not os.path.exists(MEMORY):
        return []

    with open(MEMORY,"r",encoding="utf-8") as f:
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



def remember(task,result):

    data=load_memory()

    data.append({

        "time":str(datetime.now()),

        "task":task,

        "result":result

    })

    save_memory(data)



# ======================
# BRAIN
# ======================

def analyze(task):

    return {

        "goal":task,

        "steps":[

            "วิเคราะห์",

            "ออกแบบ",

            "สร้างโค้ด",

            "ทดสอบ"

        ]

    }



# ======================
# CODE AGENT
# ======================

def generate_code(task):

    code=f"""

# VIDER GENERATED CODE

def main():

    print("Task: {task}")


if __name__=="__main__":

    main()

"""

    filename="vider_generated_app.py"


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)


    return filename



# ======================
# TEST AGENT
# ======================

def test_code(file):

    try:

        result=subprocess.run(

            ["python",file],

            capture_output=True,

            text=True

        )


        return {

            "success":
            True,

            "output":
            result.stdout

        }


    except Exception as e:

        return {

            "success":
            False,

            "error":
            str(e)

        }



# ======================
# VIDER LOOP
# ======================

print("""
=====================
 VIDER v4 ONLINE
=====================
""")


while True:


    task=input(
        "\nสั่งงาน > "
    )


    if task=="exit":
        break



    brain=analyze(task)


    file=generate_code(task)


    test=test_code(file)


    result={

        "brain":
        brain,

        "created":
        file,

        "test":
        test

    }


    remember(
        task,
        result
    )


    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=4
        )
    )
