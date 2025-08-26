import pandas

workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Machine Learning Yandex\\Lesson 1\\"
data = pandas.read_csv(workdir + 'titanic.csv', index_col='PassengerId')

# male and female counts - 1 Quiz
male_count = data.Sex[data['Sex'] == 'male'].count()
female_count = data.Sex[data['Sex'] == 'female'].count()
print((male_count, female_count))

# percent of survived passengers - 2 Quiz
peoples_total = data['Survived'].count()
survived = data.Survived[data['Survived'] == 1].count()
print((round(survived * 100.0 / peoples_total, 2)))

# percent of 1-st class passengers
first_class = data.Pclass[data['Pclass'] == 1].count()
print((round(first_class * 100.0 / peoples_total, 2)))

# mean and mediana of passengers age
mean_age = data['Age'].mean()
median_age = data['Age'].median()
print((round(mean_age,2), round(median_age,2)))

# Pearson's correlation between siblings and Parents
correlation = data.SibSp.corr(data.Parch,'pearson')
print((round(correlation,2)))

# Most popular female name onboard
final = data.Name[data['Sex'] == 'female'].str.extract(r'.*Mrs.[^(]*\((\w+)|.*Miss.\s*(\w+)|.*Lady.[^(]*\((\w+)|.*Dr.\s*(\w+)}')
print((final[1].value_counts().head(2)))
