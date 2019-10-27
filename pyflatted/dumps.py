import json
import copy
import collections.abc

def dumps(value, indent=4):
    def fn_set(known, input, value):
        input.append(value)
        index = str(len(input) - 1)
        _id = value if isinstance(value, collections.abc.Hashable) else id(value)
        known[_id] = index
        return str(index)

    def replace(value, first_run, known, input):
        if not first_run[0]:
            first_run[0] = not first_run[0]
            return value
        if isinstance(value, dict) or isinstance(value, list):
            potential = known.get(id(value), None)
            if potential == None:
                return fn_set(known, input, value)
            return str(potential)
        if isinstance(value, str):
            potential = known.get(value, None)
            if potential == None:
                return fn_set(known, input, value)
            return known.get(value, None)
        return value


    def iterate(obj, replacer, first_run, known, input, visited = {}):
        if visited.get(id(obj), False):
            return obj
        visited[id(obj)] = True
        if isinstance(obj, dict):
            new_dict = {}
            for (key, value) in obj.items():
                new_dict[key] = replacer(value, first_run, known, input)
            visited[id(new_dict)] = True
            return new_dict
        elif isinstance(obj, list):
            new_arr = []
            for value in obj:
                replaced = replacer(value, first_run, known, input)
                new_arr.append(replaced)
            visited[id(new_arr)] = True
            return new_arr
        return obj

    first_run = [False]
    known = {}
    input = []
    output = []

    i = int(fn_set(known, input, value))

    
    while i < len(input):
        first_run[0] = True
        input_processed = iterate(input[i], replace, first_run, known, input)
        output.append(json.dumps(input_processed, indent=indent))
        i += 1

    return "[{0}]".format(','.join(output))
