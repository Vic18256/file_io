f = open('newtextfile.txt', 'a')
lines = ['This', 'is', 'the', 'New', 'World']
text = '\n'.join(lines)
f.writelines(text)
f.close()