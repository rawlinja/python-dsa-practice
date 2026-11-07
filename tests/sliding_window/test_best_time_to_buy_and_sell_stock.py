from sliding_window.best_time_to_buy_and_sell_stock import max_profit


def test_example_buy_low_sell_high():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_zero_when_prices_only_fall():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_zero_for_a_single_day():
    assert max_profit([5]) == 0


def test_zero_when_all_prices_equal():
    assert max_profit([3, 3, 3, 3]) == 0


def test_two_days_rising():
    assert max_profit([1, 2]) == 1


def test_two_days_falling():
    assert max_profit([2, 1]) == 0


def test_cannot_sell_before_buying_when_max_comes_first():
    assert max_profit([9, 2, 4, 1]) == 2


def test_later_lower_min_beats_earlier_pair():
    assert max_profit([3, 8, 1, 10]) == 9


def test_earlier_pair_beats_later_lower_min():
    assert max_profit([2, 9, 1, 3]) == 7


def test_best_profit_not_at_last_day():
    assert max_profit([1, 6, 2, 3]) == 5


def test_ties_at_the_minimum():
    assert max_profit([2, 5, 2, 7]) == 5


def test_zero_price_allowed():
    assert max_profit([0, 10000]) == 10000
