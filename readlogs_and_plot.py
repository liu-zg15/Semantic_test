# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:46:39 2021

@author: Gone
"""
import os 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot




def plot_acc_loss(loss, acc):
    host = host_subplot(111)  # row=1 col=1 first pic
    plt.subplots_adjust(right=0.8)  # ajust the right boundary of the plot window
    par1 = host.twinx()   # 共享x轴
 
    # set labels
    host.set_xlabel("steps")
    host.set_ylabel("test-loss")
    par1.set_ylabel("test-accuracy")
 
    # plot curves
    p1, = host.plot(range(len(loss)), loss, label="loss")
    p2, = par1.plot(range(len(acc)), acc, label="accuracy")
 
    # set location of the legend,
    # 1->rightup corner, 2->leftup corner, 3->leftdown corner
    # 4->rightdown corner, 5->rightmid ...
    host.legend(loc=5)
 
    # set label color
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
 
    # set the range of x axis of host and y axis of par1
    # host.set_xlim([-200, 5200])
    # par1.set_ylim([-0.1, 1.1])
 
    plt.draw()
    plt.show()

path='./ounet_200/logs.txt'

with open(path) as f:
    data=f.readlines()
    f.close()
    

def get_loss_acc_epo(data):
    all_ac=[]
    all_epo=[]
    all_loss=[]
    for i in range(len(data)):
        epoch=data[i].split(' ')[0]
        if epoch=='Epoch':
            strs=data[i-1].split(' ')
            if '0s' in strs:
                eps=data[i].split(' ')[1]
                for j in range(len(strs)):
                    if strs[j]=='loss:':
                        loss=strs[j+1]
                    elif strs[j]=='accuracy:':
                        acc=strs[j+1]
                all_ac.append(acc)
                all_epo.append(eps)
                all_loss.append(loss)
    all_ac=[float(i) for i in all_ac]
    all_loss=[float(i) for i in all_loss]
    all_epo=[int(i.split(':')[0]) for i in all_epo]
    
    
    return all_ac,all_loss,all_epo

all_ac,all_loss,all_epo=get_loss_acc_epo(data)
    
plot_acc_loss(all_loss,all_ac)
        
    