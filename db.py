import sqlite3

# إنشاء اتصال بقاعدة البيانات
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

# إنشاء جدول لتخزين الحسابات إذا لم يكن موجودًا
c.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        account TEXT
    )
''')

# دالة لإضافة حساب جديد
def add_account(account):
    with conn:
        c.execute("INSERT INTO accounts (account) VALUES (:account)", {'account': account})

# دالة لاسترجاع جميع الحسابات
def get_all_accounts():
    c.execute("SELECT * FROM accounts")
    return c.fetchall()

# دالة لحذف حساب
def delete_account(account_id):
    with conn:
        c.execute("DELETE FROM accounts WHERE id = :id", {'id': account_id})

# مثال على استخدام الدوال
add_account("example_account")
all_accounts = get_all_accounts()
for account in all_accounts:
    print(account)

# إغلاق الاتصال بقاعدة البيانات عند الانتهاء
conn.close()
