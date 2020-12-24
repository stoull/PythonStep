# ss = input().split()
# word = sorted(set(ss))
# for i in word:
# 	print(f"{i}:{ss.count(i)}")

ss = input().split()
word_freq = {i : ss.count(i) for i in ss}
dict = sorted(word_freq.items())
for i in dict:
	print("%s:%d"%(i[0],i[1]))