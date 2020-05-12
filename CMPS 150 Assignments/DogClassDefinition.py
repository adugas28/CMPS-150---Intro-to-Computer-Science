class Dog ():
    def __init__(self, inName, inServ, inDays):
        # inServ = Boarding ($40 per day)
        # inServ = Grooming ($25 --> days set to 1)
        # inServ = Daycare ($16 per day)
        self.__name = inName
        self.__service = inServ
        self.__days = inDays

        if inServ == 'Boarding':
            self.__rate = 40
        elif inServ == 'Grooming':
            self.__rate = 25
        else:
            self.__rate = 16

    def GetName (self):
        return self.__name        

    def GetService (self):
        return self.__service

    def GetRate (self):
        return self.__rate

    def GetDays (self):
        return self.__days

    def GetBalance (self):
        return self.__rate * self.__days

