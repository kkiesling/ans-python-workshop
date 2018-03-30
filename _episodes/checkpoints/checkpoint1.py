import math as m

# Lead shield 5 cm thick
phi_0 = 1.e10 # #/cm**2-s
mu = 0.125 # attenuation coefficient
x = 5.0 # shield thickness in cm
phi_lead = phi_0 * m.exp(-mu*x)

print(phi_lead)


# Compute plastic shield 15 cm thick
phi = 1.e15
mu = 0.02
x = 15.
phi_plastic = phi_0 * m.exp(-mu*x)

print(phi_plastic)
