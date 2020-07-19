# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 02:15:56 2020

@author: Akshay
"""
import wikipedia
import datetime
import sys


""" A node represents a webpage.
    Every node contains the page title and its parent i.e. the webpage from 
    which this page was discovered from """
class Node:
    def __init__(self, title, parent):
        self.title = title
        self.parent = parent


""" find all webpages linked to a webpage and return it in a list """       
def find_children(node):
    children = []
    try:
        page = wikipedia.page(node.title, auto_suggest=False)  #creates wikipedia page object of the given title
        links = page.links                                     #return all links(titles) on the page
        for link in links:
            child = Node(link, node) #create a node for a given page
            children.append(child) #add nodes to the list of nodes
    except:
        pass

    return children 


""" given a page, prints the path that page """
def printPathToTarget(node):
    print(" ")
    stack = []
    stack.append(node.title)
    node = node.parent
    while(node):
        stack.append(node.title+" -> ")
        node = node.parent
    while(stack):
        print(stack.pop(), end="")
    


        
""" finds the path to a source page to a target page.
    Technique used is Breadth First Search """
def find_path(src, target):
    if src == target: return "The source page is the target itself"
    startTime = datetime.datetime.now()
    
    #create a node for the source page
    try:
        src_node = Node(src, None)
    except:
        print("please provide valid source and target pages")
    #fringe to store the pages to be visited in First in First Out manner
    queue = []
    
    #stores the pages that have already been visited
    visited = []
    
    queue.append(src_node)
    print("finding path.", end = "", flush=True)
    
    #iterate over the queue to check if a page is the target
    while(queue):
        print(".", end="", flush=True)
        curr = queue.pop(0)
        
        #check if a page is already visited, if yes : check next page
        if curr.title not in visited:
            
            #goal test, if it true then print the pah to the target and terminate the function
            if curr.title == target:
                print("")
                printPathToTarget(curr)
                time = datetime.datetime.now() - startTime
                print(" ")
                print("")
                print("Time Elapsed : "+str(time.seconds/60)+" minutes")
                return
            
            #if goal test fails, find all the links on that page and add it to the queue
            children = find_children(curr)
            for child in children:
                queue.append(child)
                
            #mark a page visited it fails goal test and is done adding its links to the queue
            visited.append(curr.title)
         
try:
    find_path(sys.argv[1],sys.argv[2])
    
except:
    print("please provide valid source and target pages")