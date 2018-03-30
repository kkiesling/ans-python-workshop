"""
Checkpoint 1: Two different problems
------------------------------------

Compute two separate attenuation problems for lead and plastic using
different initial fluxes, thickness, and attenuation coefficients.
"""

import math as m

# Compute result after lead shield 5 cm thick with an initial flux of
# 1e10 photons/cm**2-s
phi_0 = 1.e10   # photons/cm**2-s
mu = 0.125      # attenuation coefficient 1/cm
x = 5.0         # shield thickness in cm
phi_lead = phi_0 * m.exp(-mu*x)

print(phi_lead)


# Compute result after plastic shield 15 cm thick with an initial flux
# of 1e15 photons/cm**2-s
phi_0 = 1.e15   # photons/cm**2-s
mu = 0.02       # attenuation coefficient 1/cm
x = 15.0        # shield thickness in cm
phi_plastic = phi_0 * m.exp(-mu*x)

print(phi_plastic)
