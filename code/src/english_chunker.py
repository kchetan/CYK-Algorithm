import sys
filename = sys.argv[1]
g = open(filename,'r')
#g=open('../src/English_Test_Chunking.txt','r')
#e=open('./Test/Hindi/Chunking/Hindi_Chunking_Test.txt','r')
test=[]
for line in g:
    #print line
    a=line.split(' ')
    c=[]
    for i in a:
        b=i.split('_')
        c.append(b)
    test.append(c)
#print test
inter=[]
##for line in f:
##    line=line.strip()
##    a=line.split('->')
##    inter.append(a)
##    #print a
chunks=[]
z='S'
c=[]
#print inter[0][1].split(' ')
##for i in range(0,(len(inter)-1)):
##    if inter[i][0]!=z:
##        chunks.append(inter[i][1].split(' '))
##for i in chunks:
##    if 'VP' in i:
##        i.remove('VP')
chunks=[['CD'],['IN', 'CD', 'RB'],['EX'],['WRB'],['WP'],['PRP'], ['PP'], ['IN', 'NP'], ['TO', 'NP'], ['DT', 'NN', 'NN'], ['NNP'], ['VBZ'], ['DT', 'NN'], ['DT', 'NNS'], ['VBP', 'NP', 'PP'], ['IN', 'CD', 'RB'], ['TO', 'VB'], ['S'], ['VBP'], ['VB'], ['VBD'], ['VBN'], ['MD'], ['VB', 'CC', 'VB'], ['PRP$', 'NN', 'NN'], ['PRP$', 'NN'], ['PRP$', 'NN', 'POS', 'NN'], ['NP'], ['RB', 'VP'], ['RB', 'RB', 'VP'], ['VBG'], ['NN'], ['NNS'], ['ADJP'], ['JJ', 'S'], ['NP', 'PP'], ['JJ', 'NN', 'NN'], ['EX'], ['RB', 'NP'], ['VB', 'CD'], ['JJ']]
##print chunks
cn=0
for i in test:
    #print i
    cn=cn+1
    chunked=[]
    chunkedf=[]
    j=0
    while(j>=0):
        flag=0
        flagc=0
        for k in chunks:
            if k[0]==i[j][1]:
                #print 'aaaa'
                #print k[0]
                #print i[j][1]
                flag=1
                #print len(k)
                if len(k)>1 and k[1]==i[j+1][1]:
                    flag=2
                    if len(k)>2 and k[2]==i[j+2][1]:
                        flag=3
                        if len(k)>3 and k[3]==i[j+3][1]:
                            flag=4
            if flag==1 and flag>flagc:
                chunked=[]
##                chunked.append('[')
                chunked.append(i[j][0])
##                chunked.append(']')
                #print chunkedf
                flagc=1
            if flag==2 and flag>flagc:
                chunked=[]
##                chunked.append('[')
                chunked.append(i[j][0])
                chunked.append(i[j+1][0])
##                chunked.append(']')
                flagc=2
            if flag==3 and flag>flagc:
                chunked=[]
##                chunked.append('[')
                chunked.append(i[j][0])
                chunked.append(i[j+1][0])
                chunked.append(i[j+2][0])
##                chunked.append(']')
                flagc=3
            if flag==4 and flag>flagc:
                chunked=[]
##                chunked.append('[')
                chunked.append(i[j][0])
                chunked.append(i[j+1][0])
                chunked.append(i[j+2][0])
                chunked.append(i[j+3][0])
##                chunked.append(']')
                flagc=4
        #print chunked
        if chunked not in chunkedf:
            if chunked[0]!=chunkedf[:-1][:-1]:
                chunkedf.append(chunked)
        
        if flagc==1:
            j=j+1
        if flagc==2:
            j=j+2
        if flagc==3:
            j=j+3
        if flagc==4:
            j=j+4
##        if flag==0:
##            print j
##            print "Cannot chunk\n"
##            j=-1
        if j==(len(i)-1):
            break
    chunkedf.append(i[-1][0])
    print '[',
    for ii in chunkedf:
        print '[',
        for jj in ii:
            print jj,
        print ']',
    print ']'
    if cn>=(len(test)-1):
            break
        



























##for i in test:
##    chunked=[]
##    j=0
##    while(j>=0):
##        flag=0
##        for k in chunks:
##            if k[0]==i[j][1]:
##                if flag==0:
##                    chunked.append('[')
##                    chunked.append(i[j][0])
##                    j=j+1
##                    flag=1
##                if len(k)>1 and k[1]==i[j][1]:
##                    
##                    chunked.append(i[j][0])
##                    j=j+1
##                    if len(k)>2 and k[2]==i[j][1]:
##                        chunked.append(i[j][0])
##                        j=j+1
##                        if len(k)>3 and k[3]==i[j][1]:
##                            chunked.append(i[j][0])
##                            j=j+1
##                chunked.append(']')
##                
                    
                
    
    
