import matplotlib.pyplot as plt

# Data
months = ["Jun", "Jul", "Aug", "Sep", "Oct"]
monthwise_bounce = [48, 58, 44, 54, 56]
overall_bounce = [63, 62, 56, 55, 55]

plt.figure(figsize=(10, 6))

plt.plot(months, monthwise_bounce, color="#e97100", marker='o', linewidth=2.5, label="Month-wise Bounce Rate")

plt.scatter(months, overall_bounce, color="#e97100", edgecolor="black", s=80, label="Overall Bounce Rate (per month)")

plt.title("Bounce Rate​", fontsize=14, weight='bold')
plt.xlabel("Month")
plt.ylabel("Bounce Rate (%)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()