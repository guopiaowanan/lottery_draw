#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Gp @ 2019-07-18 17:05:17

import random 

P1901 = ["郭飘","李行","柯康", "赵骏然", "严瑞哲", "方小静", "华豪", "彭文杰", "万华", "魏垚", "张一波", "刘洋华",  "马勋",  "吴文涛",  "杨义龙",  "范丽文",  "林欢",  "杨尚儒", "邓彭川",  "周志勇",  "柯鸿成",  "吕浩亮",  "张晶晶",  "叶冲",  "汪梦龙",  "李论",  "徐佳伟", '程明', '黄辉']

answer = str(input("是否查看班级成员信息(y/n):"))

if answer == str("y"):
	print("班级：P1901\n总人数:",len(P1901))
	print("成员:",P1901)
else:
	pass

"""
增加、删除学生
"""

while True:	
	answer1 = str(input("是否添加(add)或删除(del)学生(add/del)【回车跳过】:"))
	if answer1 == str("add"):
		P1901.append(input("请输入即将添加的学生姓名："))
		print(P1901)                                    
		P1901 = P1901
		continue
	elif answer1 == str("del"):
		P1901.remove(input("请输入即将删除的学生姓名："))
		print(P1901)                                    
		P1901 = P1901
		continue
	else:
		break 
"""
随机抽取的人数
"""
while True:
	i = int(input("输入抽取的人数："))
	if i < 1:	
		print("人数不能为该值")
	elif  i > int(len(P1901)):
		print("请输入合适的数字，总人数为：",len(P1901))
	else:
		stus = []
		for j in range(1,i + 1):
			stu = random.choice(P1901)  #随机抽取一个学生
			if stu in stus:             #抽取学生重复时，增加一次抽取次数
				pass
			else:
				stus.append(stu)
				j - 1 
		print("请以下同学提交作业:", stus)		
		
		#print("请以下同学提交作业:", random.sample(P1901,i))  #等效于45到53行
		
		print("全班总人数：",len(P1901))
		break







