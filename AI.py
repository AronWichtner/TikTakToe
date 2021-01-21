import random

class AI:
    sign: str
    name: str

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name

    def check_if_valid(self, btns):
        possible_buttons = []
        for buttonlist in btns:
            for button in buttonlist:
                if button["text"] == "-":
                    possible_buttons.append(button)
        return possible_buttons

    def setsign(self, buttonlist):
        possible_buttons = self.check_if_valid(buttonlist)
        button = random.choice(possible_buttons)
        button["text"] = self.sign



