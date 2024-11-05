class myEidBuget:
    def __init__(self):
        self.__myBuget=5000

    def displayBuget(self):
        print('Your Buget is:',self.__myBuget)

    def updateBuget(self,buget):
        self.__myBuget=buget

zawad=myEidBuget()
zawad.displayBuget()

zawad.updateBuget(7000)
zawad.displayBuget()




