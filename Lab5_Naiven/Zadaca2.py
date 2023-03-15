#NAIVEN BAESOV SO KARAKTERISTIKI STO SE NEPREKJINATI VREDNOSTI
#GAUSOV NAIVEN KLASIFIKATOR KE KORISTIME
import csv
from sklearn.naive_bayes import GaussianNB

def read_file(doc):
    with open(doc) as f:
        csv_reader=csv.reader(f,delimiter=',')
        dataset=list(csv_reader)[1:]
        #dataset=[int(el) for row in dataset for el in row]
    dataset_v2=[]
    for row in dataset:
        row_v2=[int(el) for el in row]
        dataset_v2.append(row_v2)
    return dataset_v2

if __name__=="__main__":
    #TUKA NE TREBA ENCODER ZATOA STO GAUSSAN ZNAE DA SE SPRAVI SO NEPREKJINATI VREDNOSTI

    dataset=read_file('med.csv') #IMAME STRINGOVI MORA DA SE PRETVORI BIDEJKI KORISTIME NAIVEN GAUSOV VO INT

    train_set=dataset[:int(len(dataset)*0.7)] #mnoz za treniranje
    train_x=[row[:-1] for row in train_set] #karakteristiki
    train_y=[row[-1] for row in train_set] #klasata

    test_set=dataset[int(len(dataset)*0.7):] #mnoz za testiranje
    test_x=[row[:-1] for row in test_set] #karakteristiki
    test_y=[row[-1] for row in test_set] #klasata

    classifier=GaussianNB()
    classifier.fit(train_x,train_y)

    acc = 0  # tocnost, t.e kolku primeroci imame pogodeno
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            acc += 1
    new = acc / len(test_set)

    print(f'Accuracy: {new}')

    entry = [int(el) for el in input().split(" ")]
    predicted_class = classifier.predict([entry])[0]  #PREDICT OCEKUVA LISTA OD LISTI!
    print(predicted_class)

    #DA PROVERIME KOJA E VEROJATNOSTA NA SEKOJA OD KLASITE
    print(classifier.predict_proba([entry]))


