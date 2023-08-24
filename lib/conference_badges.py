def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]  # using list comprehension

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i + 1}!" for i, name in enumerate(names)]

def printer(names):
    all_messages = batch_badge_creator(names) + assign_rooms(names)
    for message in all_messages:
        print(message)
