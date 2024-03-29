import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

### test hash method ###
# @pytest.mark.skip("TODO")
def test_hash_range():
    hashtable = Hashtable()
    actual = hashtable._hash('test')
    assert 0 <= actual < hashtable.size

# @pytest.mark.skip("TODO")
def test_hash_same():
    hashtable = Hashtable()
    actual = hashtable._hash('test')
    actual2 = hashtable._hash('test')
    assert actual == actual2

### test set and get methods ###
# @pytest.mark.skip("TODO")
def test_set_one_get_one():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_set_two_get_one():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set('orange', 'used for orange juice')
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_key_not_exist():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set('orange', 'used for orange juice')
    actual = hashtable.get('banana')
    expected = None
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_bucket_collision():
    hashtable = Hashtable()
    hashtable.set('dear', 'the beginning of a letter')
    hashtable.set('read', 'the past tense of read')
    actual = hashtable.get('dear')
    expected = 'the beginning of a letter'
    assert actual == expected

### test has method ###
# @pytest.mark.skip("TODO")
def test_has():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.has("apple")
    expected = True
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_has_not():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.has("pineapple")
    expected = False
    assert actual == expected

### test keys and values methods ###
# @pytest.mark.skip("TODO")
def test_keys_list():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set('orange', 'used for orange juice')
    actual = hashtable.keys()
    expected = ['apple', 'orange']
    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_keys_list_empty():
    hashtable = Hashtable()
    actual = hashtable.keys()
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_values_list():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set('orange', 'used for orange juice')
    actual = hashtable.values()
    expected = ['Used for apple sauce', 'used for orange juice']
    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_values_list_empty():
    hashtable = Hashtable()
    actual = hashtable.values()
    expected = []
    assert actual == expected

@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
