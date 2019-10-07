from tasks import add

result = add.delay(4, 4)
#print(dir(result))
#print("state", result.ready())

def on_raw_message(body):
    print(body)
    
print(result.get(on_message=on_raw_message, propagate=False))


#print(result.ready())

# for r in result.collect():
#     print("state")
#     print(r.state)