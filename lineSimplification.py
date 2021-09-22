import numpy as np
from simplification.cutil import (
    simplify_coords, # this is Douglas-Peucker
    simplify_coords_vw,  # this is Visvalingam-Whyatt
)

# generate coords of 5000 ordered points as a line
coords = np.sort(np.random.rand(5000, 2), axis=0)
# how many coordinates returns DP with eps=0.01?
simplified = simplify_coords(coords, .0025).shape


