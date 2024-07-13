from deny_me.restrict import Allow

def test_custom():

    class abc:
        def __init__(self) -> None:
            pass

        @Allow(3).times
        def function(self, a: str):
            return a
    
    a = abc()
    # run once
    assert a.function("abc") == "abc"
    # run twice
    assert a.function("abc") == "abc"
    # run thrice
    assert a.function("abc") == "abc"

    # run fourth time - error
    check = False

    try:
        value = a.function("abc")
    except Exception:
        check = True
    
    assert check == True