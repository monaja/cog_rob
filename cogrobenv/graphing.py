import matplotlib.pyplot as plt
import numpy as np

# --- IMPORTANT: Replace these values with your actual data ---
# Categories for the x-axis
categories = ['Body', 'Floor']

# Data for the LEFT plot (Rate of Touch) - ESTIMATED FROM IMAGE
rate_means = np.array([13.5, 7.5]) # Approximate mean values
rate_std_devs = np.array([7.5, 4.0]) # Approximate standard deviations

# Data for the RIGHT plot (Duration of Touch) - ESTIMATED FROM IMAGE
duration_means = np.array([3200, 4800]) # Approximate mean values
duration_std_devs = np.array([2200, 5000])# Approximate standard deviations
# --- End of data section ---

# Set up the figure and axes for two side-by-side plots
# figsize=(10, 5) makes the figure wider to accommodate both plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# --- Plot 1: Rate of Touch (Left) ---
x_pos = np.arange(len(categories)) # the label locations [0, 1]

# Create bars with error bars (yerr=standard deviation)
ax1.bar(x_pos, rate_means, yerr=rate_std_devs,
        align='center', alpha=0.9, ecolor='black', capsize=10, color='black') # Use black color like image

# Set labels and title
ax1.set_ylabel('Rate of Touch (per minute)')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(categories)
ax1.set_title('Mean rate of touches') # Optional title
ax1.set_ylim(0, 25) # Set y-axis limit to match the image

# Remove top and right spines for cleaner look (optional)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# --- Plot 2: Duration of Touch (Right) ---

# Create bars with error bars
ax2.bar(x_pos, duration_means, yerr=duration_std_devs,
        align='center', alpha=0.9, ecolor='black', capsize=10, color='black') # Use black color

# Set labels and title
ax2.set_ylabel('Duration of Touch (ms)')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(categories)
ax2.set_title('Mean duration of touches') # Optional title
ax2.set_ylim(0, 12000) # Set y-axis limit to match the image

# --- Replicate right-side Y-axis for the second plot ---
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

# Remove top and left spines for cleaner look (optional)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)


# Improve layout to prevent labels overlapping
plt.tight_layout()

# Display the plot
plt.show()