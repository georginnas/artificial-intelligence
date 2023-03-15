import csv
from sklearn.neural_network import MLPClassifier

def read_file(readfile):
    with open(readfile) as file:
        csv_reader=csv.reader(file, delimiter=";")
        dataset=list(csv_reader)[1:]
    data=[]
    for row in dataset:
        data.append(list(map(float,row[:-1])) + row[-1:]) #ke gi napravi site float da bidat osven posledniot clen sto mora string da ostane!
    return data
def divide_sets(dataset):
    bad_class=[row for row in dataset if row[-1]=='bad']
    good_class=[row for row in dataset if row[-1]=='good']
    return bad_class,good_class


if __name__=="__main__":

    dataset=read_file('wine.csv')
    bad_class,good_class=divide_sets(dataset)
    train_set=bad_class[:int(0.7*len(bad_class))]+good_class[:int(0.7*len(good_class))]
    train_x=[row[:-1] for row in train_set]
    train_y=[row[-1] for row in train_set]


    val_set=bad_class[int(0.7*len(bad_class)):int(0.8*len(bad_class))]+good_class[int(0.7*len(good_class)):int(0.8*len(good_class))]
    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    test_set=bad_class[int(0.8*len(bad_class)):]+good_class[int(0.8*len(good_class)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]


    classifier=MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2=MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3=MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x,train_y)
    classifier2.fit(train_x,train_y)
    classifier3.fit(train_x,train_y)

    final_classifier=None
    max_acc = 0
    for i, c in enumerate([classifier, classifier2, classifier3]): #KE NIO DADE TORKA OD INDEKS I ELEMENT
        val_predictions=c.predict(val_x)
        val_acc=0
        for true, pred in zip(val_y, val_predictions):
            if true==pred:
                val_acc+=1
        new_acc=val_acc/len(val_y)
        print(f'Klasifikatorot {i} ima tochnost so validacisko mnozestvo od {new_acc}')

        if val_acc > max_acc:
            max_acc=val_acc
            final_classifier=c  #NA OVOJ NACIN GO NAOGAME KOJ E KLASIFIKATOROT SO NAJDOBRA TOCNOST
    #Tocnos so najdobriot klasifikator na testiracko mnozestvo:

    acc=0
    predictions=final_classifier.predict(test_x)

    for true,pred in zip(test_y,predictions):
        if true==pred:
            acc+=1
    acc=acc/len(test_y)

    print(f'Tochnosta na testirackoto mnozestvo e: {acc}')
