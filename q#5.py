class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        # Get a string from console input
        self.input_string = input("Enter a string: ")

    def printString(self):
        # Print the string in upper case
        print(self.input_string.upper())

# def testStringManipulator():
#     string_manipulator = StringManipulator()

#     string_manipulator.getString()

#     string_manipulator.printString()
# testStringManipulator()
