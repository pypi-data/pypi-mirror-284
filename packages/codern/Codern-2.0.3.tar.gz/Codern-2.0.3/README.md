# send_email

`send_email` یک کتابخانه Python است که برای ارسال ایمیل‌ها از طریق API سایت [api-free.ir](https://api-free.ir) طراحی شده است. این کتابخانه به شما امکان می‌دهد که به راحتی و به سرعت ایمیل‌های خود را ارسال کنید.

## نصب

برای نصب این کتابخانه، می‌توانید از `pip` استفاده کنید. دستور زیر را در ترمینال خود اجرا کنید:

```bash
pip install git+https://github.com/Mahditerorist/send_email.git
```
**استفاده**
در زیر یک مثال ساده برای استفاده از این کتابخانه آورده شده است:

```python
Copy code
from send_email import Email

# تنظیمات ایمیل
setup = Email(
    To='mahdiahmadi.1208@gmail.com',
    text='hi',
    Title='Codern',
    Token=None,
    Input='iran'
)

# ارسال ایمیل
result = setup.Send()
print(result)
```
مثال عملی
```python
Copy code
from send_email import Email

# تنظیمات ایمیل
to_email = 'recipient@example.com'
text_content = 'این یک ایمیل تستی است.'
email_title = 'سلام!'
api_token = 'your_api_token_here'
input_type = 'info'

# ساخت نمونه‌ای از کلاس Email
email = Email(
    To=to_email,
    text=text_content,
    Title=email_title,
    Token=api_token,
    Input=input_type
)

# ارسال ایمیل
result = email.Send()
if result:
    print('ایمیل با موفقیت ارسال شد!')
else:
    print('خطا در ارسال ایمیل')

```
# پارامترها
1. To: آدرس ایمیل گیرنده.
2. text: متن ایمیل.
3. Title: عنوان ایمیل.
4. Token: توکن احراز هویت برای استفاده از API. برای دریافت توکن، باید در سایت api-free.ir ثبت‌نام کنید و توکن مخصوص خود را دریافت کنید.
5. Input: نوع ورودی که می‌تواند یکی از مقادیر 'info', 'app', 'Login', 'support' باشد.
راهنمای کامل
1. ثبت‌نام در سایت api-free.ir
ابتدا به آیدی rubika.ir/bot_token بروید آنجا می‌توانید توکن API خود را دریافت کنید.

2. نصب کتابخانه
با استفاده از دستور pip کتابخانه را نصب کنید:

```bash
Copy code
pip install git+https://github.com/Mahditerorist/send_email.git
```
3. استفاده از کتابخانه
یک فایل Python جدید ایجاد کنید و کد زیر را در آن قرار دهید:

```python
Copy code
from send_email import Email

# تنظیمات ایمیل
setup = Email(
    To='mahdiahmadi.1208@gmail.com',
    text='hi',
    Title='Codern',
    Token=None,
    Input='iran'
)

# ارسال ایمیل
result = setup.Send()
print(result)
```
4. اجرای کد
فایل Python خود را اجرا کنید تا ایمیل ارسال شود:

```bash
Copy code
python your_file_name.py
```
مشکلات متداول
1. خطای اتصال به API
اگر با خطای اتصال به API مواجه شدید، مطمئن شوید که به اینترنت متصل هستید و آدرس API به درستی وارد شده است.

2. خطای احراز هویت
اگر با خطای احراز هویت مواجه شدید، مطمئن شوید که توکن API را به درستی وارد کرده‌اید و توکن معتبر است.

مشارکت
اگر مایل به مشارکت در توسعه این کتابخانه هستید، می‌توانید مخزن را فورک کرده و تغییرات خود را از طریق Pull Request ارسال کنید. هر گونه کمک و پیشنهاد استقبال می‌شود.

مجوز
این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر فایل LICENSE را مشاهده کنید.

برای هر گونه سوال یا مشکل، می‌توانید از طریق api-free.ir با ما در تماس باشید.
