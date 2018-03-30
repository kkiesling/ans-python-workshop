"""
Checkpoint 4: Shield made of two materials
------------------------------------------

Pass a set of material properties representing two materials in a shield
each with their own thickness and attenuation coefficient.
"""

import math as m

def calc_phi(phi_0, mat_props):
    """Calculates final flux after two shields of different thicknesses
    and attenuation coefficients given the starting flux phi_0.

    Input:
    ------
        phi_0: float, initial flux value (photons/cm**2-s)
        mat_props: list of tuples, each tuple represents a set of
            properties for each material in the problem in the form
            [(mu0, x0), (mu1, x1)] where:
                mu0: float, attenuation coefficient for first shield
                    (1/cm)
                x0: float, shield thickness for first shield (cm)
                mu1: float, attenuation coefficient for second shield
                    (1/cm)
                x1: float, shield thickness for second sheild (cm)

    Returns:
    --------
        phi_2: float, final flux value after second shield
            (photons/cm**2-s)
    """

    # unpack each set of material properties
    mat0 = mat_props[0]     # first set of properties (mu0, x0)
    mat1 = mat_props[1]     # second set of properties (mu1, x1)

    # first material properties and get flux after first shield
    mu0 = mat0[0]
    x0 = mat0[1]
    phi_1 = phi_0 * m.exp(-mu0*x0)

    # get second material properties and get flux after second shield
    mu1 = mat1[0]
    x1 = mat1[1]
    phi_2 = phi_1 * m.exp(-mu1*x1)

    # return final flux value
    return(phi_2)


# Set initial flux and material properties
phi_0 = 1.e15
lead_props = (.125, 5.0)
plastic_props = (.02, 15.0)
mat_props = [lead_props, plastic_props]

phi_final = calc_phi(phi_0, mat_props)

print(phi_final)

