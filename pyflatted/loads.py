import json
import copy
import collections.abc

class StringWrapper:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return "[String: '{}']".format(self.string)

def loads(string):
    def revive(input, parsed, output):
        keys = range(0, len(output)) if type(output) == list else output.keys()
        for key in keys:
            value = output[key]
            if (type(value) == StringWrapper):
                tmp = input[int(value.string)]
                if type(tmp) == dict and not id(tmp) in parsed:
                    parsed.add(id(tmp))
                    output[key] = revive(input, parsed, tmp)
                else:
                    output[key] = tmp
            else:
                output[key] = value
        return output

    def wrap_strings(value):
        if type(value) == list:
            returnable = []
            for element in value:
                returnable.append(wrap_strings(element))
            return returnable
        if type(value) == dict:
            returnable = {}
            for key in value.keys():
                returnable[key] = wrap_strings(value[key])
            return returnable
        if type(value) == str:
            return StringWrapper(value)
        return value
                
    initial = json.loads(string)
    processed = wrap_strings(initial)
    input = list(map(lambda el: el.string if type(el) == StringWrapper else el, processed)) # Unwrap top level
    value = input[0]
    return value if type(value) == object else revive(
        input,
        set(),
        value
    )
