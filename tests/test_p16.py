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


def test_example_b_1():
    data = "C200B40A82".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 3


def test_example_b_2():
    data = "04005AC33890".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 54


def test_example_b_3():
    data = "880086C3E88112".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 7


def test_example_b_4():
    data = "CE00C43D881120".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 9


def test_example_b_5():
    data = "D8005AC2A8F0".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 1


def test_example_b_6():
    data = "F600BC2D8F".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 0


def test_example_b_7():
    data = "9C005AC2F8F0".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 0


def test_example_b_8():
    data = "9C0141080250320F1802104A08".splitlines()
    p, offset = Packet.from_bytes(parse_input(data))
    assert p.evaluate() == 1
