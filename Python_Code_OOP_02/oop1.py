
class Phone:
    def call(self):
        print('Any Phone You can easily call')
    def message(self):
        print('Any Phone You can easily send message')

class iPhone(Phone):
    def confiq_sys(self):
        print('iPhone Configaration system is best')

    def Photo_quaility(self):
        print('iPhone Photo quaility is best')


class Samsung(Phone):
    def confiq_sys(self):
        print('Samsung Configaration system is so so good')

    def Photo_quaility(self):
        print('Samsung Photo quaility is so so good')

class OPPO(Phone):
    def confiq_sys(self):
        print('OPPO Configaration system is  good')

    def Photo_quaility(self):
        print('OPPO Photo quaility is good')


ip=iPhone()
ip.call()
ip.message()
ip.confiq_sys()
ip.Photo_quaility()
