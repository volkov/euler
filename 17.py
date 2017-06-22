def to_letters_0_9(x):
  return {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
  }[x]
def to_letters_10_19(x):
  return {
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'
  }[x]
def to_letters_20_99(x):
  return {
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety'
  }[x//10]+" " + to_letters_0_9(x%10)

def to_letters_0_99(x):
  if x<10: return to_letters_0_9(x)
  if 9<=x<=19: return to_letters_10_19(x)
  if 19<x<=99: return to_letters_20_99(x)

def to_letters_100_999(x):
  result = to_letters_0_9(x//100) + " hundred"
  reminder = x % 100
  if reminder != 0:
    result+=" and "+to_letters_0_99(reminder)
  return result
def to_letters(x):
  if x<100: return to_letters_0_99(x)
  if x==100: return 'one hundred'
  if 100<=x<1000: return to_letters_100_999(x)
  if x==1000: return 'one thousand'
count = 0
for i in range(1000):
  i_string = to_letters(i+1)
  print(i_string)
  count+=len(i_string.replace(" ",""))
print("Letters",count)
