"""
Checkpoint 0: Initial Problem
------------------------------

Compute flux after 5 cm of lead shielding using simple linear
attenuation formula.
"""

# need to import the "math" module to use different math functions
import math as m

# set values of initial flux (phi_0), attenuation coefficient (mu),
# and shield thickness (x)
phi_0 = 1.e15   # photon/cm**2-s
mu = 0.125      # attenuation coefficient
x = 5.0         # shield thickness in cm

# calcuate phi
phi = phi_0 * m.exp(-mu*x)

# print the final result
print(phi)
