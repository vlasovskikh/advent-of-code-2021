from aoc21.p01a import count_depth_increases


def test_empty():
    assert count_depth_increases([]) == 0


def test_single():
    assert count_depth_increases([100]) == 0


def test_single_increase():
    assert count_depth_increases([100, 101]) == 1


def test_single_decrease():
    assert count_depth_increases([100, 99]) == 0


def test_single_unchanged():
    assert count_depth_increases([100, 100]) == 0


def test_two_spaced_increases():
    assert count_depth_increases([100, 101, 98, 99]) == 2
