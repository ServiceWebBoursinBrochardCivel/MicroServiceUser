class User:

    def __init__(self, id="", pseudo="", mail="", password=""):
        self.id = id
        self.pseudo = pseudo
        self.mail = mail
        self.password = password

    def getId(self):
        return self.id

    def getPseudo(self):
        return self.pseudo

    def getMail(self):
        return self.mail

    def getPassword(self):
        return self.password