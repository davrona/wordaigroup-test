import pytest
from word_counter import word_counter

def test_empty_file(tmp_path):
    # Test case for an empty file
    file_path = tmp_path / 'testcase1.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('')
    total_words, common_words = word_counter(str(file_path))
    assert total_words == 0
    assert common_words == []

def test_common_words(tmp_path):
    # Test case with a file containing common words
    file_path = tmp_path / 'testcase2.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('apple apple banana orange apple banana orange pear')
    total_words, common_words = word_counter(str(file_path))
    assert total_words == 8
    assert common_words == [('apple', 3), ('banana', 2), ('orange', 2), ('pear', 1)]

def test_case_insensitivity(tmp_path):
    # Test case to check case insensitivity
    file_path = tmp_path / 'testcase3.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('Apple APPLE OrAnGe oranGe BANANA')
    total_words, common_words = word_counter(str(file_path))
    assert total_words == 5
    assert common_words == [('apple', 2), ('orange', 2), ('banana', 1)]

def test_complex_file(tmp_path):
    # Test case with a file containing special characters and variations
    file_path = tmp_path / 'testcase4.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('The quick brown fox jumps over the lazy dog. Fox, dog, and lazy dog!')
    total_words, common_words = word_counter(str(file_path))
    assert total_words == 14
    assert common_words == [('dog', 3), ('the', 2), ('fox', 2), ('lazy', 2), ('quick', 1), ('brown', 1), ('jumps', 1), ('over', 1), ('and', 1)]

# Add more test cases as needed
