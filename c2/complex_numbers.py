import numpy as np

# define complex numbers
z = 1.0 + 2.0j
u = 2.0 + 3.0j

# display
print("z= ", z)
print("u= ", u)

# display
print("Re(z)= ", np.real(z))  # real part
print("Im(z)= ", np.imag(z))  # imaginary part
print("z^*= ", np.conjugate(z))  # complex conjugate
print("|z|= ", np.abs(z))  # absolute value

v = z + u
print("z+u= ", v)  # addition

v = z - u
print("z-u= ", v)  # subtraction

v = z * u
print("z*u= ", v)  # multiplication

v = z / u
print("z/u= ", v)  # division
