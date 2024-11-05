class phone:
    def call(self):
        print("i am callig in phone class")
    def messege(self):
        print("i am messegeing in phone class")

class iphone(phone):
    def config_sys(self):
        print("iphone config_system is so good")

class samsung(phone):
    def photo(self):
        print("i like samsung photo quality")


s=samsung()
s.call()
s.messege()
s.photo()