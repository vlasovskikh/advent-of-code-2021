from aoc21.p16 import parse_input, sum_version_numbers, Packet, Literal, Operator


def test_literal_2021():
    data = "D2FE28".splitlines()
    msg = parse_input(data)
    p, offset = Packet.from_bytes(msg)
    assert p == Packet(6, 4, Literal(2021))


def test_operator_type_0():
    data = "38006F45291200".splitlines()
    msg = parse_input(data)
    p, offset = Packet.from_bytes(msg)
    assert p == Packet(
        1,
        6,
        Operator(
            [
                Packet(6, 4, Literal(10)),
                Packet(2, 4, Literal(20)),
            ]
        ),
    )


def test_operator_type_1():
    data = "EE00D40C823060".splitlines()
    msg = parse_input(data)
    p, offset = Packet.from_bytes(msg)
    assert p == Packet(
        7,
        3,
        Operator(
            [
                Packet(2, 4, Literal(1)),
                Packet(4, 4, Literal(2)),
                Packet(1, 4, Literal(3)),
            ]
        ),
    )


def test_example_1():
    data = "8A004A801A8002F478".splitlines()
    assert sum_version_numbers(parse_input(data)) == 16


def test_example_2():
    data = "620080001611562C8802118E34".splitlines()
    assert sum_version_numbers(parse_input(data)) == 12


def test_example_3():
    data = "C0015000016115A2E0802F182340".splitlines()
    assert sum_version_numbers(parse_input(data)) == 23


def test_example_4():
    data = "A0016C880162017C3686B18A3D4780".splitlines()
    assert sum_version_numbers(parse_input(data)) == 31
