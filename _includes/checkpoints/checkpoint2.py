"""
Checkpoint 2: Modularize a repeated problem
-------------------------------------------

Create a function to calculate the result for any initial flux, shield
thickness, and attenuation coefficient.
"""

import math as m


def calc_phi(phi_0, mu, x):
    """Calculates final flux after shield of thickness x with
    attenuation coefficient mu given the starting flux phi_0.

    Input:
    ------
        phi_0: float, initial flux value (photons/cm**2-s)
        mu: float, attenuation coefficient (1/cm)
        x: float, shield thickness (cm)

    Returns:
    --------
        phi: float, final flux value (photons/cm**2-s)
    """

    phi = phi_0 * m.exp(-mu*x)
    return(phi)


# Lead shield
phi_lead = calc_phi(1.e10, 0.125, 5.0)
print(phi_lead)


# Plastic shield
phi_plastic = calc_phi(1.e15, 0.02, 15.)
print(phi_plastic)
