import csv
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler,MinMaxScaler
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

    scaler=StandardScaler()
    scaler.fit(train_x)
    scaler2=MinMaxScaler()
    scaler2.fit(train_x)

    classifier = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3= MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x, train_y)
    classifier2.fit(scaler.transform(train_x),train_y)
    classifier3.fit(scaler2.transform(train_x),train_y)

    val_acc1=0
    val_predictions=classifier.predict(val_x)
    for true, pred in zip(val_y, val_predictions):
        if true==pred:
            val_acc1+=1

    val_acc1=val_acc1/len(val_y)
    print(f'Bez normalizacija imame tochnost so validacisko mnozestvo od {val_acc1}')

    val_acc2 = 0
    val_predictions = classifier2.predict(scaler.transform(val_x))
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc2 += 1

    val_acc2 = val_acc2 / len(val_y)
    print(f'So standardna normalizacija imame tochnost so validacisko mnozestvo od {val_acc2}')

    val_acc3 = 0
    val_predictions = classifier3.predict(scaler2.transform(val_x))
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc3 += 1

    val_acc3 = val_acc3 / len(val_y)
    print(f'So minmax skaliranje imame tochnost so validacisko mnozestvo od {val_acc3}')



    tp,fp,tn,fn=0,0,0,0
    predictions=classifier3.predict(scaler2.transform(test_x))
    for pred, true in zip(predictions,test_y):
        if true=='good': #DALI VISTINSKATA GLASA NI E GOOD
            if pred==true: #DOKOLKU PREDVIDUVANJETO NI E VISTINSKATA VREDNOST
                tp+=1 #IMAME TRUE POSITIVE (TOCNO PREDVIDUVANJE ZA GOOD)
            else:
                fn+=1 #IMAME POZITIVNA KLASA STO TREBA DA SE PREDVIDI NO NIE PREDVIDUVAME NEGATIVNA TOA ZNACI IMAME LAZNO NEGATIVNO PREDVIDUVANJE FALSE NEGATIVE
        else:
            if pred==true: #KOGA TRUE KLASATA NI E BAD, KOGA PREDVIDUVANJETO NI E EDNAKVO NA VISTINSKATA VRNOST ODNOSNO NA BAD TOGAS
                tn+=1 #TRUE NEGATIVE
            else:
                fp+=1 #A\IMAME VISTINSKA VREDNOST BAD A NIE SME PREDVIDILE GOOD TOGAS IMAME LAZNO POZITIVNA KLASA

    acc=(tp+tn)/(tp+fp+tn+fn)
    precision=tp/(tp+fp)
    recall=tp/(tp+fn)

    print('Evaluacija')
    print(f'Tochnost: {acc}')
    print(f'Preciznost: {precision}')
    print(f'Odziv: {recall}')
