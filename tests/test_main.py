import pytest
from main import sort_lists, read_today_messages, send_message

def test_sort_lists():
    list1 = ["Message 1", "Message 2"]
    list2 = [1, 2, 3, 4]
    result = sort_lists(list1, list2)
    assert result == [3, 4]  # Ожидаем, что все элементы из list2 будут возвращены

def test_sort_lists_with_numbers():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3, 4, 5]
    result = sort_lists(list1, list2)
    assert result == [4, 5]  # Ожидаем, что 4 и 5 будут возвращены 

def test_read_today_messages():
    messages = read_today_messages()
    assert len(messages) > 0  # Ожидаем, что будет хотя бы одно сообщение

def test_send_message():
    message = "Test message"
    send_message(message)   