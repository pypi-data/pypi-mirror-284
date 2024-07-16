import numpy as np
from tensorflow.keras.models import load_model
# from importlib.resources import files
# import udirect
import os

class predictiveModel:
    '''
    This class implements the modifier of moments model presented in Lilienkamp and Weatherill (2024, in prep.)
    to provide adjustments for the mean and the standard deviation of ground motion predictions to incorporate
    rupture forward directivity.

    '''
    def __init__(self):
        self.model_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'directivity_model')
        self.model = load_model(self.model_path, compile=False)
        self.xmin_file = os.path.join(self.model_path, 'xmin.npy')
        self.xmax_file = os.path.join(self.model_path, 'xmax.npy')
        self.xmin = np.load(self.xmin_file)[np.array([0, 1, 6, 5, 2, 8, 7, 9])]
        self.xmax = np.load(self.xmax_file)[np.array([0, 1, 6, 5, 2, 8, 7, 9])]
        self.ymin = np.array([-0.73322594165802, 0])
        self.ymax = np.array([0.8272385001182556, 0.5207511782646179])

    def predict(self, input):
        '''
        input : array_like
                Input array of shape (256, 256, 8), where the 8 channels contain:
                1: Rupture plane distance (km)
                2: Joyner-Boore distance (km)
                3: GC2-U coordinate (km)
                4: GC2-T coordinate (km)
                5: ry0 coordinate (km)
                6: Magnitude
                7: Style of faulting (one of [0, 1]) 0: dip slip; 1: strike slip
                8: Response period T (one of [0.75, 1.00, 1.25, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 7.50, 10.00] in seconds)

        output : array_like
                 Output array of shape (256, 256, 2), where the 2 channels provide:
                 1: The modifier of the ground motion mean (natural log units)
                 2: The modifier of the ground motion std (natural log units)
        '''
        input_normed = ((input - self.xmin) / (self.xmax - self.xmin)).reshape(1, 256, 256, 8)
        output_normed = self.model.predict(input_normed)
        output = output_normed * (self.ymax - self.ymin) + self.ymin

        return output[0, ...]
        



