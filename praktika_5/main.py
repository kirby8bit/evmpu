from calculate_sqrt import calc_sqrt

def main():
  #example 1:
  message, result = calc_sqrt(5, 3, 4)
  print(message)
  print(f"результат: {result}")

  #example 2:
  message, result = calc_sqrt(3, 4)
  print(message)
  print(f"результат: {result}")
 
  #example 3:
  message, result = calc_sqrt(5)
  print(message)
  print(f"результат: {result}")

  #example 4:
  message, result = calc_sqrt()
  print(message)
  print(f"результат: {result}")

  #example 5:
  message, result = calc_sqrt(0, 0, 5)
  print(message)
  print(f"результат: {result}")


if __name__== "__main__":
  main()