s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
#here the length is comming 2 but it should come 3 because the value are differnt.
#but .. 20==20.0 , it give true in python .( its very imp question in interview.)