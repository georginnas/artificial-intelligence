#Dadeni se karakteristiki na koli i da se vidi koja e prifatliva ili ne e prifatliva
import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
import math
def read_file(file_name):

    with open(file_name) as doc:
        csv_reader=csv.reader(doc, delimiter=',')
        dataset=list(csv_reader)[1:] #da go preskokne prviot red bidejki ni e nepotreben objasnuvanje za kolonite
    return dataset



if __name__=='__main__':
    dataset=read_file('cars.csv')

    encoder=OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset]) #treniranje bez klasata(posledniot element)

    train_set=dataset[:int(0.7*len(dataset))] #prvite 70 posto se za treniranje
    train_x=[row[:-1]for row in train_set] #bez klasata
    train_y=[row[-1] for row in train_set] #samo klasata(poslednata kolona)
    train_x=encoder.transform(train_x) #gi transformira vo brojki kolonite

    test_set=dataset[int(0.7*len(dataset)):] #ostanatite 30 posto se za testiranje
    test_x=[row[:-1] for row in test_set]
    test_y=[row[-1] for row in test_set]
    test_x=encoder.transform(test_x) #gi transformira vo brojki kolonite

    classifier=CategoricalNB()
    classifier.fit(train_x,train_y)

    predicted_class=classifier.predict([test_x[5]])[0]
    true_class=test_y[5]

    accuracy=0

    for i in range(len(test_set)):
        predicted_class=classifier.predict([test_x[i]])[0]
        true_class=test_y[i]

        if predicted_class== true_class:
            accuracy+=1
    accuracy=accuracy/len(test_set)
    print(f'Accuracy: {accuracy}')
    entry=[el for el in input().split(' ')]
    encoded_entry=encoder.transform([entry])
    predicted_class=classifier.predict(encoded_entry)
    print(predicted_class)
