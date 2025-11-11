import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct']
monthly_kpi = [25.6, 13.7, 21.9, 21.5, 19.3]   
overall_kpi = [16.6, 15.6, 17.8, 18.7, 18.8]   

y = np.arange(len(months))

plt.figure(figsize=(10, 7))

bar_color = "#e97100"   
line_color = "#e97100"  

plt.barh(y, monthly_kpi, color=bar_color, alpha=0.8, label='Monthly KPI Engagement (%)')

plt.plot(overall_kpi, y, color=line_color, marker='o', linewidth=2.5, label='Overall Engagement (%)')

max_val = max(max(monthly_kpi), max(overall_kpi))
plt.xlim(0, max_val + 5)  

plt.xlabel('Engagement (%)', fontsize=12)
plt.ylabel('Month', fontsize=12)
plt.title('% of Visits Engaging with Primary KPIs', fontsize=14, weight='bold')
plt.yticks(y, months)
plt.legend()

for i, val in enumerate(monthly_kpi):
    plt.text(val + 0.5, i, f'{val}%', va='center', fontsize=9, color=bar_color, weight='bold')

for i, val in enumerate(overall_kpi):
    plt.text(val + 0.5, i + 0.15, f'{val}%', va='center', fontsize=8, color=line_color, weight='bold')

plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
