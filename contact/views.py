# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.conf import settings
# from .forms import ContactForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact = form.save()  # حفظ البيانات في قاعدة البيانات
#             print("done......." , contact.name , contact.email)
#             # إرسال الإيميل
#             send_mail(
#                 subject=f"رسالة جديدة من {contact.name}",
#                 message=contact.message,
#                 from_email=contact.email,
#                 recipient_list=[settings.DEFAULT_FROM_EMAIL],  # ضع إيميلك هنا
#             )

#             return redirect('success')  # صفحة نجاح
#     else:
#         form = ContactForm()

#     return render(request, 'pages/form.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:  # لو البيانات موجودة
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            print("✅ البيانات وصلت: ", name, email, message)
            return redirect('contact')  # غير 'contact' بالاسم اللي انت مسمي بيه ال url
        else:
            print("⚠️ مفيش بيانات اتبعت!")

    return render(request, 'pages/form.html')


