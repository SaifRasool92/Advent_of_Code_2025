# Highlights

* Scene: rolls of paper are placed on a grid using @ for rolls and . for empty spaces.
* Accessibility rule: a roll is accessible to a forklift if fewer than four of its eight neighbors contain rolls.
* Part 1 goal: count how many rolls are accessible in the initial grid without removing anything.

  * Example: initial accessible rolls in the sample = 13.
  * Your full puzzle answer = 1553.
* Part 2 goal: repeatedly remove any accessible roll, update the grid, and continue until no more removals are possible. Count total removed.

  * Example: total removed in the sample = 43.
  * Your full puzzle answer = 8442.
* Implementation sketch:

  1. Parse grid into a 2D array.
  2. For each cell with @, count its eight neighbors that are @.
  3. For part 1, count cells where neighbor count < 4.
  4. For part 2, loop: find all currently accessible rolls, remove them (set to .), repeat until none found; accumulate count.
* Complexity and tips:

  * Each full scan is O(rows * cols). Part 2 may need many iterations, worst case O(rows * cols * iterations). Use a queue or track frontier of changed neighbors to speed it up.
  * Be careful with boundary cells when checking neighbors.
  * Visualizing a few iterations helps debug which rolls become accessible next.
