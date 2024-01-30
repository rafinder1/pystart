emails = 'xd@o2.pl', 'koks@gmail.com', 'kapcer@o2.it', 'xd@o2.pl'

correct_user = set()
for email in emails:
    if '@' in email and ('.pl' in email or '.com' in email):
        correct_user.add(email)

print(f"Start emails: {emails}")
print(f"Correct user: {correct_user}")
