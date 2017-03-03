from pypinyin import lazy_pinyin,pinyin
import pypinyin
import requests
#import urllib2
import json
from random import randrange


def isPinyin(s):
    return check(s[0]) and check(s[len(s)-1])

def check(uchar):
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
                return True
    else:
                return False

def requestQian(delimiter):
    #print delimiter
    googleAPI = 'http://www.google.com/transliterate/all?tlqt=1&langpair=en|zh&text='+delimiter+'&&tl_app=1'
    #req = urllib2.Request(googleAPI)
    #response = urllib2.urlopen(req)
    #html = response.read()
    r = requests.get(googleAPI)
    html = r.text
    qianyu = json.loads(html)
    qianyu = qianyu.pop()
    qianyu = qianyu['hws'][0]
    return qianyu

def qian(bytes,qianDegree):
    #bytes = input('please input the stuff you want to Qian:')
    uni = bytes
    #uni = bytes.decode('utf-8')
    ans = lazy_pinyin(uni)
    #qianDegree = 52
#print ans[1]
    for i in range(0,len(ans)-1):
    #if randrange(10)>qianDegree:
    #    continue
        if not isPinyin(ans[i]):
            continue
        temp = list(ans[i])
    #print i
    #print ans[i]
        if randrange(100)<=qianDegree:
            posa = randrange(len(temp)-1)
            posb = posa+1
        
            tempSwap = temp[posa]
            temp[posa] = temp[posb]
            temp[posb] = tempSwap
        if randrange(100)<=qianDegree:
        #print "hahahaha"
            posa = randrange(len(temp))
            temp.insert(posa,temp[posa])
        ans[i] = "".join(temp)  
    #print ans[i]

    print (ans)
#delimiter = ''
#delimiter = delimiter.join(ans)
#ans = list(delimiter)
#delimiter = "".join(ans)
#print delimiter



    l=0
    r=-1
    ans.insert(len(ans),u' ')
#print ans
#print len(ans)
    import sys
    finalresult = ''
    for i in range(0,len(ans)):
    #print ans[i]
    #print i
    #print l
    #print r 
        if l>r and not isPinyin(ans[i]):
            l=i+1
            r=l-1
            continue
        if not isPinyin(ans[i]):
        #print '------------'
            original = "".join(ans[l:r+1])
        #print ans[0]
            finalresult = finalresult + (requestQian(original))#,end='')
            finalresult = finalresult + (ans[i])
            l = i+1
            r = l-1
        else:
            r = i
    print (finalresult)
    return finalresult

#qian('生命是多么的辉煌，是多么sdfa的 234!!!精彩',35)
