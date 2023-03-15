#Dadena e glukoza i pritisok da se odredi dali e dijabeticar
import csv
from sklearn.naive_bayes import GaussianNB
def read_file(file):
    with open(file) as doc:
        csv_reader=csv.reader(doc, delimiter=',')
        dataset=list(csv_reader)[1:]
    data=[]
    for row in dataset:
        row2=[int(el) for el in row] #da se napravat vo integer biodejki se string
        data.append(row2)
    return data

if __name__=='__main__':
    dataset=read_file('med.csv')

    train_set=dataset[:int(0.7*len(dataset))]
    train_x=[row[:-1] for row in train_set]
    train_y=[row[-1] for row in train_set]


    test_set=dataset[int(0.7*len(dataset)):]
    test_x=[row[:-1] for row in test_set]
    test_y=[row[-1] for row in test_set]

    classifier=GaussianNB()
    classifier.fit(train_x,train_y)

    accuracy=0

    for i in range(len(test_set)):
        predicted_class=classifier.predict([test_x[i]])[0]
        true_class=test_y[i]
        if predicted_class==true_class:
            accuracy+=1
    accuracy=accuracy/len(test_set)
    print(f'Accuracy: {accuracy}')
    entry=[int(el)for el in input().split(' ')]
    predicted_class=classifier.predict([entry])[0]
    print(predicted_class)
    print(classifier.predict_proba([entry]))
