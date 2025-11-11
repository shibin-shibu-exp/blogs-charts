import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["Aug", "Sep", "Oct"]

desktop_month = [5082, 4071, 3804]
mobile_month  = [6130, 6714, 7728]

desktop_overall = [14581, 24948, 32676]
mobile_overall  = [18235, 18652, 22455]

x = np.arange(len(months))
width = 0.35

fig, ax1 = plt.subplots(figsize=(14, 7))
ax2 = ax1.twinx()  # Secondary y-axis

desktop_color = "#262626"  
mobile_color  = "#FF6600"
desktop_line  = "#4C4C4C"
mobile_line   = "#FF944D"

bars1 = ax1.bar(x - width/2, desktop_month, width, label='Desktop (Monthly)', color=desktop_color, alpha=0.9)
bars2 = ax1.bar(x + width/2, mobile_month, width, label='Mobile (Monthly)', color=mobile_color, alpha=0.9)

ax2.plot(x, desktop_overall, '*--', color=desktop_line, markersize=10, linewidth=1.8, label='Desktop (Overall)')
ax2.plot(x, mobile_overall, '*--', color=mobile_line, markersize=10, linewidth=1.8, label='Mobile (Overall)')

for i, (d, m) in enumerate(zip(desktop_month, mobile_month)):
    ax1.text(x[i] - width/2, d + 80, f"{d}", ha='center', va='bottom', fontsize=9, color=desktop_color)
    ax1.text(x[i] + width/2, m + 80, f"{m}", ha='center', va='bottom', fontsize=9, color=mobile_color)

for i, (d_total, m_total) in enumerate(zip(desktop_overall, mobile_overall)):
    ax2.text(x[i], d_total + 400, f"{d_total}", color=desktop_line, ha='center', fontsize=8)
    ax2.text(x[i], m_total + 400, f"{m_total}", color=mobile_line, ha='center', fontsize=8)

ax1.set_xticks(x)
ax1.set_xticklabels(months)
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Monthly Visits", color='black', fontsize=12)
ax2.set_ylabel("YTD", color='gray', fontsize=12)

ax1.set_title("Device Performance", fontsize=15, weight='bold', color='#262626')
ax1.grid(axis='y', linestyle='--', alpha=0.4)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', frameon=False)

plt.tight_layout()
plt.show()
