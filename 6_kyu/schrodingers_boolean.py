# Can a value be both True and False?

# Define omnibool so that it returns True for the following:

# omnibool == True and omnibool == False


class Omnibool:
    def __init__(self):
        pass

    def __eq__(self, other):
        return True

omnibool = Omnibool()
