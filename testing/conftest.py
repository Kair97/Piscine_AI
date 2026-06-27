import pytest
from bank import BankAccount

@pytest.fixture
def sample_data():
    return [4, 8, 15, 16, 23, 42]

@pytest.fixture 
def empty_list():
    return []

@pytest.fixture
def funded_account():
    return BankAccount("Kair", 1000.0)