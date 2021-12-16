#!/bin/env python3
def yearly_income(income, status_number):
  income = int(income)
  status_number = int(status_number)
  result = 0
  if status_number != (2 | 4):
    if 0 <= income <= 9950:
      result = (income * .1)
    elif 9951 <= income <= 40525:
      result = ((income - 9950) * .12 + 995)
    elif 40526 <= income <= 86375:
      result = ((income - 40525) * .22 + 4664)
    elif 86376 <= income <= 164925:
      result = ((income - 86375) * .24 + 14751)
    elif 164926 <= income <= 209425:
      result = ((income - 164925) * .32 + 33603)
    elif (209426 <= income <= 523600) & (status_number == 1):
      result = ((income - 209425) * .35 + 47843)
    elif (209426 <= income <= 314150) & (status_number == 3):
      result = ((income - 209425) * .35 + 47843)
    elif (523601 <= income) & (status_number == 1):
      result = ((income - 523600) * .37 + 157804)
    elif (314151 <= income) & (status_number == 3):
      result = ((income - 314150) * .37 + 84496.75)
  if status_number == (2):
    if 0 <= income <= 19900:
      result = (income * .1)
    elif 19901 <= income <= 81050:
      result = ((income - 19900) * .12 + 1990)
    elif 40526 <= income <= 172750:
      result = ((income - 81050) * .22 + 9328)
    elif 172751 <= income <= 329850:
      result = ((income - 172750) * .24 + 29502)
    elif 329851 <= income <= 418850:
      result = ((income - 329850) * .32 + 67206)
    elif (418851 <= income <= 628300):
      result = ((income - 418850) * .35 + 95686)
    elif (628301 <= income):
      result = ((income - 628300) * .37 + 168993.5)
  if status_number == (4):
    if 0 <= income <= 14200:
      result = (income * .1)
    elif 14201 <= income <= 54200:
      result = ((income - 14200) * .12 + 1420)
    elif 54201 <= income <= 86350:
      result = ((income - 54200) * .22 + 6220)
    elif 86351 <= income <= 164900:
      result = ((income - 86350) * .24 + 13293)
    elif 164901 <= income <= 209400:
      result = ((income - 164900) * .32 + 32145)
    elif (209401 <= income <= 523600):
      result = ((income - 209400) * .35 + 46385)
    elif (523601 <= income):
      result = ((income - 523600) * .37 + 156355)
  for x in range(0, 21):
    print('')
  print('Here is what your income tax is:')
  print(result)
  return result

def confirm_comprehension(taxes, confirmation):
  while confirmation == 'n':
    print('You can go to the website https://www.1040paytax.com/ and pay ${placeholder} or you can call 888-877-0450 on your phone and pay there'.format(placeholder=taxes))
    confirmation_input = input("Do you understand how to now? (y/n):").strip()
    confirmation = confirm_comprehension(taxes, confirmation_input)
  print('Great! Now go pay your taxes or the IRS will come for you.')

print('1: single')
print('2: married filing jointly')
print('3: married filing separate')
print('4: head of household')
print('NO LETTERS')
filing_status = input("Please enter number for filing status from the list above:").strip()
income = input("Please input your yearly income here:").strip()
taxes = yearly_income(income, filing_status)
confirmation_input = input("Do you understand how to pay your taxes? (y/n):").strip()
confirmation = confirm_comprehension(taxes, confirmation_input)











