import matplotlib.pyplot as plt

# Data
months = ["Jun", "Jul", "Aug", "Sep", "Oct"]
monthly_visits = [2221, 6155, 11213, 10807, 11533]
cumulative_visits = [15520, 21605, 32818, 43603, 55135] 

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(months, monthly_visits, color="#e97100", alpha=0.7, label="Monthly Visits")
ax1.set_xlabel("Month")
ax1.set_ylabel("Monthly Visits")
ax1.tick_params(axis="y")

ax2 = ax1.twinx()
ax2.plot(months, cumulative_visits, color="#e97100", marker="o", label="Cumulative Visits", linewidth=2)
ax2.set_ylabel("YTD")

plt.title("# of Visits to Section", fontsize=14, weight='bold')
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

plt.tight_layout()
plt.show()
