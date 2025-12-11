
# **Part 1 Highlights**

* You enter the reactor area and discover a communication issue between the reactor and a new server rack.
* The Elves give you a list describing how each device connects to others.
* Your job is to start at the device labeled you and find every possible route that eventually reaches out.
* Each device only sends data forward through its outputs.
* After exploring all routes in your full puzzle input, the total number of valid paths is **796**.

# **Part 2 Highlights**

* The Elves figure out that the faulty path must pass through two specific devices: **dac** and **fft**.
* Your new task is to find all paths starting from svr and ending at out.
* From those, count only the ones that include both dac and fft, in any order.
* The example shows several paths, but only a subset goes through both required devices.
* Your final task is: count how many svr to out paths satisfy this condition.
