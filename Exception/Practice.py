class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def printMessage(self):
        print("User defined exception:",self.msg)

if __name__=="__main__":
    try:
        raise Accident("Hello World")
    except Accident as e:
        e.printMessage()