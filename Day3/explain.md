<p align="center">
  <img src="https://github.com/user-attachments/assets/0dabc0bd-8832-4eba-8751-0732538e8ac2" alt="2025 Day 3 Visualization" width="600">
</p>



**Part One Highlights**
• You have several battery banks. Each line is one bank.
• Each digit is a battery with a joltage from 1 to 9.
• You must pick exactly **two batteries in order** to form the largest possible two digit number.
• For each bank, choose the two largest digits that appear earliest in the sequence to form the maximum number.
• Add the maximum two digit joltages from all banks.
• Example total in the prompt: **357**.
• Your final answer: **17263**.

**Part Two Highlights**
• Now you must pick **exactly twelve batteries** from each bank.
• They must stay in their original order; no rearranging.
• The goal is to create the **largest possible 12 digit number** from each bank.
• Strategy: skip the smallest digits while keeping the sequence length at 12.
• Example total for the sample: **3121910778619**.
• Your task: compute this total for your full input.


