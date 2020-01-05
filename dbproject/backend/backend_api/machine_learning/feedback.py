import NeutralNetwork2
#DATA FROM DB COME HERE IN JSON, the re scored data and response

#Divde data by 100

#Data is then fed into network and network is updated

data_testx = [[0.33333333, 0.3125 ,    0.,        0.,    0],
 [0.66666667, 0.3125,     0.,         0.,         0.        ],
 [0.66666667, 0.6875,     0.,         0.,         0.        ],
 [0.66666667, 0.,         0.23076923, 0.,         0.        ],
 [0.16666667, 0.1875,     0.,         0.,         0.        ],
 ]

data_testy = [0, 0, 0, 0, 0]

NeutralNetwork2.retrain_neutral_network(data_testx, data_testy, 'Java')

 

