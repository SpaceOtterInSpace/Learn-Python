#dict = {'foo':foo, 'bar':bar, 'baz':baz}

def foo():
    print "Test string"

def bar():
    return True

def baz(x):
    return x

dict = {'foo':foo, 'bar':bar, 'baz':baz(420)}

#dict['foo']()
#dict['bar']()
x = dict['baz']()

print x