#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : 21score.py
@Time    : 2021/12/31 20:38:56
@Author  : dzb
@Contact : dzbwhut@163.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : 计算21点: 2-10：  点数=牌面值
                     A：     点数=1 或者10,用户决定
                     J,Q,K:  点数=0.5   
                           
           算法:     1) 计算"牌面最低值的总分"：定值牌的总分+所有'A'牌的最低分
                     2）如果 牌面最低值的总分==21，返回21点
                     3）否则，查找'含A牌组合分'中的最优值：
                            a）按A的张数，由1点逐步变为10点：加9；
                            b) 如果当前得分为21点，返回21点；
                            c) 否则，更新当前最大值；
                            d) 若还有A牌查询，返回a) 
                            e) 否则，当前最大值。
          单元测试: 1)  先自动测试： 自动生成10组数据并验证
                    2)  再人工测试:  控制台输入牌值，自动验证
                    3） 结束测试：   控制台输入'X', 
                      
'''
import random

def cards_21Score_calcu(cards):
    t=len(cards)
    if t==0:  
        return 0
        
    v=0
    L=0
    vn=[str(e) for e in range(2,11)]
    vh=['J','Q','K']
    
    #计算定值，'A'计数
    for c in cards:  
        if c in vn:
            v= v + int(c)
        elif c in vh:
            v=v+0.5 
        elif c=='A':
            L=L+1
            
    v=(v+L)%21 #定值与L张‘A’卡的最低得分
     
    if v == 0:
        return 21
    
    # 查询'A'的最佳组合值
    mx=v
    for i in range(L):
        v=(v+9)%21
        if v==0:
            return 21
        
        if v>mx:
            mx=v 
        
    return mx


if __name__=='__main__':
    vs=[str(e) for e in range(2,11)]
    vs.extend(['J','Q','K','A'])  
    lc=len(vs)   
    
    print('\n\n-------------test1: 10 random-cards-------------')
    
    for i in range(10):
        cards=[]
        for j in range(i*2):
            d=random.randint(0,lc-1)
            cards.append(vs[d])  
        cards.extend(['A']*random.randint(1,lc-i))#增加‘A’的数量
        
        print('\n ', i+1,')  ',cards,' --> ',cards_21Score_calcu(cards))
        
    
    print('\n\n-------------test2: input cards: A 2-10 J Q K -------------')   
    while 1:
        s=input('-> ')
        cards=s.split()
        if 'X' in cards:
            break
        else:
            print(cards,' --> ',cards_21Score_calcu(cards))
        
            
    
        
        

