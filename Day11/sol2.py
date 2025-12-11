#!/usr/bin/env python

import collections
import functools
import os.path


def get_input(filename=None):
  if not filename:
    filename = os.path.join(os.path.dirname(__file__), "input.txt")
  with open(filename) as fp:
    input = fp.read().rstrip("\n")

  connections = collections.defaultdict(set)
  for line in input.split("\n"):
    machine, outputs = line.split(": ")
    connections[machine].update(outputs.split(" "))
  return connections


def part1(input):
  @functools.cache
  def count_paths(start):
    if start == "out":
      return 1
    return sum(count_paths(next) for next in input[start])

  return count_paths("you")


def part2(input):
  @functools.cache
  def count_paths(start, fft=False, dac=False):
    if start == "out":
      return 1 if fft and dac else 0
    return sum(
      count_paths(next, fft=fft or start == "fft", dac=dac or start == "dac")
      for next in input[start]
    )

  return count_paths("svr")


if __name__ == "__main__":
  # We are running in a Colab-like environment, so argparse is not suitable.
  # Directly call the functions with a hardcoded input file name.
  # Note: __file__ is not defined in Colab, so use 'input.txt' directly.
  input_data = get_input("input.txt")

  answer1 = part1(input_data)
  print(answer1)

  answer2 = part2(input_data)
  print(answer2)
