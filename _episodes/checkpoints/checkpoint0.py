# need to import the "math" module to use different math functions
import math as m

# Lead shield 5 cm thick
phi_0 = 1.e10 # #/cm**2-s
mu = 0.125 # attenuation coefficient
x = 5.0 # shield thickness in cm
phi = phi_0 * m.exp(-mu*x)

print(phi)

