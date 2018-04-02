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
phi_0 = 1.e10   # photons/cm**2-s
mu = 0.5182     # attenuation coefficient 1/cm
x = 5.0         # shield thickness in cm
phi_lead = calc_phi(phi_0, mu, x)
print(phi_lead)


# Water shield
phi_0 = 1.e15   # photons/cm**2-s
mu = 0.0493     # attenuation coefficient 1/cm
x = 15.0        # shield thickness in cm
phi_water = calc_phi(phi_0, mu, x)
print(phi_water)
