import pytest
from leap_year import isLeapYear

def test_is_leap_year_when_year_divisible_by_4_but_not_100():
    assert isLeapYear(1972) == False

def test_is_leap_year_when_year_divisible_by_400():
    assert isLeapYear(2024) == True

def test_is_not_leap_year_when_year_not_divisible_by_4():
    assert isLeapYear(2125) == False

def test_is_not_leap_year_when_year_divisible_by_100_but_not_400():
    assert isLeapYear(1973) == False

# Det er skuddår i: 1972, 1992, 2016, 2020, 2024, 2032, 2052, 2124
# Det er ikke skudd i: 1973, 1974, 1991, 1993, 2015, 2017, 2019, 2021, 2023, 2025, 2031, 2033, 2051, 2053, 2123, 2125