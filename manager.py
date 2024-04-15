from functions import *
import time


def load_new_thing(index=None):
    name = input(' > Name: ')
    description = input(' > Description: ')
    bgcolor = input(' > Background color: ')
    border_col = input(' > Border_color: ')
    img_name = input(' > Image_name: ')
    hreef = '/' + str(len(get_data()))
    print('>>> In progress...', end=' ')
    new_lst = {"name": name,
               "description": description,
               "bgcolor": bgcolor,
               "border_col": border_col,
               "img_name": img_name,
               "hreef": hreef}
    try:
        that_lst = get_data(indx=index)
        for i in that_lst.keys():
            if new_lst[i] == '':
                new_lst[i] = that_lst[i]
    except:
        print()
        time.sleep(0.5)
        print('>>> Previous data not found- saving new...')
    for i in range(100):
        print('-', end='');
        time.sleep(0.01)
    return new_lst

print()
command = input(">>> Input a command: ")
while command:
    if command.lower() in 'add new'.split():
        add_data(load_new_thing())
        print(">>> Successfully added new thing to the database")
    elif command.lower() in "rem del remove delete".split():
        indx = int(input(" > Index of removing row (it MUST be in type int64): "))
        remove_data(indx=indx)
        for i in range(100):
            print('-', end=''); time.sleep(0.005)
        print(">>> Successfully deleted row", indx, "from the database")
    elif command.lower() in "see all show".split():
        data = get_data()
        for i in data:
            for k, v in i.items():
                print("    ", k, ":", v)
                time.sleep(0.04)
            print()
            time.sleep(1/len(data))
    elif command.lower() in 'update upd'.split():
        indeX = int(input(" > Index of data that will be updated: "))
        update_data(indeX, load_new_thing(indeX))
        print(">>> Data in dataframe", indeX, "was updated successfully")
    elif command.lower() == "close":
        print("closing database manager...")
        break
    else:
        print()
        print('     function output is: TыChoDolbaebError')
        print()
        time.sleep(2)
    command = input(">>> Input a command: ")
