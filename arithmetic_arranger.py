import re

def arithmetic_arranger(problem_list, showanswer=False):
  lst1 = list()
  lst2 = list()
  lstdash = list()
  lstresults = list()
  arranged_problems = ''

  # situations that will return an error
  if len(problem_list) > 5:
    return 'Error: Too many problems.'
  
  for problem in problem_list:
    items = problem.split()
    if len(items) != 3: 
      return 'Invalid input format'

    if not (items[1] == '+' or items[1] == '-'):
      return "Error: Operator must be '+' or '-'."

    if len(re.findall('[^ 0-9-+]', problem)) > 0 :
      return 'Error: Numbers must only contain digits.'

    if len(items[0]) > 4 or len(items[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    # defines the number of '-', find len of largest number + 1 space + 1 operator
    dashx = max(len(items[0]), len(items[2])) + 1 + 1

    # append all lists through for loop
    lstdash.append('-' * dashx)
    lst1.append((' ' * (dashx - len(items[0]))) + items[0])
    lst2.append(items[1] + (' ' * (dashx - 1 - len(items[2]))) + items[2])
    result = str(eval(items[0]+items[1]+items[2]))
    lstresults.append(' ' * (dashx - len(result)) + result)
    # end of for loop

  # construct each line in result
  line1 = '    '.join(lst1)
  line2 = '\n' + '    '.join(lst2)
  line3 = '\n' + '    '.join(lstdash)
  line4 = '\n' + '    '.join(lstresults)

  # the default case would be not displaying results 
  arranged_problems = line1 + line2 + line3
  if showanswer == True: arranged_problems = arranged_problems + line4

  return arranged_problems
