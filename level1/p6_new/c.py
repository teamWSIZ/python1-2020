

s = 'GGACD'
# print(s.startswith('GGA'))
# print(s.startswith('GGGA'))

a = 'GGA'
print(s.startswith(a))
s = s[len(a):]      # odcinamy od s kawałek długości len(a)
print(s)

#,,, w pętli póki len(s) != 0