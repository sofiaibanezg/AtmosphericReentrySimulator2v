class ReentrySimulator:
    def __init__(self, capsule, atmosphere):
        self.capsule = capsule
        self.atmosphere = atmosphere
        self.time = 3
        self.dt = 1  # paso de tiempo en segundos
        self.data_log = []

    def run(self):
        while not self.capsule.is_landed():
            self.step()
            self.time += self.dt

    def step(self):
        # 1. Calcular fuerzas (drag y gravedad)
        # 2. Actualizar velocidad y posición
        # 3. Estimar temperatura
        # 4. Guardar datos
        pass