from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import json

#   volu weig minT maxT | RPE RPE RPE | tes tco tce dist | tes tco tce dist | tes tco tce dist
X_train = [
    [1   , 10.6, 10, 25,   6,  19,  14,  35, 31,  2, 15.7,  22, 18, -5,  2.1,  12, 11, -5, 13.0],
    [0.05,  0.7, 23, 35,  17,  15,  19,  25, 11, -2,  6.5,  25, 21, -2,  3.5,  24, 20, -4, 10.2],
    [0.70,  7.2, -4,  2,  16,  17,   8,  18, 16, -1,  7.1,  32, 30,  3,  6.0,  25, 21,  4,  6.0],
    [0.60,  3.2,  6, 12,  13,  14,  15,  28, 25, 10, 10.2,  28, 26, 10,  3.4,  23, 20, 15,  5.2],
    [0.02,  0.3,  5, 23,  17,   7,  12,  25, 18,  0, 12.0,  21, 20,  2, 10.7,  19, 18, -2,  7.2],
    [1.23, 15.1,  0, 30,  17,   7,  15,  25, 18,  0,  8.2,  26, 25,  2, 12.0,  25, 22, -1,  8.0],
    [0.90, 11.2,  0, 25,   9,  12,  18,  22, 20,  2,  2.1,  28, 26,  1,  2.8,  28, 24,  0,  7.4],
    [0.20,  3.5, -1,  5,   7,  18,  11,  23, 21,  2,  5.9,  24, 21,  7,  5.1,  23, 22,  5,  6.7],
    [0.50,  2.0, -6,  0,  18,  16,   9,  18, 18,  0, 14.2,  20, 18, -1,  5.7,  20, 18, -3,  5.3],
    [0.02,  0.1, 12, 30,  10,  14,  20,   5,  5, -1,  3.9,  25, 20,  0,  3.2,   9,  8, -1,  1.7],
    [0.50,  9.3, -2,  6,  16,  11,  17,  22, 20,  5, 10.2,  22, 22,  2, 11.4,   5,  3, -6, 14.0]
]
y_train = [
    ['courier_1', 'truck_1'],
    ['courier_2', 'truck_2'],
    ['courier_3', 'truck_1'],
    ['courier_1', 'truck_2'],
    ['courier_3', 'truck_3'],
    ['courier_2', 'truck_3'],
    ['courier_1', 'truck_1'],
    ['courier_2', 'truck_1'],
    ['courier_1', 'truck_3'],
    ['courier_3', 'truck_2'],
    ['courier_2', 'truck_2']
]

def getDataset(product):
    with open('couriers.json', 'r') as f:
        couriers = json.load(f)

    with open('trucks.json', 'r') as f:
        trucks = json.load(f)

    data = []
    data.append(product['volume'])
    data.append(product['weight'])
    data.append(product['minT'])
    data.append(product['maxT'])
    for i in range(0, len(couriers)):
        data.append(couriers[i]['RPE'])
    for i in range(0, len(trucks)):
        data.append(trucks[i]['t_est'])
        data.append(trucks[i]['t_cont'])
        data.append(trucks[i]['t_cell'])
        data.append(trucks[i]['dist'])
    return data


def process(product):
    d = getDataset(product)
    dataset = []
    dataset.append(d)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    suggestion = model.predict(dataset)

    return suggestion