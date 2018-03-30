# need to import the "math" module to use different math functions
import math as m

def calc_phi(phi_0, mat_props):

    mat0 = mat_props[0]
    mat1 = mat_props[1]

    mu0 = mat0[0]
    x0 = mat0[1]

    phi_1 = phi_0 * m.exp(-mu0*x0)

    mu1 = mat1[0]
    x1 = mat1[1]

    phi_2 = phi_1 * m.exp(-mu1*x1)

    return(phi_2)


# Lead shield 5 cm thick followed by plastic shield 15 cm thick
phi_0 = 1.e10
lead_props = (.125, 5.0)
plastic_props = (.02, 15.)
mat_props = [lead_props, plastic_props]

phi_final = calc_phi(phi_0, mat_props)

print(phi_final)

