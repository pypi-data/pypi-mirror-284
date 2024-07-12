from deny_me.password import Password, PasswordError, ProtectedError

def test_pass():

    class abc:
        def __init__(self):
            pass

        # define a function with pass
        @Password("pass123").protected
        def function(self, *args, **kwargs):
            return "working"
    
    a = abc()

    # call it with pass
    assert a.function(password="pass123") == "working"

    # call it with wrong pass
    check = False

    try:
        value = a.function(password="hehe")
    except PasswordError:
        check = True
    
    assert check == True

    # call it without password
    check = False
    try:
        value = a.function()
    except ProtectedError:
        check = True
    
    assert check == True