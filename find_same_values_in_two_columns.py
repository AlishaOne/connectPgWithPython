"""
session_id,email_s,email
tbc83384,23332,23332
bce62622,23375,23375
abc83386,64622,64675
cbc83387,86666,86666
abc83388,45644,45644
abc83389,44509,44508
aac83390,97366,83669
abc83391,86666,83654
bbc83392,97368,64527
zbc83393,97369,97366
abc83394,97370,47563
"""
# ! pip install pandas
import pandas as pd
# ! pip install xlrd
# ! python -m pip install --upgrade pip
import xlrd
from pandas import ExcelWriter as ew

df_orig = pd.read_csv('F:\\downloads\\test_data_v.csv')
print(df_orig.columns)
# print(df_orig[['session_id','email','email_s']])
print("--------------------------------------")
print([e for e in df_orig['email_s'] if e in df_orig['email']])
# print([e1 for e1 in df_orig.email])
# print([e2 for e2 in df_orig.email_s])
df1 = df_orig[df_orig['email_s'].isin(df_orig['email'])]
df2 = df_orig['session_id'][df_orig['email_s'].isin(df_orig['email'])]
print(df1)
print(f"Same emails' session id\n")
print(df2)
#write df1 to csv and excel
df1.to_csv('F:\\downloads\\test_data_v_same_session.csv',encoding='utf-8')
with ew('F:\\downloads\\test_data_v_same_session.xlsx') as writer:
    df1.to_excel(writer,sheet_name='Sheet1')
