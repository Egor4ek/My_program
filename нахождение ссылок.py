print('обнаружение ссылок и тд')
s=input('введите тект ')
words=s.split(',') 
for w in words:
	n=w.find ('@')
	if n!=-1:
		print('в строке присутствует @mail: ' +str(w))
a=input()
