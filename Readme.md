# pyflatted
A (partial) port of [flatted](https://github.com/WebReflection/flatted) to Python 3, which allows for dumping and parsing circular or otherwise recursive JSON-compatible structures.

This was done mainly so circular JSON data can be communicated between Python and Node for one of our earlier projects.

# How does it work?
While dumping the string, all objects, including dictionaries, lists, and strings, are flattened out and replaced as unique index.

```python
import pyflatted

a = [{"one": 1}, {"two": '2'}]
a[0]["a"] = a       # [{'one': 1, 'a': [...]}, {'two': '2'}]
print(a)
flatted = pyflatted.dumps(a)
print(flatted)      # [["1", "2"], {"one": 1, "a": "0"}, {"two": "3"}, "2"]
unflatted = pyflatted.loads(flatted)
print(unflatted)    # [{'one': 1, 'a': [...]}, {'two': '2'}]
```

# Current state of feature parity with flatted
What works:
* dumps (with Python json.dumps options passed through, incl. indent and others)
* loads

What we want to support:
* Custom replacers and replacers for dumping and parsing respectively

What we don't want to support:
* Alternative primitives

Contributions are very welcome.

# License
The MIT License. See 'License'.

# Open Source Acknowledgement
Copyright (c) 2018, Andrea Giammarchi, @WebReflection

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.