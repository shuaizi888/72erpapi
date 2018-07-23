#coding:utf-8
#Author:sgao
import sys
import yaml
print sys.path

class A(object):

    @property
    def d1(self):
        print 'd1'

    @property
    def d2(self):
        print 'd2'


getattr(A(),'d%d'%2)