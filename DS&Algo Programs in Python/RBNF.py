from scipy import spatial
import pandas as pd
from scipy.special import expit
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import random

# input from file
df = pd.read_csv('data.csv', delim_whitespace=False, sep=',', header=None)
df = df.values.tolist()

# divide in test and train
train, test = train_test_split(df, test_size=0.2)

train = np.asarray(train)
test = np.array(test)

Y = train[:,72]
train = train[:,:-1]

Y_test = test[:,72]
test = test[:,:-1]

# Normalise the data set
scaler = MinMaxScaler().fit(train)
train = scaler.transform(train)
scaler = MinMaxScaler().fit(test)
test = scaler.transform(test)

Y = Y.tolist()
train = train.tolist()
Y_test = Y_test.tolist()
test = test.tolist()
ls = train

# Method to calculate mean of list of lists
def cal_mean(cls1):
    a = np.array(cls1)
    return np.mean(a, axis=0)

# Method to Iterate, updating the cluster centres
def update():
    new_cluster_centers = []
    rows,cols = (k,1)
    new_clusters = [[0 for i in range(cols)] for j in range(rows)]      # Initialise the list of clusters
    for i in range(len(ls)):                                            # Assign each point to the nearest centers
        min_distance = 999
        cluster_id = 0
        for j in range(len(cluster_centers)):
            dist =spatial.distance.euclidean(ls[i],cluster_centers[j])
            if(dist  < min_distance):
                min_distance = dist
                cluster_id = j
        new_clusters[cluster_id].append(ls[i])
    temp = []
    for i in range(len(new_clusters)):
        temp.append(new_clusters[i][1:])
    new_clusters = temp
    for i in range(len(new_clusters)):
        new_cluster_centers.append(cal_mean(new_clusters[i]))
    return new_cluster_centers,new_clusters                     # Return the list of cluster centres along with the respective centres

# ####################################### K-MEANS PART


k = int(15)                                      # Number of Clusters
cluster_centers = random.choices(ls, k=k)        # Randomly select 2 Clusters points as centers
clusters = []

for i in range(100):                             # Doing 100 iterations
    print("iteration",i)
    cluster_centers, clusters = update()

for i in range(k):                               # Printing the centres and the respective clusters
    print("The cluster centers is:")
    print(cluster_centers[i])
    print("And the cluster points are:")
    print(clusters[i])

# cnt = int(0)                                  # Writing the centres, and later using it for saving the time in RBNF
# w = csv.writer(open("cluster_centers.csv", "w",newline=''))
# for i in cluster_centers:
#     w.writerow(i)

# ############################################ RBNF PART

no_of_neurons = [15,1];
no_of_features = 72
no_of_iterations = 500
eta = -0.00001


# Declare the weights and bias
w01 = []
b01 = []
w02 = []
b02 = []
sigma = []
beta = []

# Method to initialise the weights and bias
def init(weights,bias,index):
    features = 0
    for i in range(no_of_neurons[index]):
        ls = []
        if index==0:
            features = 72
        else:
            features = no_of_neurons[index-1]
        limit = np.sqrt(features)
        limit = 1/limit
        for j in range(features):
            ls.append(round(random.uniform(-1*limit,limit), 3))
        weights.append(ls)

    for i in range(no_of_neurons[index]):
        bias.append(round(random.uniform(-1*limit,limit), 3))

# Method to calculate the value of the Gaussian Kernel Function
def phi(temp_ls):
    ans = []
    for i in range(k):
        val = spatial.distance.euclidean(temp_ls, cluster_centers[i])
        val *=  beta[i]
        val *= -1
        ans.append(np.exp(val))
    return ans

# Method to calculate the parameter beta
def init_beta():
    for i in range(len(clusters)):
        ans = 0
        centre = cluster_centers[i]
        sum = 0
        for j in range(len(clusters[i])):
            sum += spatial.distance.euclidean(clusters[i][j],cluster_centers[i])
        sum /= len(clusters[i])
        sigma.append(sum)
        beta.append(1/(2*(sum**2)))

# Call the beta method
init_beta()
init(w02,b02,1)
w02 = w02[0]

# list to plot the Graphs
X_axis = []
Y_axis = []

for itr in range(no_of_iterations):
    print("iteration",itr)
    X_axis.append(itr)
    MSE = 0
    for i in range(len(train)):
        X = train[i]
        H = np.array(phi(X))
        V = np.dot(w02, H)
        V = V + b02
        Y_pred = expit(V)

        # BACKWARD #
        e = Y[i] - Y_pred
        MSE += e*e
        E = e * (Y_pred * (1 - Y_pred))

        J_b02 = E
        J_w02 = E * H
        b02 -= eta * (J_b02)
        w02 -= eta * (J_w02)

    MSE /= len(train)
    Y_axis.append(MSE)

# Plot the Graphs
plt.plot(X_axis,Y_axis)
plt.show()


# Testing
ans = 0
mean = 0
for i in range(len(test)):
    X = test[i]
    H = np.array(phi(X))
    V = np.dot(w02, H)
    V = V + b02
    Y_pred = expit(V)
    mean += Y_pred
    print(Y_pred,end="")
    print(Y_test[i])
    if Y_test[i]==1:
        if Y_pred >= float(0.5):
            ans += 1
    else:
        if Y_pred < float(0.5):
            ans+= 1
print(mean/len(test))
print(ans,len(test))
print("Accuracy:",ans/len(test))




