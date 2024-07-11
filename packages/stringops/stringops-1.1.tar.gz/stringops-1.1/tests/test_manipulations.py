from stringops.manipulation import Manipulation
from stringops.read import Read

def test_half():
    a = Manipulation("abc")
    assert a.half("left") == "ab"
    assert a.half("right") == "bc"

def test_split():
    a = Manipulation("abc xyz")
    assert len(a.split(" ", "all")) == 2
    assert a.split(" ", 0) == "abc"
    assert a.split(" ", 1) == "xyz"

def test_add():
    a = Manipulation("abc")
    assert a.add("d") == "abcd"

def test_convert_to_read():
    a = Manipulation("abc")
    assert type(a.convert_to_read()) == Read
    assert a.convert_to_read().there("a") == True