from __future__ import annotations

from dataclasses import dataclass
from typing import Union

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


@dataclass
class Operator:
    packets: list[Packet]

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
    print(sum_version_numbers(data))


if __name__ == "__main__":
    main()
