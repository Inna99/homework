# from pytest_mock import MockerFixture
#
# from homework9.task3 import universal_file_counter
# from pathlib import Path
#
#
# def test_universal_file_counter_three_parameters():
#     cur_dir = Path()
#     assert universal_file_counter(cur_dir, "txt", str.split) == 6
#
#
# def test_universal_file_counter_two_parameters(mocker: MockerFixture) -> None:
#     # handlers = [
#     #     mocker.mock_open(read_data='somedata1').return_value,
#     #     mocker.mock_open(read_data='somedata2').return_value
#     # ]
#     # mocker.patch('builtins.open', side_effects=handlers)
#     cur_dir = Path("file1.txt")
#     assert universal_file_counter(cur_dir, "txt") == 2
