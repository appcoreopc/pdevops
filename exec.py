from tasks import execute
from model.commandtype import CommandType
import json
from typing import List

cmd1 = CommandType("list", "ls", "al")
cmd2 = CommandType("list", "pwd", "")
cmd3 = CommandType("list", "ping", "www.google.com")

cmds = List[CommandType]
cmds = [cmd1, cmd2, cmd3]

a = json.dumps(cmds, default=lambda o: o.__dict__)
print(a)

result = execute.delay(a)

def on_raw_message(body):
    print(body)

result.get(on_message=on_raw_message, propagate=False)


#print(result.ready())

# for r in result.collect():
#     print("state")
#     print(r.state)