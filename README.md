# Oblique throw - Simple simulation
Simple simulation of the oblique throw, without air resistance.
This script visualizes a simulated oblique throw without friction forces. The initial velocity, the launch angle **alpha**, the location factor **g** and the launch height **h** can be varied as desired.
A table should also appear in the console as output, containing the following information:

- The zero point: y(x) = 0
- The zero point: y(t) = 0

#### Units
- *alpha* = deg
- *g-acceleration* = m/s²
- *initial height* = m
- *initial velocity* = m/s

### Example

    python3 oblique_throw_without_air_res.py --alpha 45 -g 9.81 -y 20 -i 10
