import pandas as pd


data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

sort_employee =employee.sort_values(by='salary',ascending=False)
second_high_sala =sort_employee['salary'].iloc[1]
print(second_high_sala)


data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})

def sal_cat(salary):
    if salary<20000:
        return 'Low Salary'
    elif 20000<=salary<=50000:
        return 'Average Salary'
    else:
        return 'High Salary'
  
accounts['salary category'] =accounts['income'].apply(sal_cat)
#categories mention so that it does not drop when zero for any category
categories =['Low Salary','Average Salary','High Salary']

accounts['salary category']  =pd.Categorical(accounts['salary category'],categories=categories)
salary_count =accounts['salary category'] .value_counts(dropna=False)

print(salary_count)
