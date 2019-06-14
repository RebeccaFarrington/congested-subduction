import underworld as uw
from underworld.scaling import units as u

import model_properties as modprop

alpha   = 3.0e-5 / u.degK

mantle_density   = 3400 * u.kilogram / u.metre**3 # at surface
eclogite_density = (((7.*3500* u.kilogram / u.metre**3)+(25.-7.)*2900  * u.kilogram / u.metre**3)/25.)

ref_density    = mantle_density * (modprop.Tint-modprop.Tsurf) * alpha

# Material properties
um = {
    'name'     : 'upper mantle',
    'index'    : 0,
    'viscosity': 1. * u.pascal * u.second * 1e20, 
    'density'  : ref_density,
    'cohesion' : 1e3 * u.megapascal,
}

lm = {
    'name'     : 'lower mantle',
    'index'    : 1,
    'viscosity': 10. * u.pascal * u.second * 1e20, 
    'density'  : ref_density,
    'cohesion' : 1e3 * u.megapascal,
}


# 80Ma oceanic lithosphere
subplate1 = {
    'name'     : 'oceanic plate 1',
    'index'    : 3,
    'viscosity':  1e5 * u.pascal * u.second * 1e20, 
    'density'  : -0.34 * ref_density,
    'density2' : eclogite_density,
    'cohesion' : 12.5  * u.megapascal,
    'cohesion2':  6.25 * u.megapascal,         # this is an estimate from Extended Data Figure 2 plot
}

subplate2 = {
    'name'     : 'oceanic plate 2',
    'index'    : 4,
    'viscosity':  1e5 * u.pascal * u.second * 1e20, 
    'density'  :   0.60 * ref_density,
    'cohesion' :  67.4  * u.megapascal,
    'cohesion2':  33.7 * u.megapascal,      
}

          
subplate3 = {
    'name'     : 'oceanic plate 3',
    'index'    : 5,
    'viscosity': 19296. * u.pascal * u.second * 1e20, 
    'density'  :   0.38 * ref_density,
    'cohesion' :  121.3 * u.megapascal,
    'cohesion2':   60.7 * u.megapascal,      
}

subplate4 = {
    'name'     : 'oceanic plate 4',
    'index'    : 6,
    'viscosity':   96. * u.pascal * u.second * 1e20, 
    'density'  :  0.22 * ref_density,
    'cohesion' : 174.5 * u.megapascal,
    'cohesion2':  87.2 * u.megapascal,      
}

# strong back arc material properties
backArc1 = {
    'name'     : 'ribbon1',
    'index'    : 7,
    'viscosity': 88797. * u.pascal * u.second * 1e20, 
    'density'  : -1.20 * ref_density,
    'cohesion' : 76.9 * u.megapascal,
    'cohesion2': 38.4 * u.megapascal,
}
backArc2 = {
    'name'     : 'ribbon2',
    'index'    : 8,
    'viscosity': 172. * u.pascal * u.second * 1e20, 
    'density'  : 0.12 * ref_density,
    'cohesion' : 184.6 * u.megapascal,
    'cohesion2':  92.3 * u.megapascal,
}

trans1 = {
    'name'     : 'trans1',
    'index'    : 9,
    'viscosity':  1e5 * u.pascal * u.second * 1e20, 
    'density'  : -1.98 * ref_density,
    'cohesion' : 40. * u.megapascal,
    'cohesion2': 20. * u.megapascal,
}
trans2 = {
    'name'     : 'trans2',
    'index'    : 10,
    'viscosity':  1e5 * u.pascal * u.second * 1e20, 
    'density'  : 0.25 * u.kilogram / u.metre**3,
    'cohesion' : 150. * u.megapascal,
    'cohesion2':  75. * u.megapascal,
}

craton1 = {
    'name'     : 'craton1',
    'index'    : 11,
    'viscosity':  1e5 * u.pascal * u.second * 1e20, 
    'density'  : -2.11* ref_density,
    'cohesion' : 130. * u.megapascal,
    'cohesion2':  65. * u.megapascal,
}

craton2 = {
    'name'     : 'craton2',
    'index'    : 12,
    'viscosity': 14763. * u.pascal * u.second * 1e20, 
    'density'  : -0.25 * ref_density,
    'cohesion' : 130. * u.megapascal,
    'cohesion2':  65. * u.megapascal,
}

# assume ribbon and buoyant strip have cratonic material properties
ribbon = {
    'name'     : 'ribbon',
    'index'    : 13,
    'viscosity':  1e5 * u.pascal * u.second * 1e20, 
    'density'  : -2.11* ref_density,
    'cohesion' : 130. * u.megapascal,
    'cohesion2':  65. * u.megapascal,
}

buoyStrip = {
    'name'     : 'buoyStrip',
    'index'    : 14,
    'viscosity':  1e5 * u.pascal * u.second * 1e20,    # strong 
    'density'  : -2.11* ref_density,   # assume cratonic density
    'cohesion' : 1e3 * u.megapascal,  # non yeilding 
    'cohesion2': 1e3 * u.megapascal,  # non yeilding 
}

# define material list
material_list = [ um, lm,
                 subplate1, subplate2, subplate3, subplate4, 
                 backArc1, backArc2, 
                 trans1, trans2, 
                 craton1, craton2, 
                 ribbon, 
                 buoyStrip ]
