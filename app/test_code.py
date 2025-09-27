from main import display_cars

def test_code():
    count = display_cars()
    assert isinstance(count,list)
    assert len(count) >= 1
