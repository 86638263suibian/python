'''import requests

file = open('sqlerr.txt' , 'r')
err_list = file.readlines()
file.close()
resp = requests.get('http://www.ya.ru')
#print resp.text 
#err = 'DOCTYPE'
err = str(err_list[0])
err = err.strip()
print err
if resp.text.find(err)>0:
    print 'YES'
else:
    print 'NO'

'''
import requests
import re
import os
import string
#------------------------sqlerr.txt------------------------------
file = open('sqlerr.txt' , 'r')
err_list = file.readlines()
file.close()
print(' ______________________________________')
print('|                                      |')
print('|  Parser dork from                    |')
print('|      _                               |')
print('|     |_) o ._   _     _  _  ._ _      |')
print('|     |_) | | | (_| o (_ (_) | | |     |')
print('|                _|                    |')
print('|                                      |')
print('|                v.2.1                 |')
print('|                           famgor(c)  |')
print('|______________________________________|')
print
#--------------------------------------------------------------
def check_404(url):
    rsp = requests.get(url)
    if (rsp.status_code == 200):
        return 1
    else:
        return 0
#--------------------------------------------------------------
file = open('url_pars.txt', 'w')
file.close()
#search = raw_input('Text of dork (example:index.php?id=):')
#search = 'post.php?id='
#------------------Dorks list----------------------------------
dorks = open('dorks.txt' , 'r', ,encoding='utf8')
dorks_list = dorks.readlines()
dorks.close()
#--------------------------------------------------------------
pages = int(input('Input number of page: '))*10
#print(pages)
print('Number of dorks: '+str(len(dorks_list)))
#pages = 10
for i in range(len(dorks_list)):
    search = dorks_list[i].strip()
    #print('Use dork: '+search)
    count = 1
    while (count < pages):
#http://www.bing.com/search?q=index.php?id=&go=&filt=all&first=1&FORM=PERE3
        req = ('http://www.bing.com/search?q=' + search + '&first='+str(count))
        try:	
            response = requests.get(req)
        except:
            print('Error get bing.com')
	#print response.text	
        req = ''	
        try:
            link = re.findall('<h2><a href="(.+?)"', response.text, re.DOTALL)
            for i in range(len(link)):
                print(link[i])
		#if link[i].find('yandex'):
		#	print 'YANDEX'
		#else:
                if link[i].find('http://bs.yandex.ru'):
                    #print('url: '+link[i])	
                    open('url_pars.txt', 'a+').write(link[i] +'\'' + '\n')
		#else:
		    #print 'ya'
		#count = count+10
		#print count
        except:
            print('Error parsing url')
        count = count+10
    #print(count)
#---------------------Delete duplicates-------------------------
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]
print('Removing duplicates...')
input = open('url_pars.txt', 'r')
output = open('url.txt', 'w')
linesarray = input.readlines()
input.close()
seen = []
seen = f7(linesarray)
#print(seen)
for i in range(len(seen)):
    output.write(seen[i])
'''linesarray = input.readlines()
input.close()
seen = []
for i in range(len(linesarray)):
    if seen.count(linesarray[i]) == 0:
        seen.append(linesarray[i])
	#if linesarray[i].find('http://bs.yandex.ru'):
	output.write(linesarray[i])'''		
        #else:
		#print 'ya'
	
os.remove('url_pars.txt')
output.close()
print('Complete')
print('Checking error...')
#-------------------------url.txt--------------------------------
file = open('url.txt' , 'r')
url_list = file.readlines()
file.close()
#------------------------Proverka--------------------------------
err_page = 0
good_page = 0
#responce = ''
for i in range(len(url_list)):
    page = url_list[i].strip()
    #print(page)
    try:
        #if (check_404(page))==1:
        response = requests.get(page, timeout = 10)
        #print(response.status_code)
        #else: break
    except:
        err_page = err_page+1
        print('Error while get page.')
    #else:
    for i in range(len(err_list)):
        err = str(err_list[i])
        err = err.strip()			
        if response.text.find(err)>0:
            print('FIND "'+err+'" in '+page)
            open('good.txt', 'a+').write(page + '\n')
            good_page = good_page + 1
        else:
            pass
#-------------------------------------------------------------------
print('Good pages: '+str(good_page))
print('404,403 pages: '+str(err_page))
print('Complete. Press any key...')
