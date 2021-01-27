# simple function

def greeting():
    def morning():
        print("Good morning ma'am")
    return morning()

def greeting2(item):
    return item


def afternoon():
        print("Good afternoon sir")


#greeting("Good morning")

greeting = greeting()
greeting1 = greeting2(afternoon())

#another instance

def assemble(item):
    def status():
        print("The items have been coupled.")
        item()
    return status


@assemble
def dispatch():
    print("The items have been dispatched.")

#dispatch1 = assemble(dispatch)
#dispatch1()



def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0 or a == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(2,5)
divide(2,0)
