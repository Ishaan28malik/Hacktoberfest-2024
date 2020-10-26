'''
	Best KNN algorithm implementation world has ever seen
'''
import math

def EuclideanDistance(a, b): # N dimention Euclidean distance implementation
	s = 0
	for i in range(len(a)):
		s += (a[i] - b[i]) ** 2
	return math.sqrt(s)

class KNN:
	def __init__(self, k, training_data):
		self.k = k
		self.samples = training_data
	
	def predict(self, params):
		distances = []
		for sample in self.samples:
			distances.append((sample[1], EuclideanDistance(params, sample[0])))
		distances.sort(key = lambda a: a[1])
		distances = list(map(lambda a: a[0], distances[0:self.k]))
		return max(set(distances), key = distances.count)

Iris_setosa     = 0
Iris_versicolor = 1
Iris_virginica  = 2

def ClassNameToEnum(class_name):
	if class_name == "Iris-setosa":
		return Iris_setosa
	if class_name == "Iris-versicolor":
		return Iris_versicolor
	if class_name == "Iris-virginica":
		return Iris_virginica
	print("------------ Error: Unknown Class Name!! ------------")

def EnumToClassName(enum):
	if enum == Iris_setosa:
		return "Iris-setosa"
	if enum == Iris_versicolor:
		return "Iris-versicolor"
	if enum == Iris_virginica:
		return "Iris-virginica"
	print("------------ Error: Unknown Class Name!! ------------")

def ReadData():
	training_data = []
	training_data_file = open("iris_train.txt")

	is_first_line = True
	for line in training_data_file.readlines():
		if is_first_line:
			is_first_line = False
			continue
		items = line.replace('\n', '').split(',')
		training_data.append([list(map(float, items[0:-1])), ClassNameToEnum(items[-1])])
		
	training_data_file.close()

	test_data = []
	test_data_file = open("iris_test.txt")

	is_first_line = True
	for line in test_data_file.readlines():
		if is_first_line:
			is_first_line = False
			continue
		items = line.replace('\n', '').split(',')
		test_data.append(list(map(float, items)))
		
	test_data_file.close()

	return (training_data, test_data)

def main():
	# read data
	# format: [[float(param), float(param), ...], int(class)]
	(training_data, test_data) = ReadData()

	# choose K
	# People on the net said: "use odd numbers for K (4K XD).
	# and using sqrt(n) where n is number of samples; works most of the time"
	k = math.sqrt(len(training_data))
	kRounded = round(k)
	if kRounded % 2 == 0:
		if kRounded > k:
			k = kRounded - 1
		else:
			k = kRounded + 1
	else:
		k = kRounded

	knn = KNN(k, training_data)

	for test in test_data:
		print(EnumToClassName(knn.predict(test)))

if __name__ == "__main__":
	main()
