# Calculate the salary of an employed salesperson who earns PLN 2,000 using the shortened version
# of if. Ask him about his seniority, number of hours worked and number of goods sold.
# Name          Value               Condition
# Seniority     10%, the rest 2%    >= 2 [years]
# Sales         25%                 >= 30 [pcs.]
# Activity      8%, the rest 2%     >= 160 [hours] and seniority >= 1 [years]

base = 2000

seniority = int(input("How long you work [years]: "))
sales = int(input("How long products you sell [pcs.]: "))
activity = int(input("How long you work in month [hours]: "))

bonus_seniority = 0.1 if seniority >= 2 else 0.02
bonus_sale = 0.25 if sales >= 30 else 0
bonus_activity = 0.08 if activity >= 160 and seniority >= 1 else 0.02

bonus = base * bonus_seniority + base * bonus_sale + base * bonus_activity

print(f"Your salary is equal: {int(base + bonus)} PLN")
