import json
d = {"a": 1}
l = [1,3,4]
t =(3,4)
b = True
s = "Hello word"
st = {1, 2, 'Test'}
none = None
obj = {'tuple': t, 'list': l, 'dict': d, 'bool': b}
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
print(json.dumps(b))


with open('storage.json', "w") as f:
    json.dump(obj,f)