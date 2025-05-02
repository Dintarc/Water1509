import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Your provided data
data = {
    'Trial': list(range(1, 31)),
    'Flow Type': ['Low']*10 + ['Medium']*10 + ['High']*10,
    'Flow Rate (ml/s)': [0]*30,
    'Collected (ml)': [230, 200, 220, 230, 250, 180, 220, 290, 210, 220,
                      400, 330, 480, 260, 420, 340, 340, 390, 330, 260,
                      370, 250, 290, 470, 300, 410, 400, 330, 240, 420]
}

# Create DataFrame
df = pd.DataFrame(data)

# Export to Excel
excel_filename = "water_collection_experiment_results.xlsx"
df.to_excel(excel_filename, index=False)
print(f"Excel file saved as: '{excel_filename}'")

# Visualization (kept as per your request)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Box Plot
df.boxplot(column='Collected (ml)', by='Flow Type', ax=ax1)
ax1.set_title('Water Collection by Flow Type')
ax1.set_ylabel('Volume (ml)')

# Animation Setup
container_capacity = 500
collection_time = 180
ax2.set_xlim(0, collection_time)
ax2.set_ylim(0, container_capacity)
ax2.set_title('Water Collection Simulation')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Volume (ml)')
ax2.grid(True)

line, = ax2.plot([], [], lw=2, color='blue')
time_text = ax2.text(0.02, 0.95, '', transform=ax2.transAxes)
vol_text = ax2.text(0.7, 0.95, '', transform=ax2.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    vol_text.set_text('')
    return line, time_text, vol_text

def animate(i):
    t = i * 0.5
    vol = min(2.5 * t, container_capacity)  # Adjusted for better visualization
    line.set_data(np.linspace(0, t, 100), np.linspace(0, vol, 100))
    time_text.set_text(f'Time: {t:.1f}s')
    vol_text.set_text(f'Volume: {int(vol)}ml')
    return line, time_text, vol_text

ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=int(collection_time * 2), interval=20, blit=True
)

plt.tight_layout()
plt.show()