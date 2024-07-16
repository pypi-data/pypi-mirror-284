

import tempfile

"""Tests for `spock` package."""

import pytest
from spock_literature import Author
from spock_literature.publication import Publication
from spock_literature.bot import Bot_LLM


llm = Bot_LLM()

@pytest.fixture
def create_author():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    author = Author('Mehrad Ansari')
    return author
    
    
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_author(create_author):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    
    global llm
    
    with tempfile.NamedTemporaryFile(mode='w', delete=True, suffix='.json') as temp_file:
        create_author.setup_author(temp_file.name, llm)
    
    


@pytest.fixture
def Publication():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    pass

def test_author(Author):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string