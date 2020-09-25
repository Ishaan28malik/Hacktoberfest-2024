import numpy as np
import random, itertools, collections


from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull

from interLine import interLine
from perpBisector2d import perpBisector2d
from inHull import inHull


def voronoi(pins,bnd):

	pnts = inHull(pins,bnd)

	#print np.shape(pout)[0]

	# linear equations for the boundary
	bndhull = ConvexHull(bnd)
	bndTmp = bndhull.equations
	bndMat = np.matrix(bndTmp)
	Abnd = bndMat[:,0:2]
	bbnd = bndMat[:,2]


	# Delaunay triangulation
	tri = Delaunay(pnts)

	# find voronoi neighbors for each generater point
	neib = [ [] for row in pnts]
	for j, obj in enumerate(pnts):
		neib[j]=[]
		i = 0
		for row in tri.simplices:
		    i = i + 1
		    tmp = np.intersect1d(tri.simplices[i-1],[j])
		    if tmp.size !=0:
		        neib[j].append(np.setdiff1d(tri.simplices[i-1],j))
		neib[j] = np.unique(neib[j])

	# find linear equations for perpendicular bisectors

	mylistA = []
	mylistb = []

	for i, obj in enumerate(pnts):
		A = np.array([[0, 0]])
		b = np.array([0])
		for j in range(0,len(neib[i])):
		    Altmp, blt = perpBisector2d(pnts[i],pnts[neib[i][j]])
		    Al = np.array([Altmp])
		    bl = np.array([blt])
		    A = np.concatenate((A,Al),axis=0)
		    b = np.concatenate((b,bl),axis=0)
		Amat = np.matrix(A)
		bmat = np.matrix(b)
		mylistA.append(Amat[1:np.shape(Amat)[0]])
		mylistb.append(bmat[:,1:np.shape(bmat)[1]])

	# obtain voronoi vertices

	vorn = [ [] for row in pnts]
	for j in range(0,len(mylistA)):
		Atmp = np.concatenate((mylistA[j],Abnd))
		btmp = np.concatenate((mylistb[j].transpose(),-bbnd))
		k =0
		for comb in list(itertools.combinations(range(1,np.shape(Atmp)[0]+1),2)):
			k = k+1
			if k <= len(list(itertools.combinations(range(1,np.shape(Atmp)[0]+1),2))):
				lineA = [Atmp[comb[0]-1].item(0,0),Atmp[comb[0]-1].item(0,1),btmp[comb[0]-1].item(0,0)]
				lineB = [Atmp[comb[1]-1].item(0,0),Atmp[comb[1]-1].item(0,1),btmp[comb[1]-1].item(0,0)]
				output = interLine(lineA,lineB)
				if type(output) != type(False):
					if (np.round(np.dot(Atmp,np.array([output.item(0,0),output.item(1,0)])),7)<=np.round(btmp.transpose(),7)).all():
						vorn[j].append([output.item(0,0),output.item(1,0)])



	return pnts,vorn
