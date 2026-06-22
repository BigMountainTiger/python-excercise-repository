def base_generator():
    yield "Hello"
    yield "World"


def wrapper_generator():
    yield "Start"
    yield from base_generator()
    yield "End"


for item in wrapper_generator():
    print(item)
