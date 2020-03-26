#!/usr/bin/env python
# coding: utf-8

# In[1]:


from csp import *


# In[2]:


def rand_graph(n, p):
    dic = {}
    for i in range(n):
        tmp_list = []
        for j in range(n - i - 1):
            if random.random() <= p:
                tmp_list.append(i + j + 1)
        dic[i] = tmp_list
    for i in range(n):
        i = n - 1 - i
        for j in range(i):
            tmp_list = dic[j]
            for k in range(len(tmp_list)):
                if tmp_list[k] == i:
                    dic[i].append(j)
                elif tmp_list[k] > i:
                    break
    for i in range(n):
        dic[i].sort()
    return dic


