import app.main


def test_should_return_zeros_when_ages_are_zero() -> None:
    assert app.main.get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_before_fifteen_years() -> None:
    assert app.main.get_human_age(14, 14) == [0, 0]


def test_should_return_one_human_year_at_fifteen() -> None:
    assert app.main.get_human_age(15, 15) == [1, 1]


def test_should_still_return_one_human_year_at_twenty_three() -> None:
    assert app.main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_human_years_at_twenty_four() -> None:
    assert app.main.get_human_age(24, 24) == [2, 2]


def test_should_still_return_two_human_years_at_twenty_seven() -> None:
    assert app.main.get_human_age(27, 27) == [2, 2]


def test_cat_should_be_older_than_dog_at_twenty_eight() -> None:
    assert app.main.get_human_age(28, 28) == [3, 2]


def test_should_correctly_calculate_large_ages() -> None:
    assert app.main.get_human_age(100, 100) == [21, 17]
