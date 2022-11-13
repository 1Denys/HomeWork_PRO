class MyExeption(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def error_message(self):
        return self.message

while True:
    try:
        cost = float(input('Enter price: '))
        if cost < 0:
            raise MyExeption('The number must be positive')
        print('Price: ', cost)
        break
    except ValueError as error:
        print('Price need to consist of digit')
    except MyExeption as error:
        print(error.error_message())

