import datetime


def log(stuff):
    print(datetime.datetime.now())
    if isinstance(stuff, int) or isinstance(stuff, float):
        print(stuff)
    else:
        for thing in stuff:
            print(thing)
    print("-----")
