import os
import json
from datetime import datetime


MEMORY = "vider_v7_memory.json"


# =========================
# MEMORY
# =========================

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



def remember(task,result):

    data = load_memory()

    data.append({

        "time":
        str(datetime.now()),

        "task":
        task,

        "result":
        result
    })

    save_memory(data)



# =========================
# CODE READER
# =========================

def read_project():

    files=[]

    for root,dirs,names in os.walk("."):

        for name in names:

            if name.endswith(".py"):

                files.append(
                    os.path.join(
                        root,
                        name
                    )
                )

    return files



# =========================
# CODE BUILDER
# =========================

def create_module(name):

    filename=name+".py"

    code=f"""

# Created by VIDER v7

def run():

    print(
        "Module {name} running"
    )

"""

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)


    return filename



# =========================
# TESTER
# =========================

def check():

    files=read_project()

    return {

        "python_files":
        files,

        "count":
        len(files)

    }



# =========================
# VIDER AGENT
# =========================

print("""
====================
 VIDER v7 ONLINE
====================
""")


while True:

    cmd=input(
        "\nVIDER > "
    )


    if cmd=="exit":

        break


    if cmd=="scan":

        result=check()


    else:

        module=create_module(
            "vider_module"
        )

        result={

            "created":
            module,

            "scan":
            check()

        }


    remember(
        cmd,
        result
    )


    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=4
        )
    )
