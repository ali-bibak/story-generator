import copy
import codecs

input_file = 'final_story.txt'
treshhold = 0.8

def lcs(s1, s2):
	row = [0 for s in s2+'.']
	mat = [copy.deepcopy(row) for s in s1+'.']
	for i in range(1,len(s1+'.')):
		for j in range(1,len(s2+'.')):
			if s1[i-1] == s2[j-1]:
				mat[i][j] = max(mat[i-1][j-1]+1,mat[i][j-1],mat[i-1][j])
			else:
				mat[i][j] = max(mat[i-1][j],mat[i][j-1])
	return mat[len(s1)][len(s2)]



if __name__ == '__main__':
	st = codecs.open(input_file, 'r', 'utf-8').read().replace('  ', ' ').replace('\t', ' ').replace('\n', '').split('.')
	res = st[0] + '.'
	last = res
	for i in xrange(1,len(st)):
		PC = lcs(last, st[i]+'.')/(len(st[i]+'.'))
		if PC < treshhold:
			last = st[i]+'.'
			res += last
	f = codecs.open(input_file, 'w', 'utf-8')
	f.write(res)
	f.close()

