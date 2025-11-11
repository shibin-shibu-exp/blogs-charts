import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["Jun", "Jul", "Aug", "Sep", "Oct"]

monthwise_time = [4 + 13/60, 4 + 32/60, 4 + 24/60, 4 + 8/60, 3 + 50/60]
overall_time = [4 + 29/60, 4 + 43/60, 4 + 35/60, 4 + 29/60, 4 + 21/60]

x = np.arange(len(months))

plt.figure(figsize=(10, 6))

plt.bar(x, monthwise_time, color="#FF4500", alpha=0.7, label="Month-wise Time Spent (min)")

plt.scatter(x, overall_time, color="#FF4500", s=100, edgecolor="black", linewidth=0.7, label="Overall Time Spent (min)", zorder=5)

def format_minutes_to_time(y, _):
    mins = int(y)
    secs = int((y - mins) * 60)
    return f"{mins}:{secs:02d}"

ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_minutes_to_time))

y_min = min(min(monthwise_time), min(overall_time)) - 0.1
y_max = max(max(monthwise_time), max(overall_time)) + 0.1
plt.ylim(y_min, y_max)

plt.xticks(x, months)
plt.xlabel("Month")
plt.ylabel("Time Spent (min:sec)")
plt.title("Time Spent", fontsize=14, weight='bold')
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()
