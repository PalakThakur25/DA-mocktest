
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
n = 5000

df = pd.DataFrame({
    "date": pd.to_datetime("2025-01-01")
    + pd.to_timedelta(rng.integers(0, 365, n), unit="D"),
    "region": rng.choice(
        ["North", "South", "East", "West"], n
    ),
    "category": rng.choice(
        ["Electronics", "Clothing", "Home", "Sports"], n
    ),
    "units": rng.integers(1, 10, n),
    "unit_price": rng.uniform(10, 200, n).round(2)
})

df["revenue"] = df["units"] * df["unit_price"]

total_revenue = df["revenue"].sum()
total_orders = len(df)
avg_order_value = df["revenue"].mean()
units_sold = df["units"].sum()

monthly = (
    df.set_index("date")
    .resample("MS")["revenue"]
    .sum()
)

by_category = df.groupby("category")["revenue"].sum().sort_values()
by_region = df.groupby("region")["revenue"].sum().sort_values()

fig = plt.figure(figsize=(14, 9))
fig.patch.set_facecolor("#f4f6f9")

fig.suptitle(
    "SALES ANALYTICS DASHBOARD",
    fontsize=20,
    fontweight="bold",
    y=0.98
)

gs = fig.add_gridspec(
    3, 4,
    height_ratios=[0.8, 2, 2],
    hspace=0.4,
    wspace=0.35
)

kpis = [
    ("TOTAL REVENUE", f"${total_revenue:,.0f}"),
    ("TOTAL ORDERS", f"{total_orders:,}"),
    ("AVG ORDER VALUE", f"${avg_order_value:,.2f}"),
    ("UNITS SOLD", f"{units_sold:,}")
]

for i, (title, value) in enumerate(kpis):
    ax = fig.add_subplot(gs[0, i])
    ax.set_facecolor("white")
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_color("#d9dee7")

    ax.text(
        0.5, 0.68, title,
        ha="center", va="center",
        fontsize=10, color="#555555",
        fontweight="bold"
    )

    ax.text(
        0.5, 0.32, value,
        ha="center", va="center",
        fontsize=17, color="#304ffe",
        fontweight="bold"
    )

ax1 = fig.add_subplot(gs[1, :])
ax1.set_facecolor("white")
ax1.plot(
    monthly.index,
    monthly.values,
    marker="o",
    linewidth=2,
    label="Monthly Revenue"
)
ax1.set_title("Monthly Revenue Trend", fontweight="bold")
ax1.set_ylabel("Revenue ($)")
ax1.grid(True, alpha=0.25)
ax1.tick_params(axis="x", rotation=25)
ax1.legend()

ax2 = fig.add_subplot(gs[2, :2])
ax2.set_facecolor("white")
ax2.barh(
    by_category.index,
    by_category.values
)
ax2.set_title("Revenue by Category", fontweight="bold")
ax2.set_xlabel("Revenue ($)")
ax2.grid(axis="x", alpha=0.25)

ax3 = fig.add_subplot(gs[2, 2:])
ax3.set_facecolor("white")
ax3.bar(
    by_region.index,
    by_region.values
)
ax3.set_title("Revenue by Region", fontweight="bold")
ax3.set_ylabel("Revenue ($)")
ax3.grid(axis="y", alpha=0.25)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

print("\n===== SALES ANALYTICS SUMMARY =====")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${avg_order_value:,.2f}")
print(f"Units Sold: {units_sold:,}")

print("\n===== REVENUE BY CATEGORY =====")
print(by_category.sort_values(ascending=False).round(2).to_string())

print("\n===== REVENUE BY REGION =====")
print(by_region.sort_values(ascending=False).round(2).to_string())

print("\n===== EDA COMPLETED SUCCESSFULLY =====")
