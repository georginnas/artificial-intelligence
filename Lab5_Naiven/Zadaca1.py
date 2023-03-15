# STANUVA ZBOR ZA AVTOMOBILI  KADE STO KE TREBA DA NAPRAVIME PREDVIDUVANJE DALI EDEN AVTOMOBIL E RPIFATLIV ILI NE
# IMAME SAMO KATEGORISKI ATRIBUTI (1, 2, 3 ILI POVEKE) treba string da se pojavi za da bide kategoriski!
import csv
from sklearn.preprocessing import OrdinalEncoder #ovoj gi konvertira vo brojki atributite
from sklearn.naive_bayes import CategoricalNB
def read_file(doc):
    with open(doc) as f:
        csv_reader=csv.reader(f,delimiter=',')
        dataset=list(csv_reader)[1:]
    return dataset
if __name__=="__main__":
    dataset=read_file('cars.csv')
    encoder=OrdinalEncoder() #treba da nauci sega kako da go pravi toa mapiranje
    encoder.fit([row[:-1] for row in dataset]) #treba da nauci (da trenira) od koi podatoci treba da mapira(bez klasniot posleden)

    train_set=dataset[:int(len(dataset)*0.7)] #mnoz za treniranje
    train_x=[row[:-1] for row in train_set] #karakteristiki
    train_y=[row[-1] for row in train_set] #klasata
    train_x=encoder.transform(train_x) #se pravi transformacija na mnozestvoto na treniranje vo brojki

    test_set=dataset[int(len(dataset)*0.7):] #mnoz za testiranje
    test_x=[row[:-1] for row in test_set] #karakteristiki
    test_y=[row[-1] for row in test_set] #klasata
    test_x=encoder.transform(test_x) #se rpavi transformacija na mnozestvoto na testiranje vo brojki

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y) #treniranje povikuvame samo so mnoz train
    predicted_class=classifier.predict([test_x[0]])[0] #za prviot primerok od testirackoto mnoz ni predviduva klasa(klasata mora da e string inaku ke e lista ako go nemame toa[0]
    true_class=test_y[0]

    acc=0 #tocnost, t.e kolku primeroci imame pogodeno
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class==true_class:
            acc+=1

    new=acc/len(test_set)
    print(f'Accuracy: {new}')

    entry=[el for el in input().split(" ")]
    encoded_entry=encoder.transform([entry])
    predicted_class=classifier.predict(encoded_entry)[0] #['unnac'] e ako nemame [0], ako imame [0] togas e: unacc
    print(predicted_class)


