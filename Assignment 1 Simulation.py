import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime  # <- New import for timestamp

# Experiment parameters
container_capacity = 500  # ml
collection_time = 180      # seconds (3 minutes)
n_trials = 30              # Number of experimental trials

# Flow rate parameters (ml/s)
max_safe_flow = (container_capacity / collection_time) * 0.8  # 80% of max flow
flow_rates = {
    'low': np.random.normal(1.2, 0.2, 10),
    'medium': np.random.normal(2.0, 0.3, 10),
    'high': np.random.normal(max_safe_flow, 0.4, 10)
}

# Simulate experimental results
results = []
for flow_type in ['low', 'medium', 'high']:
    for rate in flow_rates[flow_type]:
        collected = rate * collection_time
        results.append({
            'Trial': len(results)+1,
            'Flow Type': flow_type.capitalize(),
            'Flow Rate (ml/s)': round(rate / 10) * 10,
            'Collected (ml)': min(round(collected / 10) * 10, container_capacity)
        })

# Create DataFrame with results
df = pd.DataFrame(results)

# Print results table
print("Experimental Results Table:")
print(df.to_string(index=False))



# Visualization setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Box plot of results
df.boxplot(column='Collected (ml)', by='Flow Type', ax=ax1)
ax1.set_title('Water Collection Distribution by Flow Rate')
ax1.set_ylabel('Milliliters (ml)')

# Animation setup
ax2.set_xlim(0, collection_time)
ax2.set_ylim(0, container_capacity)
ax2.set_title('Virtual Water Collection Simulation')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Collected Water (ml)')
ax2.grid(True)

water_level, = ax2.plot([], [], lw=2)
time_text = ax2.text(0.05, 0.95, '', transform=ax2.transAxes)
level_text = ax2.text(0.75, 0.95, '', transform=ax2.transAxes)

def init():
    water_level.set_data([], [])
    time_text.set_text('')
    level_text.set_text('')
    return water_level, time_text, level_text

def animate(i):
    current_time = i * 0.5
    flow_rate = 2.0  # Example flow rate (ml/s)
    collected = min(flow_rate * current_time, container_capacity)
    
    water_level.set_data(np.linspace(0, current_time, 100), 
                        np.linspace(0, collected, 100))
    time_text.set_text(f'Time: {min(current_time, collection_time):.1f}s')
    level_text.set_text(f'Water: {round(collected / 10) * 10}ml')  # Rounds to nearest 10
    return water_level, time_text, level_text

# Create and show animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=int(collection_time*2), interval=20, blit=True)
plt.tight_layout()
plt.show()  # This will display the animation in VS Code

