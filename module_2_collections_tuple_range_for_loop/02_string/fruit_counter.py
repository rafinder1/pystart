text = '12 kg apples, 10 kg pear, 20 kg plum'

res = sum(int(i) for i in text.split() if i.isdigit())

print(res)
