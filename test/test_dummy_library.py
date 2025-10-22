from open_source_template.main import another_dummy_func, dummy_func


def test_dummy_func():
    """Test the correctness of dummy_func."""

    assert dummy_func(3.2) == 3


def test_another_dummy_func():
    """Test the correctness of another_dummy_func."""

    assert another_dummy_func(5) == 5.0
