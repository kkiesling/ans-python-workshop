# need to import the "math" module to use different math functions
import math as m

def calc_phi(phi_0, mat_props):

    mu = mat_props[0]
    x = mat_props[1]
    phi = phi_0 * m.exp(-mu*x)

    return(phi)


# Lead shield 5 cm thick
lead_props = (.125, 5.0)
phi_lead = calc_phi(1.e10, lead_props)
print(phi_lead)


# plastic shield 15 cm thick
plastic_props = (.02, 15.)
phi_plastic = calc_phi(1.e15, plastic_props)
print(phi_plastic)
