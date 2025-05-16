import numpy as np 
import pandas as pd

# وصف المشروع:
# هذا السكربت يقوم بتحميل وتحليل بيانات مبيعات سوبرماركت من ملف CSV.
# يتم استكشاف البيانات مبدئيًا للتعرف على محتوياتها وجودتها،
# ثم تحليل المبيعات حسب الفروع، نوع المنتجات، الجنس، وطرق الدفع.
# كما يتم حساب بعض الإحصائيات الأساسية على عمود "Total" الذي يمثل قيمة المبيعات.

# 1. تحميل البيانات من ملف CSV
data = pd.read_csv("supermarket_sales - Sheet1.csv") 

# 2. استكشاف مبدئي للبيانات
print(data.head())           # عرض أول 5 صفوف من البيانات للاطلاع على شكلها
print(data.describe())       # ملخص إحصائي للبيانات الرقمية
print(data.info())           # معلومات عن الأعمدة وأنواعها وعدد القيم غير الفارغة
print(data.isnull().sum())   # التحقق من وجود قيم مفقودة في الأعمدة
print(data.columns)          # عرض أسماء الأعمدة في مجموعة البيانات

# 3. تحليل المبيعات حسب الفروع
print(data.groupby("Branch")["Total"].mean())    # متوسط المبيعات لكل فرع
print(data.groupby("Branch")["Total"].sum())     # إجمالي المبيعات لكل فرع
print(data["Branch"].value_counts())             # عدد الفواتير لكل فرع

# 4. تحليل حسب نوع المنتج
print(data.groupby("Product line")["Quantity"].sum().sort_values(ascending=False))  # مجموع الكميات المباعة لكل خط منتج
print(data.groupby("Product line")["Total"].mean().sort_values(ascending=False))    # متوسط المبيعات لكل خط منتج

# 5. تحليل حسب الجنس
print(data["Gender"].value_counts())                       # عدد الفواتير لكل جنس
print(data.groupby("Gender")["Total"].mean().sort_values(ascending=False))  # متوسط المبيعات حسب الجنس

# 6. تحليل طرق الدفع
print(data["Payment"].value_counts().sort_values(ascending=False))  # عدد كل طريقة دفع مستخدمة
print(data["Payment"].value_counts().idxmax())                      # أكثر طريقة دفع شيوعًا

# 7. إحصائيات عامة على عمود "Total" (قيمة المبيعات)
print(np.mean(data["Total"]))   # المتوسط العام للمبيعات
print(np.std(data["Total"]))    # الانحراف المعياري للمبيعات (مدى التشتت)
print(np.min(data["Total"]))    # أقل قيمة مبيعات
print(np.max(data["Total"]))    # أعلى قيمة مبيعات
