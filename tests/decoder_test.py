#!/usr/bin/env python3
"""Exercise the actual polling frame loop without Python 2 or GPIO hardware."""

import ast
from pathlib import Path
import textwrap
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "pui.py"
source = SOURCE.read_text()
start = source.index("\tc=0\n")
end = source.index("\n\tif l!=", start)
frame_loop = compile(textwrap.dedent(source[start:end]), str(SOURCE), "exec")
mapping = ast.literal_eval(next(line[2:] for line in source.splitlines() if line.startswith("d=")))


def receive_frame(bits):
	clock = iter([0, 1] * 11)
	data = iter(bits)
	state = {"clk": lambda: next(clock), "dta": lambda: next(data)}
	exec(frame_loop, state)
	return state["c"]


class DecoderTest(unittest.TestCase):
	def test_a_make_code(self):
		# Set-2 0x1c: start, eight least-significant-first bits, odd parity, stop.
		self.assertEqual(receive_frame([0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]), 56)

	def test_all_byte_frames(self):
		# The existing lookup table uses the reversed eight data bits as its key.
		for byte in range(256):
			data = [(byte >> bit) & 1 for bit in range(8)]
			parity = 1 - sum(data) % 2
			frame = [0, *data, parity, 1]
			with self.subTest(byte=byte):
				self.assertEqual(receive_frame(frame), int(f"{byte:08b}"[::-1], 2))

	def test_existing_character_map(self):
		for byte, character in [(0x1c, "a"), (0x32, "b"), (0x16, "1"), (0x5a, "\n")]:
			data = [(byte >> bit) & 1 for bit in range(8)]
			frame = [0, *data, 1 - sum(data) % 2, 1]
			with self.subTest(character=character):
				self.assertEqual(mapping[receive_frame(frame)], character)


if __name__ == "__main__":
	unittest.main()
