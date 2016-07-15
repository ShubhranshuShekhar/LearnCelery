import pprint
from tasks import add

def show():
    print "Hello"
print add.name
# result = add.delay(2,2)
result = add.apply_async((12, 3), countdown=23, link=show())
# result.get()
print (result)

