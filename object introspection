import matplotlib
import seaborn as sns
import pandas as pd
tips = pd.DataFrame({"total_bill":[100], "tip":[15]})
g = sns.JointGrid(x="total_bill", y="tip", data=tips)

for attribute in sorted(g.__dict__):
    print(attribute, ":", g.__dict__[attribute])
    
    
