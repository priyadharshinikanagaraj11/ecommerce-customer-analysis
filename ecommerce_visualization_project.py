#Project 
#Objective
#This project aims to explore customer behavior and spending patterns to derive business insights that can help improve revenue and customer retention.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E-commerce Customer Behavior - Sheet1.csv")

print(df.head())
print(df.describe())
print(df.info())

#Which membership earns most money💰?
revenue = df.groupby('Membership Type')['Total Spend'].sum()
highest = revenue.idxmax()
print(highest, "members generate highest revenue")

#Do discounts increase spending?
discount_avg = df.groupby('Discount Applied')['Total Spend'].mean()

with_discount = discount_avg[True]
without_discount = discount_avg[False]

if with_discount > without_discount:
    print("Yes, discounts increase spending.")
elif with_discount < without_discount:
    print("No, discounts do not increase spending.")
else:
    print("Discounts have no impact on spending.")

#Which city spends the most?
city_spend = df.groupby('City')['Total Spend'].sum()
top_city = city_spend.idxmax()

print(f"{top_city} spends the most.")

#Charts
#Revenue By Membership - Bar Chart
import matplotlib.pyplot as plt

# Group data
membership_revenue = df.groupby('Membership Type')['Total Spend'].sum()

# Create figure
plt.figure(figsize=(7,5))

# Plot
plt.bar(
    membership_revenue.index,
    membership_revenue.values,
    color=['blue', 'orange', 'green']
)

# Labels & Title
plt.title("Revenue by Membership Type", fontsize=14)
plt.xlabel("Membership Type")
plt.ylabel("Total Revenue")

# Style
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()

#Customer Satisfaction Distribution - Pie Chart
# Count data
satisfaction_counts = df['Satisfaction Level'].value_counts()

# Create figure
plt.figure(figsize=(6,6))

# Plot
plt.pie(
    satisfaction_counts.values,
    labels=satisfaction_counts.index,
    autopct='%1.1f%%',
    colors=['green', 'yellow', 'red'],
    startangle=90
)

# Title
plt.title("Customer Satisfaction Distribution")

plt.show()

#Age vs Total Spend - Scatter Plot
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

# Filter each membership type
gold = df[df['Membership Type'] == 'Gold']
silver = df[df['Membership Type'] == 'Silver']
bronze = df[df['Membership Type'] == 'Bronze']

# Plot separately
plt.scatter(gold['Age'], gold['Total Spend'],
            color='green', label='Gold', alpha=0.6, edgecolors='black')

plt.scatter(silver['Age'], silver['Total Spend'],
            color='blue', label='Silver', alpha=0.6, edgecolors='black')

plt.scatter(bronze['Age'], bronze['Total Spend'],
            color='brown', label='Bronze', alpha=0.6, edgecolors='black')

plt.title("Age vs Total Spend by Membership Type")
plt.xlabel("Age")
plt.ylabel("Total Spend")

plt.legend(title="Membership Type")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

#Conclusion
#The analysis reveals that membership type, discounts, city, and customer demographics significantly influence spending behavior. 
#Gold members and specific customer segments contribute the most revenue, while discount strategies positively impact purchasing patterns. 
#These insights can help businesses improve targeting, retention, and overall profitability.




