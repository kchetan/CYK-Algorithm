import sys
filename = sys.argv[1]
g=open(filename,'r')
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
print test[0][0][0]
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
#chunks=[['CD'],['IN', 'CD', 'RB'],['EX'],['WRB'],['WP'],['PRP'], ['PP'], ['IN', 'NP'], ['TO', 'NP'], ['DT', 'NN', 'NN'], ['NNP'], ['VBZ'], ['DT', 'NN'], ['DT', 'NNS'], ['VBP', 'NP', 'PP'], ['IN', 'CD', 'RB'], ['TO', 'VB'], ['S'], ['VBP'], ['VB'], ['VBD'], ['VBN'], ['MD'], ['VB', 'CC', 'VB'], ['PRP$', 'NN', 'NN'], ['PRP$', 'NN'], ['PRP$', 'NN', 'POS', 'NN'], ['NP'], ['RB', 'VP'], ['RB', 'RB', 'VP'], ['VBG'], ['NN'], ['NNS'], ['ADJP'], ['JJ', 'S'], ['NP', 'PP'], ['JJ', 'NN', 'NN'], ['EX'], ['RB', 'NP'], ['VB', 'CD'], ['JJ']]
#chunks=['NN', 'NNP', 'NN NN', 'NN PSP', 'NNP PSP', 'NN PSP NN', 'PRP NN', 'PRP RP NN RP', 'NNC NN', 'JJ NNC NN', 'NN NN PSP', 'PRP NN PSP', 'JJ NN PSP', 'NNPC NNP NNPC NNP PSP', 'NNP NNPC NNP', 'NN PSP NNP', 'NN PSP PSP', 'NN NNP PSP PSP', 'JJ NNC NN PSP', 'NNPC NNP PSP', 'JJ QC NN PSP', 'PRP DEM QO NNC NN', 'NST NNC NN', 'NNP PSP NN', 'PRP NNPC NNP PSP', 'NNC NN PSP', 'JJ NN PSP PSP', 'PRP JJ NN', 'PRP NNPC NNP PSP PSP', 'VM', 'VM VAUX', 'VM VAUX VAUX', 'NEG VM', 'VM NEG', 'NEG VM AUX', 'RB RB VM VAUX', 'JJ', 'INTF', 'UNK', 'CC', 'RB']
chunks=[['VAUX'],['WQ'],['QO'],['NNP'],['QC'],['NST'],['NN'],['CC'],['PSP'],['PRP'],['NN','PSP','NN'],['PSP'],['NN','NN','PSP'],['VM'],['NN'], ['NNP'], ['NN', 'NN'], ['NN', 'PSP'], ['NNP', 'PSP'], ['NN', 'PSP', 'NN'], ['PRP', 'NN'], ['PRP', 'RP', 'NN', 'RP'], ['NNC', 'NN'], ['JJ', 'NNC', 'NN'], ['NN', 'NN', 'PSP'], ['PRP', 'NN', 'PSP'], ['JJ', 'NN', 'PSP'], ['NNPC', 'NNP', 'NNPC', 'NNP', 'PSP'], ['NNP', 'NNPC', 'NNP'], ['NN', 'PSP', 'NNP'], ['NN', 'PSP', 'PSP'], ['NN', 'NNP', 'PSP', 'PSP'], ['JJ', 'NNC', 'NN', 'PSP'], ['NNPC', 'NNP', 'PSP'], ['JJ', 'QC', 'NN', 'PSP'], ['PRP', 'DEM', 'QO', 'NNC', 'NN'], ['NST', 'NNC', 'NN'], ['NNP', 'PSP', 'NN'], ['PRP', 'NNPC', 'NNP', 'PSP'], ['NNC', 'NN', 'PSP'], ['JJ', 'NN', 'PSP', 'PSP'], ['PRP', 'JJ', 'NN'], ['PRP', 'NNPC', 'NNP', 'PSP', 'PSP'], ['VM'], ['VM', 'VAUX'], ['VM', 'VAUX', 'VAUX'], ['NEG', 'VM'], ['VM', 'NEG'], ['NEG', 'VM', 'AUX'], ['RB', 'RB', 'VM', 'VAUX'], ['JJ'], ['INTF'], ['UNK'], ['CC'], ['RB']]
#chunks=[['NP', 'NN'], ['NP', 'NNP'], ['NP', 'NN NN'], ['NP', 'NN PSP'], ['NP', 'NNP PSP'], ['NP', 'NN PSP NN'], ['NP', 'PRP NN'], ['NP', 'PRP RP NN RP'], ['NP', 'NNC NN'], ['NP', 'JJ NNC NN'], ['NP', 'NN NN PSP'], ['NP', 'PRP NN PSP'], ['NP', 'JJ NN PSP'], ['NP', 'NNPC NNP NNPC NNP PSP'], ['NP', 'NNP NNPC NNP'], ['NP', 'NN PSP NNP'], ['NP', 'NN PSP PSP'], ['NP', 'NN NNP PSP PSP'], ['NP', 'JJ NNC NN PSP'], ['NP', 'NNPC NNP PSP'], ['NP', 'JJ QC NN PSP'], ['NP', 'PRP DEM QO NNC NN'], ['NP', 'NST NNC NN'], ['NP', 'NNP PSP NN'], ['NP', 'PRP NNPC NNP PSP'], ['NP', 'NNC NN PSP'], ['NP', 'JJ NN PSP PSP'], ['NP', 'PRP JJ NN'], ['NP', 'PRP NNPC NNP PSP PSP'], ['VBP', 'VM'], ['VGF', 'VM VAUX'], ['VGF', 'VM VAUX VAUX'], ['VGF', 'NEG VM'], ['VGF', 'VM NEG'], ['VGF', 'NEG VM AUX'], ['VGF', 'RB RB VM VAUX'], ['JJP', 'JJ'], ['INTF', 'INTF'], ['UNK', 'UNK'], ['CCP', 'CC'], ['RBP', 'RB']]
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
##            print k[0]
##            print i[j][1]
##            print
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
                    
                
    
    
