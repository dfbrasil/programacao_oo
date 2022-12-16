class Duck:

    def swim(self):
        print ('swimming')

    def fly(self):
        print('flying')

class whale:

    def swim(self):
        print('swimming')

for animal in [Duck(), whale()]:
    animal.swim()
    animal.fly()