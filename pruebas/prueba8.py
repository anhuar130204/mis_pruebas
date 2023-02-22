txt = input()

longest=max(txt.split(), key=len)

print(longest)