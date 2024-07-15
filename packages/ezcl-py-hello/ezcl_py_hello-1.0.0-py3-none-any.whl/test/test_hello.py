from hello import (
    hello,
    hello_world,
    hi,
    hi_world
)

def test_hello(name):
    assert hello(name) == f"Hello, {name}!"
    print("Test passed!")

def test_hello_world():
    assert hello_world() == "Hello, World!"
    print("Test passed!")

def test_hi(name):
    assert hi(name) == f"Hi, {name}"
    print("Test passed!")

def test_hi_world():
    assert hi_world() == "Hi, World!"
    print("Test passed!")

if __name__ == "__main__":
    name = "Eazy Cloud Life"
    
    test_hello(name)
    test_hello_world()
    test_hi(name)
    test_hi_world()
