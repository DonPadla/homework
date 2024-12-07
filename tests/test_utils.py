from src.utils import get_open_operation_file


def test_get_open_operation_file(data_from_oprations):
    file = "/home/don_padla/PycharmProjects/project_for_bank_1.2/data/operations.json"
    assert get_open_operation_file(file) == data_from_oprations


def test_error_open_operations_file():
    file = "/test_error/not_found"
    assert get_open_operation_file(file) == []
    assert get_open_operation_file(None) == []
