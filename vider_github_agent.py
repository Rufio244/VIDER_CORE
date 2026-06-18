import os
from github import Github


# รับ Token จาก Environment
TOKEN = os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise Exception("กรุณาตั้งค่า GITHUB_TOKEN")


github = Github(TOKEN)


# ตั้งค่า repo
repo = github.get_repo(
    "Rufio244/VIDER_CORE"
)


def create_file(path, content):

    try:

        old = repo.get_contents(path)

        repo.update_file(
            path,
            "VIDER update file",
            content,
            old.sha
        )

        return "updated"

    except:

        repo.create_file(
            path,
            "VIDER create file",
            content
        )

        return "created"



# ตัวอย่างให้ Vider สร้างโค้ด

code = """

print("Created by VIDER")

"""


result = create_file(
    "generated/test.py",
    code
)


print(result)
