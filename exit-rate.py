import matplotlib.pyplot as plt

# Data
months = ["Jun", "Jul", "Aug", "Sep", "Oct"]
monthwise_exit = [59, 66, 66, 76, 74]
overall_exit = [63, 65, 65, 68, 69]

plt.figure(figsize=(10, 6))

plt.plot(months, monthwise_exit, color="#e97100", marker='o', linewidth=2.5, label="Month-wise Exit Rate")

plt.scatter(months, overall_exit, color="#e97100", edgecolor="black", s=80, label="Overall Exit Rate (per month)")

plt.title("Exit Rate​", fontsize=14, weight='bold')
plt.xlabel("Month")
plt.ylabel("Exit Rate (%)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()