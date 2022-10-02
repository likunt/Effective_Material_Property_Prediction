#!/usr/bin/env python
import plotly.graph_objects as go
import scipy.io
import numpy as np

loaded_arr = np.loadtxt("VF20.out", dtype="int8")

# This loadedArr is a 2D array, therefore
# we need to convert it to the original
# array shape.reshaping to get original
# matrice with original shape.
load_original_arr = loaded_arr.reshape(
    loaded_arr.shape[0], loaded_arr.shape[0], loaded_arr.shape[0])

X, Y, Z = np.mgrid[0:101:1, 0:101:1, 0:101:1]
fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=loaded_arr,
    isomin=-0.1,
    isomax=0.8,
    opacity=0.1, # needs to be small to see through all surfaces
    surface_count=7, # needs to be a large number for good volume rendering
    ))
fig.update_layout(scene_xaxis_showticklabels=False,
                  scene_yaxis_showticklabels=False,
                  scene_zaxis_showticklabels=False)
fig.show()







