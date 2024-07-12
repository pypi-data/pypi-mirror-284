from deny_me.restrict import twice

def test_twice():

    class abs:
        def __init__(self):
            pass

        # define a function with @twice decorator
        @twice
        def function(self, x: str):
            return x
    
    a = abs()

    # call once
    assert a.function("abc") == "abc"

    # call twice
    assert a.function("abcd") == "abcd"

    # check for error
    check = False

    try:
        value = a.function("xyz")
    except Exception:
        check = True
    
    assert check == True