

class isInteger(Exception):

    def __init__(self):
        self.val = "[Setting Error]: This Value Must Be An Integer."

    def __str__(self):
        return self.val


class isRate(Exception):

    def __init__(self):
        self.val = "[Setting Error]: This Value Must Be 0 < Value < 1"

    def __str__(self):
        return self.val


class isBool(Exception):

    def __init__(self):
        self.val = "[Setting Error]: This Value Must Be A Boolean"

    def __str__(self):
        return self.val


class MinimumArgs(Exception):

    def __init__(self):
        self.val = "[Setting Error]: System needs 2 arguments at least"

    def __str__(self):
        return self.val


class isNotEmpty(Exception):

    def __init__(self):
        self.val = "Player Data is NOT EMPTY."

    def __str__(self):
        return self.val
