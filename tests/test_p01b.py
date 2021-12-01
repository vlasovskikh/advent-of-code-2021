from aoc21.p01b import count_sliding_window_depth_increases


def test_0():
    assert count_sliding_window_depth_increases([]) == 0


def test_1():
    assert count_sliding_window_depth_increases([100]) == 0


def test_2():
    assert count_sliding_window_depth_increases([100, 101]) == 0


def test_3():
    assert count_sliding_window_depth_increases([100, 101, 102]) == 0


def test_single_increase():
    assert count_sliding_window_depth_increases([100, 101, 102, 101]) == 1


def test_single_decrease():
    assert count_sliding_window_depth_increases([100, 101, 100, 99]) == 0


def test_single_unchanged():
    assert count_sliding_window_depth_increases([100, 101, 100, 100]) == 0


def test_two_spaced_increases():
    assert count_sliding_window_depth_increases([100, 101, 101, 101, 100, 102]) == 2
