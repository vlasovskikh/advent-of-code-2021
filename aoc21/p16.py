from __future__ import annotations

from dataclasses import dataclass
from typing import Union, ClassVar

import bitstruct

from aoc21 import utils


@dataclass
class Packet:
    version: int
    type_id: int
    body: Union[Literal, Operator]

    @staticmethod
    def from_bytes(data: bytes, offset: int = 0) -> tuple[Packet, int]:
        version, type_id, offset = unpack(">u3>u3", data, offset)
        body: Union[Literal, Operator]
        if type_id == 4:
            body, offset = Literal.from_bytes(data, offset)
        else:
            body, offset = Operator.from_bytes(data, offset)
        return Packet(version, type_id, body), offset

    def evaluate(self) -> int:
        body = self.body
        if isinstance(body, Literal):
            return body.evaluate()
        elif isinstance(body, Operator):
            op = body.ops.get(self.type_id, None)
            if not op:
                raise TypeError(f"Uknown type ID: {self.type_id}")
            f = getattr(body, op, None)
            if not f:
                raise TypeError(f"Uknown operation: {op!r}")
            return f()
        else:
            raise TypeError(f"Unknown body type: {type(body)}")


@dataclass
class Literal:
    value: int

    @staticmethod
    def from_bytes(data: bytes, offset: int) -> tuple[Literal, int]:
        value = 0
        cont = True
        while cont:
            cont, bits, offset = unpack("b1>u4", data, offset)
            value = value << 4 | bits
        return Literal(value), offset

    def evaluate(self) -> int:
        return self.value


@dataclass
class Operator:
    packets: list[Packet]

    ops: ClassVar[dict[int, str]] = {
        0: "sum",
        1: "product",
        2: "minimum",
        3: "maximum",
        5: "greater_than",
        6: "less_than",
        7: "equal_to",
    }

    @staticmethod
    def from_bytes(data: bytes, offset: int) -> tuple[Operator, int]:
        packets = []
        len_type_id, offset = unpack(">u1", data, offset)
        if len_type_id == 0:
            bit_len, offset = unpack(">u15", data, offset)
            end = offset + bit_len
            while offset < end:
                packet, offset = Packet.from_bytes(data, offset)
                packets.append(packet)
            return Operator(packets), offset
        elif len_type_id == 1:
            n_packets, offset = unpack(">u11", data, offset)
            for i in range(n_packets):
                packet, offset = Packet.from_bytes(data, offset)
                packets.append(packet)
            return Operator(packets), offset
        else:
            raise ValueError(f"Unknown length type ID: {len_type_id}")

    def sum(self) -> int:
        return sum(p.evaluate() for p in self.packets)

    def product(self) -> int:
        res = 1
        for p in self.packets:
            res *= p.evaluate()
        return res

    def minimum(self) -> int:
        return min(p.evaluate() for p in self.packets)

    def maximum(self) -> int:
        return max(p.evaluate() for p in self.packets)

    def greater_than(self) -> int:
        a, b = self.packets
        return 1 if a.evaluate() > b.evaluate() else 0

    def less_than(self) -> int:
        a, b = self.packets
        return 1 if a.evaluate() < b.evaluate() else 0

    def equal_to(self) -> int:
        a, b = self.packets
        return 1 if a.evaluate() == b.evaluate() else 0


def unpack(fmt: str, data: bytes, offset: int) -> tuple:
    res = bitstruct.unpack_from(fmt, data, offset)
    return *res, offset + bitstruct.calcsize(fmt)


def sum_version_numbers(data: bytes) -> int:
    packet, offset = Packet.from_bytes(data)
    return sum_versions(packet)


def sum_versions(packet: Packet) -> int:
    version = packet.version
    body = packet.body
    if isinstance(body, Literal):
        return version
    elif isinstance(body, Operator):
        return version + sum(sum_versions(p) for p in body.packets)
    else:
        raise TypeError(f"Unknown body type: {type(body)}")


def parse_input(lines: list[str]) -> bytes:
    return bytes.fromhex(lines[0])


def main():
    data = parse_input(utils.read_input_lines(__file__))
    p, offset = Packet.from_bytes(data)
    print(sum_versions(p))
    print(p.evaluate())


if __name__ == "__main__":
    main()
