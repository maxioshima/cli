from ..clollection_framework import unique_characters_counter
import pytest


def test_argparse_argument_getting_mock(mocker):
    mocker.patch(
        'Collection.clollection_framework.create_parser',
        return_value="abcd"
    )

    expected = 4
    actual = unique_characters_counter("abcd")
    assert expected == actual


def test_of_expected_parameter1():
    assert unique_characters_counter('aab34t') == 4


def test_of_expected_value2():
    assert unique_characters_counter('1123455') == 3


def test_one_more_word():
    assert unique_characters_counter('abcc12 23nn 11l') == 4


def test_of_type_1():
    with  pytest.raises(TypeError):
        unique_characters_counter(1)


def test_of_type_2():
    with  pytest.raises(TypeError):
        unique_characters_counter(print())


def test_of_type_3():
    with  pytest.raises(TypeError):
        unique_characters_counter(True)
