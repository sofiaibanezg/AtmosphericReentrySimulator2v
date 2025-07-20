# src/main.py

from Capsule import Capsule
from Atmosphere import Atmosphere
from Simulator import ReentrySimulator

def main():
    # Crear la cápsula con parámetros: masa (kg), área (m²), coef. de arrastre
    Capsule = Capsule(mass=2000, area=10, drag_coefficient=1.2)

    # Crear el modelo atmosférico
    Atmosphere = Atmosphere()

    # Crear el simulador y correr
    Simulator = ReentrySimulator(capsule, atmosphere, dt=1)
    Simulator.run()

if __name__ == "__main__":
    main()
