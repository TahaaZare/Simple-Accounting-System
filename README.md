# 💰 Personal Finance Manager | مدیر مالی شخصی

A simple yet powerful command-line based finance manager built with Python.  
ابزاری ساده اما قدرتمند برای مدیریت درآمد و هزینه‌های شخصی در خط فرمان با استفاده از پایتون.

---

## 📦 Features | ویژگی‌ها

✅ Add income and expenses with category, description, and timestamp  
✅ افزودن درآمد و هزینه با دسته‌بندی، توضیح و زمان ثبت

✅ Automatically stores data in a JSON file  
✅ ذخیره‌سازی خودکار اطلاعات در فایل JSON

✅ View full transaction history  
✅ مشاهده کامل سوابق تراکنش‌ها

✅ View summary of total income, expenses, and current balance  
✅ مشاهده خلاصه درآمدها، هزینه‌ها و موجودی نهایی

✅ Modular and easy to extend  
✅ ساختار ماژولار و قابل توسعه

---

## 📁 File Structure | ساختار فایل

finance-manager/
├── finance_manager.py # Main script file
├── finance_data.json # JSON file to store income and expense data
└── README.md # Project documentation (this file)

---
## 🖥 Preview | پیش‌نمایش

```bash
Choose an action (add_income, add_expense, show_summary, show_data, exit): add_income
Enter income amount: 5000
Enter income category: Salary
Enter description: June salary

Choose an action (add_income, add_expense, show_summary, show_data, exit): add_expense
Enter expense amount: 1200
Enter expense category: Rent
Enter description: June rent

Choose an action (add_income, add_expense, show_summary, show_data, exit): show_summary
Total Income: 5000.0, Total Expenses: 1200.0, Balance: 3800.0

