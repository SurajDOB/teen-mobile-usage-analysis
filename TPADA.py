import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#Data loading
df = pd.read_excel("D:\DA practice\TeenPhoneAddictionDatasetAnalysis.xlsx")
print(df.head(10))

#check columns names and info
print("\n" * 2) #seperates output from previous response 
print(df.columns)
print("\n" * 2)
print(df.info())

#Cleaning column names
#removing tailing spaces and underscores if any 
df.columns = df.columns.str.strip().str.replace("_", "").str.replace(" ", "")
print("\n===== tails/underscore removed =====\n")
print(df.columns)

#stats summary 
print("\n===== SUMMARY STATISTICS =====\n")
print(df.describe())

#check for missing/null values
print("\n===== missing values =====\n")
print(df.isnull().sum())


##BASIC STATS
#Q1. Avg daily mobile usage 
print("\n" * 2) 
print("Average Daily Usage (Hours):", df['DailyUsageHours'].mean())

#Q2. Avg addiction level gender wise 
print("\n" * 2)
print(df.groupby('Gender')['AddictionLevel'].mean())

#Q3. More app usage daily? Boys or Girls ?
print("\n" * 2)
print(df.groupby('Gender')['AppsUsedDaily'].mean())

#Q4. Which location has highest avg screen time before bed 
print("\n" * 2)
print(df.groupby('Location')['ScreenTimeBeforeBed'].mean().sort_values(ascending=False).head(10))


#CORREALTION ANALYSIS
#Q5. which var correlate with addiction level
print("\n" * 2)
correlation = df.corr(numeric_only=True)
print("\nTop correlations with addiction level:\n")
print(correlation['AddictionLevel'].sort_values(ascending=False).head(10))
#checking for any factors that reduce addiction level
print("\n" *2)
print("\nFactors that reduce/doesn't affect addiction level:\n")
print(correlation['AddictionLevel'].sort_values())


####VISUALISATIONSSSSSS
#setting figure size
plt.figure(figsize=(10,6))
#correlation heatmap
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correaltion heatmap of all numeric var", fontsize=16)
plt.show()
plt.tight_layout()
#Alternative graph
correlation_with_addiction = df.corr(numeric_only=True)['AddictionLevel'].drop('AddictionLevel')  # Get correlations with Addiction Level only
correlation_with_addiction = correlation_with_addiction.sort_values() #Sort them
correlation_with_addiction.plot(kind='barh', title='Factors Correlated with Addiction Level')  #Plot as barchart
plt.xlabel('Correlation Value')
plt.grid(True)
plt.show()

#avg addiction level by gender barplot
sns.boxplot(data=df, x='Gender', y='AppsUsedDaily')
plt.title("Apps Used Daily by gender")
plt.show()
plt.tight_layout()
#avg addiction level by gender bargraph
gender_avg = df.groupby('Gender')['AddictionLevel'].mean()
gender_avg.plot(kind='bar', title='Avg Addiction level by Gender', ylabel='Addiction Level', xlabel='Gender')
plt.show()

#scatterplot : Daily usage vs Addiction level 
sns.scatterplot(data=df, x='DailyUsageHours', y='AddictionLevel', hue='Gender')
plt.title("Daily Usage vs Addiction Level")
plt.show()
#LinePLot : Daily usage vs Adddiction level
usage_group = df.groupby('DailyUsageHours')['AddictionLevel'].mean()
usage_group.plot(kind='line', marker='o', title='Daily Usage vs Addiction Level')
plt.xlabel('Daily Usage Hours')
plt.ylabel('Avg Addiction Level')
plt.grid(True)
plt.show()

boxplot: Apps used daily vs addiction level
sns.boxplot(data=df, x='AddictionLevel', y='AppsUsedDaily')
plt.title("Addiction level vs Daily App Usage")
plt.show()
#Alternate graph 
apps_group = df.groupby('AppsUsedDaily')['AddictionLevel'].mean()
apps_group.plot(kind='bar', title='Avg Addiction level by Apps Used Daily')
plt.xlabel('Apps Used Daily')
plt.ylabel('Avg Addiction Level')
plt.grid(True)
plt.show()