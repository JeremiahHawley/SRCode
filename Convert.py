white = 0
black = 1
red = 2
green = 3
blue = 4


def five_to_two(num):
  decimal_num = 0
  for i, digit in enumerate(reversed(num)):
    decimal_num += int(digit) * (5**i)

  # Convert the decimal number to binary
  binary_num = bin(decimal_num)[2:]

  return binary_num


def two_to_five(num):
  decimal_num = int(num, 2)
  base5_num = ""
  while decimal_num > 0:
    remainder = decimal_num % 5
    base5_num = str(remainder) + base5_num
    decimal_num //= 5

  return base5_num

def rgb_gen(bin):
  file = open("rgb.txt","w")
  data = str(two_to_five(bin))
  for i in range(len(data)):
    if data[i] == "0":
      file.write(",(0,0,0)")
    if data[i] == "1":
      file.write(",(255,255,255)")
    if data[i] == "2":
      file.write(",(255,0,0)")
    if data[i] == "3":
      file.write(",(0,255,0)")
    if data[i] == "4":
      file.write(",(0,0,255)")
  file_data = file.read()
  file.close()
  file = open("rgb.txt","w")
  file_data.replace(',','',1)
  file.write(file_data) 
  file.close();