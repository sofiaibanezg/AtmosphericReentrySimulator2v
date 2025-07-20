# src/Atmosphere.py

import math

class Atmosphere:
    def __init__(self):
        self.rho0 = 1.225     # kg/m³ density at sea level
        self.h_scale = 8500   # m, height scale for isothermal atmosphere 

    def get_density(self, altitude):
        """
        Calculate density as a function of altitude (exponential model)
        """
        return self.rho0 * math.exp(-altitude / self.h_scale)

    def __str__(self):
        return "Simplified exponential atmospheric model"
