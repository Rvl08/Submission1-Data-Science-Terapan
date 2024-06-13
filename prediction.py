{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3c6333a7-f955-417b-a3a9-9d158623e19e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "D:\\Programming\\AI_ML\\Dicoding\\Submission\\env\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1509: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
      "D:\\Programming\\AI_ML\\Dicoding\\Submission\\env\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1509: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
      "D:\\Programming\\AI_ML\\Dicoding\\Submission\\env\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1509: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy Score of Logistic Regression Model on Employee Data: 89.12%\n",
      "\n",
      "Classification Report               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.89      1.00      0.94       262\n",
      "           1       0.00      0.00      0.00        32\n",
      "\n",
      "    accuracy                           0.89       294\n",
      "   macro avg       0.45      0.50      0.47       294\n",
      "weighted avg       0.79      0.89      0.84       294\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Masukkan level atau tingkatan opsi saham yang diberikan kepada karyawan [1/2/3]:  2\n",
      "Masukkan total tahun pengalaman kerja karyawan:  4\n",
      "Masukkan umur karyawan:  44\n",
      "Masukkan level atau tingkatan pekerjaan karyawan dalam organisasi [1/2/3/4/5]:  3\n",
      "Masukkan pendapatan bulanan karyawan: 4267\n",
      "Masukkan jumlah tahun karyawan telah bekerja dengan manajer saat ini: 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Hasil Prediksi Attrition Menggunakan Data Baru -> Attrition: No\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score, classification_report\n",
    "\n",
    "df = pd.read_csv('employee_data.csv')\n",
    "\n",
    "df = df[['StockOptionLevel','TotalWorkingYears','Age','JobLevel','MonthlyIncome','YearsWithCurrManager','Attrition']]\n",
    "\n",
    "X = df.drop(columns='Attrition')\n",
    "y = df['Attrition']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "scaler = StandardScaler()\n",
    "\n",
    "scaled_x_train = scaler.fit_transform(X_train)\n",
    "scaled_x_test = scaler.transform(X_test)\n",
    "\n",
    "scaled_x_train = pd.DataFrame(data=scaled_x_train, columns=X_train.columns)\n",
    "scaled_x_test = pd.DataFrame(data=scaled_x_test, columns=X_test.columns)\n",
    "\n",
    "log_reg = LogisticRegression()\n",
    "log_reg.fit(scaled_x_train, y_train)\n",
    "\n",
    "y_pred = log_reg.predict(scaled_x_test)\n",
    "\n",
    "print(f'Accuracy Score of Logistic Regression Model on Employee Data: {accuracy_score(y_test, y_pred)*100:.2f}%')\n",
    "print()\n",
    "print(f'Classification Report {classification_report(y_test, y_pred)}')\n",
    "\n",
    "# Predict New Data Based on User Input\n",
    "\n",
    "stock_option = int(input('Masukkan level atau tingkatan opsi saham yang diberikan kepada karyawan [1/2/3]: '))\n",
    "total_years = int(input('Masukkan total tahun pengalaman kerja karyawan: '))\n",
    "age = int(input('Masukkan umur karyawan: '))\n",
    "job_level = int(input('Masukkan level atau tingkatan pekerjaan karyawan dalam organisasi [1/2/3/4/5]: '))\n",
    "monthly_income = int(input('Masukkan pendapatan bulanan karyawan:'))\n",
    "years_curr = int(input('Masukkan jumlah tahun karyawan telah bekerja dengan manajer saat ini:'))\n",
    "\n",
    "data = pd.DataFrame(data=[stock_option,total_years,age,job_level,monthly_income,years_curr], index=df.columns[0:6]).T\n",
    "\n",
    "data_scaled = scaler.transform(data)\n",
    "data_scaled = pd.DataFrame(data=data_scaled, columns=data.columns)\n",
    "\n",
    "print()\n",
    "pred = 'Attrition: Yes' if log_reg.predict(data_scaled) == 1 else 'Attrition: No'\n",
    "print(f'Hasil Prediksi Attrition Menggunakan Data Baru -> {pred}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
