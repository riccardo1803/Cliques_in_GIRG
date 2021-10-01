import time
import matplotlib.pyplot as plt
import random
import numpy as np
import girg_sampling as gs
from typing import List, Tuple
import networkx as nx


def triangles(
    iterations : int = 1, n : int = 10000, d : int = 1, tau : float = 2.5, gamma : float = 2, scale : float = 1., info : bool = True, save: bool = True):
    
    path = "gamma-"+str(gamma)+"/scale-"+str(scale)+"/ple-"+str(tau)+"/n-"+str(n)+".txt"
    file = open(path,"a")
        
    for _ in range(iterations):
        
        t1 = time.time()

        ws = np.random.randint(10000)
        ps = ws + 1
        ss = ws + 2

        weights = gs.generateWeights(n, tau, weightSeed=ws)
        scaled_weights = [scale*w for w in weights]        
        positions = gs.generatePositions(n, d, positionSeed=ps)
        edgelist = gs.generateEdges(scaled_weights, positions, gamma, samplingSeed=ss)

        t2 = time.time()
        if info:
            print(f"Nodes: {n}\nTau: {tau}\nDimension: {d}\nGamma: {gamma}\nSeeds: {(ws,ps,ss)}\n")
            print(f"Sampling of graph: {t2-t1}")

        G = nx.Graph()
        G.add_nodes_from(list(range(n)))
        G.add_edges_from(edgelist)

        t3 = time.time()
        if info:
            print(f"Graph creation: {t3-t2}")
        
        triangles = nx.triangles(G)
        T = sum(triangles.values()) / 3
        
        t4 = time.time()
        if info:
            print("Counting triangles:", t4 - t3)
            print("+"+"-"*30+"+")
        
        if save:
            file.write(f"{(ws,ps,ss)} {T}\n")
            
    file.close()
    
    return T


def multi_triangles(
    iterations, nset, tauset, scale=1., d : int = 1, gamma : float = 2, info : bool = False, elapsed : bool = True, save: bool = True):
    
    t1 = time.time()
    
    for tau in tauset:
        tt1 = time.time()
        for n in nset:
            ttt1 = time.time()
            triangles(iterations=iterations, n=n, tau=tau, d=d, gamma=gamma, scale=scale, info=info, save=save)    
            ttt2 = time.time()
            
            if elapsed:
                print(f"Elapsed time for Tau={tau}, n={n}: {ttt2-ttt1}")
        
        tt2 = time.time()
        if elapsed:
            print(f"Total elapsed time for Tau={tau}: {tt2-tt1}")
        
    t2 = time.time()
    
    if elapsed:
        print(f"\nTotal elapsed time: {t2-t1}")
        
    return


def run_triangle_all_tau():
    
    n_start = int(input("Start at n: "))
    n_stop = int(input("Stop at n: "))
    n_step = int(input("Step of n: "))
    
    nset = list(range(n_start,n_stop+1,n_step))

    tauset = (2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9)
    
    iterations = int(input("Number of iterations: "))
    
    multi_triangles(iterations, nset, tauset)
    
    return