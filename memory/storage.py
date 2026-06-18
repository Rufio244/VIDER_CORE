{
    "knowledge": [],
    "projects": []
}
import json


FILE="memory.json"


def save(topic,data):

    with open(FILE,"r",encoding="utf-8") as f:
        mem=json.load(f)


    mem["knowledge"].append(
        {
            "topic":topic,
            "data":data
        }
    )


    with open(FILE,"w",encoding="utf-8") as f:
        json.dump(
            mem,
            f,
            ensure_ascii=False,
            indent=4
        )
