import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.countplot(x="sex",
              data=tips)
plt.title("Count of fender in dataset")
plt.show()
