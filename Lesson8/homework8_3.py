import json


dict_ = {
    '111111': ('Jonn', 26),
    '222222': ('Sam', 19),
    '333333': ('Alex', 22),
    '444444': ('Alice', 17),
    '555555': ('Maria', 20),
    '666666': ('Emily', 24)
}

with open(
    "json_file.json",
    mode="w"
) as file:
    json.dump(dict_, file, indent=4)
