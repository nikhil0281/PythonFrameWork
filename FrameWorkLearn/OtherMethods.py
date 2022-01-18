import pytest

@pytest.fixture()
@pytest.mark.usefixtures("LifeCycle")
def test_URLDataUpdated(self, LifeCycle):
    if LifeCycle == "dv":
        url = "https://www.demoblaze.com/index.html"
    elif LifeCycle == "qa":
        url = "https://www.google.com"
    else:
        url = "https://yahoo.com"
    return url