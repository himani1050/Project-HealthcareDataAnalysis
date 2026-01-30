import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/features.csv")

sns.barplot(x='sms_received', y='no_show', data=df)
plt.title("No-show Rate by SMS Reminder")
plt.show()

sns.boxplot(x='age_group', y='waiting_days', data=df)
plt.title("Waiting Days by Age Group")
plt.show()
