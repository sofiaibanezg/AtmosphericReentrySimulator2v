# src/main.py

from Capsule import Capsule
from Athmosphere import Atmosphere
from Reentrysimulator import ReentrySimulator
import matplotlib.pyplot as plt

def main():
    # Create the capsule with mass (kg), cross-sectional area (m²), and drag coefficient

    caps  = Capsule(mass=2000, area=10, drag_coefficient=1.2)

    # Create the atmosphere model
    atms = Atmosphere()

    # Create the simulator with a time step of 1 second
    rs = ReentrySimulator(caps, atms, dt=1)

    # Run the simulation and plot the results
    rs.run()
    rs.plot_results()

if __name__ == "__main__":
    main()
