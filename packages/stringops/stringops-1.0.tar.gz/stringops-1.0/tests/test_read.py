from stringops.read import Read

def test_there():
    a = Read("abc")
    assert a.there("a") == True
    assert a.there("ab") == True