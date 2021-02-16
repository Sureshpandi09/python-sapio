# Creating multiple instances for a class.
class Books:
    format = 'hard-copy'
    category = ''

    def __init__(self, type):
        self.category = type
        print(f'This is {self.category} type.')


    @staticmethod
    def buy():
        choice = input('You wanna buy?')
        if choice.lower() == 'y':
            print('Its Rs.50')
        else:
            print('Thank you!!!')


obj = Books('Finance')
obj.buy()
