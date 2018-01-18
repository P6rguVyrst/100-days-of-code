#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tasks` package."""

import pytest

from click.testing import CliRunner

from tasks.tasks import Task
from tasks import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

@pytest.mark.alpha
def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'tasks.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


###

def test_member_access():
    t = Task('buy milk', 'toomas')
    assert t.summary == 'buy milk'
    assert t.owner == 'toomas'
    assert (t.done, t.id) == (False, None)



def test_asdict():
    t_task = Task('codecodecode', 'toomas', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'codecodecode',
        'owner': 'toomas',
        'done': True,
        'id': 21,
    }
    assert t_dict == expected

def test_replace():
    t_before = Task('finish book', 'toomas', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'toomas', True, 10)
    assert t_after == t_expected

def test_defaults():

    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    t = Task('buy milk', 'toomas')
    assert t.summary == 'buy milk'
    assert t.owner == 'toomas'
    assert (t.done, t.id) == (False, None)
