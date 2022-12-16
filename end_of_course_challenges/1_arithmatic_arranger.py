def arithmetic_arranger(problems, answer=False):

  line1 = str()
  line2 = str()
  line3 = str()
  line4 = str()

  if len(problems) > 5:
    return "Error: Too many problems."

  for prob in problems:
    prob_parts = prob.split()
    value = 0
    if len(prob_parts[0]) > len(prob_parts[2]):
      length = len(prob_parts[0])
      longer = True
    else:
      length = len(prob_parts[2])
      longer = False

    if length > 4:
      return "Error: Numbers cannot be more than four digits."

    try:
      num1 = int(prob_parts[0])
      num2 = int(prob_parts[2])
    except:
      return "Error: Numbers must only contain digits."

    if prob_parts[1] == '+':
      value = num1 + num2
    elif prob_parts[1] == '-':
      value = num1 - num2
    else:
      return "Error: Operator must be '+' or '-'."

    if longer:
      spaces = (len(prob_parts[0]) - len(prob_parts[2])) + 1
    else:
      spaces = 1

    line1 += ((((length + 2) - len(prob_parts[0])) * " ") + prob_parts[0] + "    ")
    line2 += (prob_parts[1] + (" " * spaces) + prob_parts[2] + "    ")
    line3 += (("-" * (length + 2)) + "    ")
    line4 += ((((length + 2) - len(str(value))) * " ") + str(value) + "    ")

  line1 = line1[:-4] + "\n"
  line2 = line2[:-4] + "\n"
  line3 = line3[:-4] if not answer else line3[:-4] + "\n"
  line4 = line4[:-4]

  return (f"{line1}{line2}{line3}{line4}" if answer else f"{line1}{line2}{line3}")
