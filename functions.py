import json

class БлятьТыЧёДаунХареВтиратьДИЧЬ(Exception):
    pass

def write_data(filename='data.json', data=[]):
    with open(filename, 'w') as file: json.dump(data, file)

def get_data(filename='data.json', indx=-999):
    with open(filename) as file:
        if indx == -999: return json.load(file)
        else: return json.load(file)[indx]

def remove_data(filename='data.json', indx=-1):
    try:
        lst = get_data(filename)
        lst.pop(indx)
        with open(filename, 'w') as file: json.dump(lst, file)
        return True
    except: raise БлятьТыЧёДаунХареВтиратьДИЧЬ

def add_data(thing):
    lst = get_data()
    lst.append(thing)
    write_data(data=lst)

def update_data(indx, data):
    try:
        lst = get_data()
        lst[indx] = data
        write_data(data=lst)
        return True
    except: raise БлятьТыЧёДаунХареВтиратьДИЧЬ
