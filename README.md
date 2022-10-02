# Effective_Material_Property_Prediction
- this project is to predict effective material property of particle-reinforced composite materials
- the input variables are 3D RVE model consist of spherical inclusions with varied size and matrix phase, the y variable is the effective material property including elastic modulus, shear modulus and Possion's ratio in three directions
- deep convolution neural work is applied for prediction
- transfer learning is applied for predicting RVE with higher volume fraction.

# Description for each file
- **training_model.py**: Data processing, training and postprocessing scripts ;
- **saved_model**: The model with best performance on validation set.
- **gallery**: Some figures.


