# need to import the "math" module to use different math functions
import math as m

def calc_phi(phi_0, mat_props):

    for mat in mat_props:
        mu = mat[0]
        x = mat[1]

        phi_0 = phi_0 * m.exp(-mu*x)

    return(phi_0)


# Lead shield 5 cm thick followed by plastic shield 15 cm thick
# followed by tungsten
phi_0 = 1.e15
lead_props = (.125, 5.0)
plastic_props = (.02, 15.)
tungsten_props = (.120, 7.)
mat_props = [lead_props, plastic_props, tungsten_props]

phi_final = calc_phi(phi_0, mat_props)

print(phi_final)

