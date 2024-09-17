class Programmer:
    def make(self):
        print('I am a programmer, I make software.')

class Seller:
    def make(self):
        print('I am a seller, I sell software.')

class RH:
    def make(self):
        print('I am a RH, I hire people.')

class Company:
    def do_work(self, worker):
        worker.make()

company = Company()
company.do_work(Programmer())
company.do_work(Seller())
company.do_work(RH())