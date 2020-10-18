import matplotlib
print(matplotlib._version_)


#pyplot-for visualization and submodu of matlab
import matplotlib.pyplot as plt


x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.scatter(x,y)

plt.title("jst practise")
plt.plot(x,y)


branchnames=['cse','EC','IT','EE']
studentcount=[14,34,67,80]
plt.pie(studentcount,labels=branchnames)

#matplotlib.org 