import sys
def detect():
    global name
    if len(sys.argv) == 1: name = "world"
    else: name = sys.argv[1]
def hello():
    print("Hello", name, "!")
detect()
hello()
