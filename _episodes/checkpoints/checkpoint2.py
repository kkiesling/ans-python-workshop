# need to import the "math" module to use different math functions
import math as m

def calc_phi(phi_0, mu, x):

    phi = phi_0 * m.exp(-mu*x)

    return(phi)



# Lead shield 5 cm thick
phi_lead = calc_phi(1.e10, 0.125, 5.0)
print(phi_lead)


# plastic shield 15 cm thick
phi_plastic = calc_phi(1.e15, 0.02, 15.)
print(phi_plastic)
