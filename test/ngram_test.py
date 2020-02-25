def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r


a = '오늘 강남에서 맛있는 스파게티를 먹었다.'
b = '강남에서 먹었던 오늘의 스파게티는 맛있었다.'
c = '강남 에서 먹 었 던 오늘 의 스파게티 는 맛있 었 다 .'
d = '오늘 강남 에서 맛있 는 스파게티 를 먹 었 다 .'
e = '철수는 영희를 좋아해'
f = '철수는 영희를 안 좋아해'


print(ngram(a, 2))
print(ngram(b, 2))

r2, word2 = diff_ngram(a, b, 2)
print('2-gram:', r2, word2)

r3, word3 = diff_ngram(c, d, 2)
print('2-gram:', r3, word3)

r4, word4 = diff_ngram(e, f, 2)
print('2-gram:', r4, word4)



#r3, word3 = diff_ngram(a, b, 3)
#print('3-gram:', r3, word3)