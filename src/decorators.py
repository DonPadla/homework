from functools import wraps


def log(filename=None):
    """ Если "filename" задан логирует в него имя и результат выполнения функции при успешном завершении.
    При возникновении ошибки логирует имя функции, ошибку и входные параметры.
    Если "filename" не задан логи выводятся в консоль. """

    def logging_function(func):
        @wraps(func)
        def wraper(*args, **kwargs):

            try:
                func_call = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f'{wraper.__name__} is working. Result: {func_call}\n')
                else:
                    print(f'{wraper.__name__} is working. Result: {func_call}')

            except Exception as e:
                func_call = None
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f'{wraper.__name__} have "{e}" with arguments: {args}, {kwargs}\n')
                else:
                    print(f'{wraper.__name__} have "{e}" with arguments: {args}, {kwargs}')
            return func_call
        return wraper
    return logging_function
