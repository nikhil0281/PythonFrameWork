import pytest


@pytest.mark.usefixtures("setup")
class fixtureclass:

    def test_fixmet(self):
        print("Hello world")