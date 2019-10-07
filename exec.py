from tasks import add

result = add.delay(4, 4)
print(dir(result))
print("state")
#print(result.ready())

# for r in result.collect():
#     print("state")
#     print(r.state)