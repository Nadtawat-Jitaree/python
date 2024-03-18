import pandas as pd

df = pd.read_excel('test.xlsx')
sell = pd.read_excel('sell.xlsx')

#เพิ่ม column
# new = pd.DataFrame([1,2,3,4,5])
# df['New'] = new


#รวม xlsx
df = df.merge(sell)

df['ยอดคงเหลือ'] = df['ตั้งต้น'] + df['เพิ่ม'] - df['ขาย']


print(df)

# df.to_excel('new.xlsx')
# print('success')
