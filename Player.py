class Player:
    sign: str
    name: str

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name


class ActivePlayer:
    sign: str
    contrary_sign: str
    name: str

    def __init__(self, sign, name, cont_sign):
        self.sign = sign
        self.name = name
        self.contrary_sign = cont_sign


class Winner:
    sign: str
    name: str


