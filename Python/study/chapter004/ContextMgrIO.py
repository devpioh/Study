class ContextTest:
    def __init__(self, path):
        print("open path : {0}".format(path))
        self.file = None
        self.path = path

    def __enter__(self):
        print("enter()!!")
        self.file = open(self.path, 'r')
        return self.file

    def __exit__(self, ext, exv, trb):
        print("exit()")
        print("parameters {0}, {1}, {2}".format(ext, exv, trb))
        if None != self.file:
            self.file.close()
            return True
        else:
            print( "failed file close" ) 
            return False


with ContextTest("hello.txt") as file:
    strTemp = file.read()
    print(strTemp)
