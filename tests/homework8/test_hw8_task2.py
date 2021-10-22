# from homework8.task2 import TableData
#
#
# presidents = TableData(database_name='example.sqlite', table_name='presidents')
#
#
# def test_table_data_like_dict():
#     """checking that we can refer to the class as a dictionary"""
#     assert presidents['Yeltsin'] == ['Yeltsin', 999, 'Russia']
#
#
# def test_table_data_len():
#     """checking that we can find the number of rows"""
#     assert len(presidents) == 3
#
#
# def test_table_data_is_collections():
#     """checking that the object implements the iteration protocol"""
#     assert [president for president in presidents] == ["Yeltsin", "Trump", "Big Man Tyrone"]
#
#
# def test_table_data_is_operator():
#     """checking "is" operator support"""
#
#     assert 'Yeltsin' in presidents
