import pandas as pd
emp_details = {'employee':{'dev':{'ID':'001','salary':'12000'},'kumar':{'ID':'002','salary':'13000'}}}
print(emp_details)
df = pd.DataFrame(emp_details['employee'])
print(df)