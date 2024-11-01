while True:
  while True:
    try:
      frst_number = float(input("enter the frst number: "))
      break
    except ValueError:
      print("invalid input. please enter a numeric value")
  while True:
    try:
      input_a = input("enter the operation: ")
      if input_a in ("+", "-", "/", "*"):
        break
      else:
        raise ValueError
    except ValueError:
      print("invalid operator, please enter +,-,/,*")
  while True:
    try:
      scend_number = float(input("enter the scend number: "))
      if scend_number == 0 and input_a == "/":
        raise ZeroDivisionError
      break
    except ValueError:
      print("invalid input. please enter a numeric value")
    except ZeroDivisionError:
      print("cannot divide by zero, please enter another numeric value")
  if input_a == "+":
    result = frst_number + scend_number
  elif input_a == "-":
    result = frst_number - scend_number
  elif input_a == "*":
    result = frst_number * scend_number
  elif input_a == "/":
    result = frst_number / scend_number
  else:
    result = None
  if result != None:
    print(result)
  else:
    print("invalid operator")
  while True:
    repeat = input("do you want to perform another operation (y/n): ")
    if repeat == "n" or repeat == "N"or repeat == "y" or repeat == "Y":
      break
    else:
      print("plesae enter y or n:")
  if repeat == "n" or repeat == "N":
    print("Thanks for nothing")
    break
