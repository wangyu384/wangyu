# coding=utf-8
__author__ = 'wang'
import re

year3=r'D:\git\wangyu\FundTest\year3.txt'
year2=r'D:\git\wangyu\FundTest\year2.txt'
year1=r'D:\git\wangyu\FundTest\year1.txt'
month6=r'D:\git\wangyu\FundTest\month6.txt'
month3=r'D:\git\wangyu\FundTest\month3.txt'
month1=r'D:\git\wangyu\FundTest\month1.txt'

RE1=r'\d{6}'

def getFundInfo(pth):
    fundDic={}
    index=1
    with open(pth,'rb') as f:
        for i in f:
            temp=re.search(RE1,i)
            if temp:
                fund=temp.group()
                fundDic[index]=fund
                index=index+1
    return fundDic


year3Info=getFundInfo(year3)
year2Info=getFundInfo(year2)
year1Info=getFundInfo(year1)
month6info=getFundInfo(month6)
month3info=getFundInfo(month3)
month1info=getFundInfo(month1)

totalFund={}
'''
for y3 in year3Info.keys():
    for y2 in year2Info.keys():
        for y1 in year1Info.keys():
            for m6 in month6info.keys():
                for m3 in month3info.keys():
                    for m1 in month1info.keys():
                        if year3Info[y3]==year2Info[y2]==year1Info[y1]==month6info[m6]==month3info[m3]==month1info[m1]:
                            totalFund[y3]=year3Info[y3]
'''
for y3 in year3Info.keys():
    for y2 in year2Info.keys():
        for y1 in year1Info.keys():
            for m6 in month6info.keys():
                if year3Info[y3]==year2Info[y2]==year1Info[y1]==month6info[m6]:
                    totalFund[y3]=year3Info[y3]

for i in totalFund.keys():
    print i,totalFund[i]




