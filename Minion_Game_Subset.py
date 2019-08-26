#https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def minion_game(s):
    vowel = "AEIOU"
    kevin = 0
    stuart = 0
    for i in range(len(s)):
        if s[i] in vowel:
            kevin += (len(s)-i)
        else:
            stuart += (len(s)-i)
    if kevin > stuart:
        print('Kevin %d'%kevin)
    elif stuart > kevin:
        print('Stuart %d'%stuart)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)

''' Another method -  Total no of substrings = (len(s)*(len(s)+1)/2'''
string = input()

vw = 'aeiou'.upper()
strl = len(string)
kevin = sum(strl-i for i in range(strl) if string[i] in vw)
stuart = strl*(strl + 1)/2 - kevin

if kevin == stuart:
	print ('Draw')
elif kevin > stuart:
	print ('Kevin %d' % kevin)
else:
	print ('Stuart %d' % stuart)