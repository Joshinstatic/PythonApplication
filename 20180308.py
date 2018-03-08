import pandas
titannic = pandas.read_csv("titanic_train.csv")
titanic.head 3
print titanic.describe() #按列也就是按特征进行分析
titanic["Age"] = titanic["Age"].fillna(titanic["Age".median()])#填充缺失值
print titanic.describe()
print titanic["Sex"].unique()#查看性别
titanic.loc[titanic["Sex"] == "male", Sex] = 0 #将str值转换成int值
titanic.loc[titanic["Sex"] == "female", Sex] = 1
print titanic["Embarked"].unique()#查看性别
titanic["Embarked"] = titanic["Embarked"].fillna("S")
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2





