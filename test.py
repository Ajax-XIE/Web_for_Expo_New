import pandas as pd

expo_activity_change = pd.read_excel("Expo_Plan.xlsx")


print([expo_activity_change['Date'][i] + expo_activity_change['Expo'][i] for i in list(range(len(expo_activity_change)))])