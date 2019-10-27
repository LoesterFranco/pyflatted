import pyflatted

a = [{"one": 1}, {"two": '2'}]
a[0]["a"] = a

print(pyflatted.dumps(a))