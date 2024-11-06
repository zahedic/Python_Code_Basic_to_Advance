class Phone:
    def __init__(self):
        print('It is Phone class')

class Samsung(Phone):
    def __init__(self):
        super().__init__()
        print('It is Samsung class')




s1=Samsung()