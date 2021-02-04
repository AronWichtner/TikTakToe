class Player:
    sign: str
    name: str

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name


class ActivePlayer:
    sign: str
    name: str

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name


class Winner:
    sign: str
    name: str
    status: bool
    tempwin: bool

    def __init__(self, status):
        self.status = status
        self.tempwin = False


