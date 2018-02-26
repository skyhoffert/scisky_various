# Sky
# Feb 25, 2018
# Some math for video about distance between planets

# constants for objects
d_from_s_mercury  = 57.91e9            # m
d_from_s_earth    = 149.6e9            # m
d_from_s_mars     = 227.9e9            # m
d_from_s_jupiter  = 778.5e9            # m
d_from_s_neptune  = 4.498e12           # m
d_from_s_pluto    = 5.906e12           # m

# other constants
sphere_size       = 24e-2              # m, basketball
solar_radius      = 695.7e6            # m

# ask which planet?
choice = input('Which object would you like? (M V E M A J S U N P E): ')

# by default...
distance_from_sun = d_from_s_earth

# choose object
if choice.lower() == 'mercury':
    distance_from_sun = d_from_s_mercury
elif choice.lower() == 'earth':
    distance_from_sun = d_from_s_earth
elif choice.lower() == 'mars':
    distance_from_sun = d_from_s_mars
elif choice.lower() == 'jupiter':
    distance_from_sun = d_from_s_jupiter
elif choice.lower() == 'neptune':
    distance_from_sun = d_from_s_neptune
elif choice.lower() == 'pluto':
    distance_from_sun = d_from_s_pluto
else:
    print( '{} was not a valid option'.format(choice) )

# compute
res    = distance_from_sun / (2 * solar_radius) * sphere_size # m

# print results
print( 'Distance is {0:.2f} m'.format(res) )
print( '         or {0:.2f} ft' .format(res * 3.28) )
print( '         or {0:.2f} yds'.format(res * 1.09) )