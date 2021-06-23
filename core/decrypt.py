class Rot:
    def __init__(self, string, shift_value) -> None:
        self.string = string
        self.shift_value = shift_value
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.decrypted_txt = ''

    def decryptor(self):
        for i in self.string:
            if i in self.letters:
                if i.isupper():
                    self.decrypted_txt += self.letters[self.letters.index(i) + self.shift_value].capitalize()
                else:
                    self.decrypted_txt += self.letters[self.letters.index(i) + self.shift_value]
            else:
                self.decrypted_txt += i 
        return self.decrypted_txt