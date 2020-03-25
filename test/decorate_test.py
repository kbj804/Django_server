import datetime

# def datetime_decorator(func):
#         def decorated():
#                 print(datetime.datetime.now())
#                 func()
#                 print(datetime.datetime.now())
#         return decorated


# @datetime_decorator
# def main_function_4():
#         print("MAIN FUNCTION 1 START")


# @datetime_decorator
# def main_function_5():
#         print("MAIN FUNCTION 2 START")


# @datetime_decorator
# def main_function_6():
#         print("MAIN FUNCTION 3 START")


class DatetimeDecorator:
    def __init__(self, f):
            self.func = f

    def __call__(self, *args, **kwargs):
            print(datetime.datetime.now())
            self.func(*args, **kwargs)
            print(datetime.datetime.now())


class MainClass:
    
    @DatetimeDecorator
    def main_function_1():
        print("MAIN FUNCTION 1 START")


    @DatetimeDecorator
    def __main_function_2():
        print("MAIN FUNCTION 2 START")


    @DatetimeDecorator
    def __main_function_3():
        print("MAIN FUNCTION 3 START")



my = MainClass()
my.main_function_1()
my._MainClass__main_function_2()
my._MainClass__main_function_3()


