#!/usr/bin/python
# -*- coding utf-8 -*-
''' this script for change all files name using dict'''

import os,sys


dict1 = { "hanlong01-02.xls":"132503940037677.xls", "leien01.xls":"132513300047675.xls", "lianzhong01.xls":"132563910030346.xls", "xianlvgu01.xls":"132609396016447.xls", "xianlvgu031.xls":"133056390057597.xls", "xianlvgu032.xls":"133056390258576.xls", "xianlvgu033.xls":"133056390499498.xls", "lianzhong031.xls":"133109484069752.xls", "lianzhong032.xls":"133109484252471.xls", "lianzhong033.xls":"133109484424266.xls", "leien031.xls":"133230606024846.xls", "leien032.xls":"133230606257303.xls", "leien033.xls":"133230606407226.xls", "hanlong031.xls":"133274544066139.xls", "hanlong032.xls":"133274544247481.xls", "hanlong033.xls":"133274544651490.xls", "133411368098533-1.xls":"133480608063474.xls", "133411368098533-2.xls":"133480608230383.xls", "133411368098533-3.xls":"133480608439031.xls", "133411368098533-4.xls":"133480608896503.xls", "133411368098533-5.xls":"133480609013491.xls", "133411368098533-6.xls":"133480609203475.xls", "133411368098533-7.xls":"133480609495135.xls", "133456221592266-1.xls":"133264596067835.xls", "133456221592266-2.xls":"133264596202326.xls", "133456221592266-3.xls":"133264596494579.xls", "133456221592266-4.xls":"133264596651237.xls", "133456221592266-5.xls":"133264596836762.xls", "133456221592266-6.xls":"133264597016577.xls", "133456221592266-7.xls":"133264597229928.xls", "20120723-1.xls":"133290156029989.xls", "20120723-2.xls":"133290156220350.xls", "20120723-3.xls":"133290156417065.xls", "20120723-4.xls":"133290156698574.xls", "20120723-5.xls":"133290156861836.xls", "20120723-6.xls":"133290157044221.xls", "20120723-7.xls":"133290157299035.xls", "lj20120723-1.xls":"133237836001752.xls", "lj20120723-2.xls":"133237836269404.xls", "lj20120723-3.xls":"133237836450433.xls", "lj20120723-4.xls":"133237836609206.xls", "lj20120723-5.xls":"133237836832243.xls", "lj20120723-6.xls":"133237837059614.xls", "lj20120723-7.xls":"133237837201627.xls", "lj20120723-8.xls":"133237837466717.xls", "lj20120723-9.xls":"133237837654114.xls", "dfhl-kj-201207231.xls":"133921428048369.xls", "dfhl-kj-201207232.xls":"133921428211043.xls", "dfhl-kj-201207233.xls":"133921428444219.xls", "hanlong20410kj.xls":"134284308029879.xls", "hanlong30410kj.xls":"134586708033221.xls", "hanlong40410kj.xls":"134837628020263.xls", "hanlong50410kj.xls":"135105468077749.xls", "hanlong60410kj.xls":"135389622088512.xls", "hanlong70410kj.xls":"135449898026636.xls", "le-kj-20120723-1.xls":"133730796046358.xls", "le-kj-20120723-2.xls":"133730796211274.xls", "le-kj-20120723-3.xls":"133730796479059.xls", "leien20411kj.xls":"134312196059229.xls", "leien30411kj.xls":"134623236065163.xls", "leien40411kj.xls":"134830596001416.xls", "leien50411kj.xls":"135089796003086.xls", "leien60411kj.xls":"135339540035888.xls", "leien70411kj.xls":"135519198087888.xls", "lianzhong10412kj.xls":"133757076069934.xls", "lianzhong10412kj1.xls":"133757076235160.xls", "lianzhong20412kj.xls":"134344596022179.xls", "lianzhong30412kj.xls":"134612436069597.xls", "lianzhong40412kj.xls":"134880276015974.xls", "lianzhong50412kj.xls":"135139476062232.xls", "lianzhong60412kj.xls":"135399360091625.xls", "lianzhong70412kj.xls":"135475764077582.xls", "my-20120723-1.xls":"133748316053748.xls", "my-20120723-2.xls":"133748316286290.xls", "my-20120723-3.xls":"133748316455184.xls", "my-20120723-4.xls":"133748316621176.xls", "my-20120723-5.xls":"133748316832440.xls", "lingju20413kj.xls":"134318556005280.xls", "lingju30413kj.xls":"134586396066532.xls", "lingju40413kj.xls":"134854596040865.xls", "lingju50413kj.xls":"135113796024017.xls", "lingju60413kj.xls":"135339066049891.xls", "lingju70413kj.xls":"135608418049486.xls", "leien10104kj.xls":"135754254036195.xls", "lingju20104kj.xls":"135994506083324.xls", "leien30104kj.xls":"136204656071529.xls", "leien40104kj.xls":"136486830012070.xls", "leien50104kj.xls":"136497396097367.xls", "leien60104kj.xls":"136790076068301.xls", "leien70104kj.xls":"137403156089056.xls", "lingju10105kj.xls":"135779784040698.xls", "leien20105kj.xls":"136013544062646.xls", "lingju30105kj.xls":"136212636025944.xls", "lingju40105kj.xls":"136557804058008.xls", "lingju50105kj.xls":"136797558031607.xls", "lingju60105kj.xls":"137074038086181.xls", "lingju70105kj.xls":"137377158088036.xls", "lingju80105kj.xls":"137645358010773.xls", "hanlong10404kj.xls":"136478022096921.xls", "hanlong20404kj.xls":"136685832036000.xls", "hanlong30404kj.xls":"136963752030677.xls", "aomei40404kj.xls":"137144472061844.xls", "hanlong50404kj.xls":"137662872088546.xls" }


def rename_files1():
    #filenames=os.listdir(os.getcwd())
    print len(dict1)
    path = '/tmp/s'
    filenames = os.listdir(path)
    print  filenames
    print xrange(len(dict1))
    out=open('/tmp/record.txt','w')
    for i in xrange(len(dict1)):
        print "a=%s "  %  filenames[i]; 
        print "b=%s "  %  dict1.has_key(filenames[i])
        if(dict1.has_key(filenames[i])):
            os.rename(os.path.join(path,filenames[i]),os.path.join(path,dict1.get(filenames[i])))
            out.write("%s rename to %s ok"   %  (filenames[i],dict1.get(filenames[i])))
            out.write('\n')
        else: 
            print "No found file,plz checking"
    out.close()



#def rename_files2():
#    filenames=os.listdir(os.getcwd())
#    for file in filenames:
#        print file
#        #if file.split('.',1)[1] == 'py':
#        #    os.rename(file,'ex'+file.split('.',1)[0]+'.py')
#        print file[-2:]
#        if file[-2:] == 'py':
#            os.rename(file,file[:-2]+'.py')


if __name__ == '__main__':
    rename_files1()
#    rename_files2()
