#!/usr/bin/env python
# coding: utf-8

# In[1]:


# from csp import *


# In[2]:


def check_teams(graph, csp_sol):
    result = True
    if len(graph) != len(csp_sol):
        return False
    for i in range(len(graph)):
        tmp_list = graph[i]
        for j in range(len(tmp_list)):
            if csp_sol[i] == csp_sol[tmp_list[j]]:
                result = False
                return result
    return result

