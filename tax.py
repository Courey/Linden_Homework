# Single filers
  # 10% $0 to $9,950 10% of taxable income
  # 12% $9,951 to $40,525 $995 plus 12% of the amount over $9,950
  # 22% $40,526 to $86,375 $4,664 plus 22% of the amount over $40,525
  # 24% $86,376 to $164,925 $14,751 plus 24% of the amount over $86,375
  # 32% $164,926 to $209,425 $33,603 plus 32% of the amount over $164,925
  # 35% $209,426 to $523,600 $47,843 plus 35% of the amount over $209,425
  # 37% $523,601 or more $157,804.25 plus 37% of the amount over $523,600

# Head of household
  # 10% $0 to $14,200 10% of taxable income
  # 12% $14,201 to $54,200 $1,420 plus 12% of the amount over $14,200
  # 22% $54,201 to $86,350 $6,220 plus 22% of the amount over $54,200
  # 24% $86,351 to $164,900 $13,293 plus 24% of the amount over $86,350
  # 32% $164,901 to $209,400 $32,145 plus 32% of the amount over $164,900
  # 35% $209,401 to $523,600 $46,385 plus 35% of the amount over $209,400
  # 37% $523,601 or more $156,355 plus 37% of the amount over $523,600

# Married, filing jointly
  # 10% $0 to $19,900 10% of taxable income
  # 12% $19,901 to $81,050 $1,990 plus 12% of the amount over $19,900
  # 22% $81,051 to $172,750 $9,328 plus 22% of the amount over $81,050
  # 24% $172,751 to $329,850 $29,502 plus 24% of the amount over $172,750
  # 32% $329,851 to $418,850 $67,206 plus 32% of the amount over $329,850
  # 35% $418,851 to $628,300 $95,686 plus 35% of the amount over $418,850
  # 37% $628,301 or more $168,993.50 plus 37% of the amount over $628,300

# Married, filing separately
  # 10% $0 to $9,950 10% of taxable income
  # 12% $9,951 to $40,525 $995 plus 12% of the amount over $9,950
  # 22% $40,526 to $86,375 $4,664 plus 22% of the amount over $40,525
  # 24% $86,376 to $164,925 $14,751 plus 24% of the amount over $86,375
  # 32% $164,926 to $209,425 $33,603 plus 32% of the amount over $164,925
  # 35% $209,426 to $314,150 $47,843 plus 35% of the amount over $209,425
  # 37% $314,151 or more $84,496.75 plus 37% of the amount over $314,150

# ^^^ pretend this stuff isn't up there ^^^

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
  for x in range(0, 19):
    print('')
  print('Here is what your income tax is:')
  print(result)
  print('Please pay your taxes')
  for x in range(0, 19):
    print('')
  return result


# comment out both test sections to use the CLI
# ______ this is fake testing ________
# def test_single_bracket_1():
#   status_number = 1
#   income = 9950
#   result = yearly_income(income, status_number)
#   if result == 995.0:
#     print("test_single_bracket_1 success!")
#   else:
#     print("test_single_bracket_1 failure")

# # ______ tests to run ________________
# test_single_bracket_1()


# ________ comment out when runing tests. uncomment to use CLI __________
# This gets the input from the terminal
print('1: single')
print('2: married filing jointly')
print('3: married filing separate')
print('4: head of household')
print('NO LETTERS')
filing_status = input("Please enter number for filing status from the list above:").strip()
income = input("Please input your yearly income here:").strip()
yearly_income(income, filing_status)











