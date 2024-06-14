import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('employee_data.csv')

df = df[['StockOptionLevel','TotalWorkingYears','Age','JobLevel','MonthlyIncome','YearsWithCurrManager','Attrition']]

X = df.drop(columns='Attrition')
y = df['Attrition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

scaled_x_train = scaler.fit_transform(X_train)
scaled_x_test = scaler.transform(X_test)

scaled_x_train = pd.DataFrame(data=scaled_x_train, columns=X_train.columns)
scaled_x_test = pd.DataFrame(data=scaled_x_test, columns=X_test.columns)

log_reg = LogisticRegression()
log_reg.fit(scaled_x_train, y_train)

y_pred = log_reg.predict(scaled_x_test)

print(f'Accuracy Score of Logistic Regression Model on Employee Data: {accuracy_score(y_test, y_pred)*100:.2f}%')
print()
print(f'Classification Report {classification_report(y_test, y_pred)}')

# Predict New Data Based on User Input

stock_option = int(input('Masukkan level atau tingkatan opsi saham yang diberikan kepada karyawan [1/2/3]: '))
total_years = int(input('Masukkan total tahun pengalaman kerja karyawan: '))
age = int(input('Masukkan umur karyawan: '))
job_level = int(input('Masukkan level atau tingkatan pekerjaan karyawan dalam organisasi [1/2/3/4/5]: '))
monthly_income = int(input('Masukkan pendapatan bulanan karyawan:'))
years_curr = int(input('Masukkan jumlah tahun karyawan telah bekerja dengan manajer saat ini:'))

data = pd.DataFrame(data=[stock_option,total_years,age,job_level,monthly_income,years_curr], index=df.columns[0:6]).T

data_scaled = scaler.transform(data)
data_scaled = pd.DataFrame(data=data_scaled, columns=data.columns)

print()
pred = 'Attrition: Yes' if log_reg.predict(data_scaled) == 1 else 'Attrition: No'
print(f'Hasil Prediksi Attrition Menggunakan Data Baru -> {pred}')
