import datetime


def log(stuff):
    print(datetime.datetime.now())
    if isinstance(stuff, int):
        print(stuff)
    else:
        for thing in stuff:
            print(thing)
    print("-----")