import pytest

def not_string(s):
    hst = s.split()

    if (hst[0] == "not"):
        return s
    return "not " + s

@pytest.mark.parametrize("s, result", [('pass', 'not pass'), ('rot', 'not rot'), ("bay2tc", "not bay2tc")])
def test_not_string(s, result):
    assert result == not_string(s)

if __name__ == "__main__":
    test_not_string("quamon", "not quamon")