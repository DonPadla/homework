from src.decorators import log


def test_log_captured(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function is working\n"


def test_failed_log(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == 'my_function have "division by zero" with arguments: (2, 0), {}\n'
