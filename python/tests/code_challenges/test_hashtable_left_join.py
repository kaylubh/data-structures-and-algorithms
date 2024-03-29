import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", "NONE"],
        ["guide", "usher", "follow"],
    ]

    actual = left_join(synonyms, antonyms)

    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_first_empty():
    synonyms = {}
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = []

    actual = left_join(synonyms, antonyms)

    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_second_empty():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {}

    expected = [
        ["fond", "enamored", "NONE"],
        ["wrath", "anger", "NONE"],
        ["diligent", "employed", "NONE"],
        ["outfit", "garb", "NONE"],
        ["guide", "usher", "NONE"],
    ]

    actual = left_join(synonyms, antonyms)

    assert sorted(actual) == sorted(expected)
