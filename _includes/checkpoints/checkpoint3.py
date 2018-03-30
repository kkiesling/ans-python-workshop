"""
Checkpoint 3: Passing a set of properties
-----------------------------------------

Pass a tuple representing the shielding properties (x and mu) to the
function.
"""

import math as m

def calc_phi(phi_0, mat_props):
    """Calculates final flux after shield of thickness x with
    attenuation coefficient mu given the starting flux phi_0.

    Input:
    ------
        phi_0: float, initial flux value (photons/cm**2-s)
        mat_props: tuple, a tuple of size 2 in the form (mu, x) where
            mu and x are:
                mu: float, attenuation coefficient (1/cm)
                x: float, shield thickness (cm)

    Returns:
    --------
        phi: float, final flux value (photons/cm**2-s)
    """

    # unpack properties
    mu = mat_props[0]
    x = mat_props[1]

    # calcluate phi
    phi = phi_0 * m.exp(-mu*x)

    return(phi)


# Lead shield
lead_props = (.125, 5.0)
phi_lead = calc_phi(1.e10, lead_props)
print(phi_lead)


# Plastic shield
plastic_props = (.02, 15.0)
phi_plastic = calc_phi(1.e15, plastic_props)
print(phi_plastic)
