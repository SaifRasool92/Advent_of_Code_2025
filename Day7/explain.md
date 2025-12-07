<p align="center">
  <img src="https://github.com/user-attachments/assets/d6588138-c53d-4cd2-9471-37414be95f01" alt="2025 Day 6 Visualization" width="100%">
</p>




# Highlights - Part One

* Start at the entry point and follow the beam downward through empty cells.
* When the beam hits a splitter, that beam stops and two new beams begin immediately to its left and right.
* Continue that process until every beam either exits the grid or ends at a splitter.
* The quantity you need is how many times a beam was stopped by a splitter (total splits).
* For your input the total count of splits is **1609**. Great job analyzing that.

# Highlights - Part Two

* Now imagine a single quantum particle that simultaneously takes both branches at every splitter. Each branching creates separate timelines.
* To find how many timelines exist after the particle finishes, explore every possible route but merge identical situations so you don’t double-count equivalent outcomes.
* Practical method: simulate step-by-step, keeping the set of active positions (or states) after each move; when a splitter is reached, replace that position with its two child positions; if multiple timelines reach the same cell, treat them as separate histories during counting but collapse identical positions when propagating forward to avoid exponential explosion.
* The worked example in the problem ends with **40** timelines; apply the same simulation/DP approach to your full input to get the final timeline count.


