def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    speakers = [f"Hello, my name is {name}." for name in names]
    return speakers

def assign_rooms(names):
    welcomelist = [f"Hello, {name}! You'll be assigned to room {index}!" for index, name in enumerate(names, start = 1)]
    return welcomelist

def printer(names):
    for item in batch_badge_creator(names):
        print(item)

    for item in assign_rooms(names):
        print(item)

