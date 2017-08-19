

class isInteger(Exception):

    def __init__(self):
        self.val = "[Setting Error]: This Value Must Be An Integer."

    def __str__(self):
        return self.val


class isRate(Exception):

    def __init__(self):
        self.val = "[Setting Error]: This Value Must Be An Integer."

    def __str__(self):
        return self.val