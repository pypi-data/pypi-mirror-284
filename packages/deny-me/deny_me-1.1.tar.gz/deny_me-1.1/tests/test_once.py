from deny_me.restrict import once

def test_once():
    class abc:
        def __init__(self):
            pass

        # define a function with @once decorator.
        @once
        def function(self, a: str):
            return a
    
    a = abc()
        
    # call the function once
    assert a.function("a") == "a"

    # check for twice
    check = False

    try:
        value = a.function("abc")
    except Exception:
        check = True
    
    assert check == True