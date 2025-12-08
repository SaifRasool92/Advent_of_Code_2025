


# **Highlights of Day 8: Playground**

* You arrive in a huge underground playground filled with junction boxes hanging in the air.
* Elves want to connect these boxes using strings of lights, and electricity can only flow between connected boxes.
* Goal is to connect boxes based on the **shortest 3D distance** between them.
* Each connection forms or expands a **circuit**. Unconnected boxes are single-box circuits.
* As you keep connecting the closest pairs, circuits merge or stay the same if already connected.
* After **10 shortest connections** in the example, circuits form sizes: 5, 4, 2, 2, and seven singles.
* Multiplying the **three largest circuit sizes** gives **40**.
* In your full puzzle, after connecting the **closest 1000 pairs**, the product of the three biggest circuits is **115885**.

# **Part Two Highlights**

* Now you keep connecting until **all junction boxes form one big circuit**.
* The key moment is the **final connection** that unifies every box.
* In the example, the last two boxes to connect are at X coordinates **216** and **117**.
* Their product is **25272**.
* Your goal: multiply the X coordinates of the **final pair** you connect in your actual input.
