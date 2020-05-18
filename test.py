import pyflatted

a = [{"one": 1}, {"two": '2'}]
a[0]["a"] = a               # [{'one': 1, 'a': [...]}, {'two': '2'}]
print(a)
flatted = pyflatted.dumps(a)
print(flatted)              # [["1", "2"], {"one": 1, "a": "0"}, {"two": "3"}, "2"]
unflatted = pyflatted.loads(flatted)
print(unflatted)            # [{'one': 1, 'a': [...]}, {'two': '2'}]
print(unflatted[0]["a"])    # [{'one': 1, 'a': [...]}, {'two': '2'}]