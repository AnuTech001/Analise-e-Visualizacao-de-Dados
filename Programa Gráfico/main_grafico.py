import matplotlib.pyplot as plt

# Horários (X) e Temperaturas (Y)
horarios = list(range(25))
temperaturas = [15 + (x if x <= 12 else 24 - x) for x in range(25)]

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(horarios, temperaturas, label="Temperatura (°C)", marker="o")
plt.title("Evolução da Temperatura ao Longo do Dia")
plt.xlabel("Horário (h)")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.legend()
plt.show()
