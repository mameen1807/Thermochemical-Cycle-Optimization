# thermochemical_cycle_optimization.py

import numpy as np
import matplotlib.pyplot as plt

# ---------------- Thermochemical reaction example ----------------
# Example: metal oxide <-> reduced oxide + oxygen (simplified)
delta_H = 250e3  # J/mol, reaction enthalpy
delta_S = 300    # J/mol.K, reaction entropy
R = 8.314        # J/mol.K

# Temperature range
T = np.linspace(600, 1200, 200)  # K

# Equilibrium pressure using van't Hoff relation
P_eq = np.exp((delta_S / R) - (delta_H / (R * T)))  # atm (simplified)

# Energy density for a given mass
mass_material = 40  # kg
molar_mass = 100    # g/mol, example
moles_material = mass_material * 1000 / molar_mass
energy_stored = moles_material * delta_H  # J

# ---------------- Plots ----------------
plt.figure(figsize=(10,4))

# P-T curve
plt.subplot(1,2,1)
plt.plot(T, P_eq)
plt.xlabel("Temperature (K)")
plt.ylabel("Equilibrium Pressure (atm)")
plt.title("Equilibrium Pressure vs Temperature")
plt.grid(True)

# Energy stored bar chart
plt.subplot(1,2,2)
plt.bar(['Stored Energy'], [energy_stored/1e6], color='red')
plt.ylabel("Energy (MJ)")
plt.title(f"Energy Stored in {mass_material} kg Material")
plt.grid(axis='y')

plt.tight_layout()
plt.show()

# Optional: calculate equilibrium temperature at set pressures
pressures_to_check = [1, 5, 10]  # atm
T_eq_for_P = delta_H / (delta_S - R * np.log(pressures_to_check))
for p, t_eq in zip(pressures_to_check, T_eq_for_P):
    print(f"Equilibrium temperature at P={p} atm: {t_eq:.1f} K")
