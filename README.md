## Project Description
A physics-based simulator that models the descent of a space capsule through Earth's atmosphere. It computes altitude, velocity, and temperature over time based on a simplified drag model and visualizes the results using Python and matplotlib.

This project was developed as part of the Programming and Computer Science course in the Aerospace Engineering Program.

## Team Members
- Sofía Gabriela Ibáñez Gil

## How to Set Up and Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/atmospheric-reentry-simulator.git
cd atmospheric-reentry-simulator
```

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Simulation
```bash
python src/main.py
```

### 5. Output
- The simulation will print state updates to the terminal.
- It will display 3 plots: Altitude vs Time, Velocity vs Time, and Temperature vs Time.

## Features
- Object-Oriented structure with `Capsule`, `Atmosphere`, and `ReentrySimulator` classes.
- Tracks altitude, velocity, and estimated external temperature.
- Plots results for clear visualization.
