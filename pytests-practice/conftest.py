import pytest


def pytest_adoption(parser):
    """Turn nice features on with the --nice option."""
    group = parser.getgroup('nice')
    group.addoption(
        '--nice',
        action='store_true',
        help='nice: turn failures into opportunities.')


def pytest_report_header():
    """A message is displayed in the header when running tests."""
    if pytest.config.getoption('nice'):
        return 'Thanks for running the tests.'


def pytest_report_teststatus(report):
    """Turn failures into opportunities."""
    if report.when == 'call':
        if report.failed and pytest.config.getoption('nice'):
            return report.outcome, 'O', 'OPPORTUNITY for improvement'
