#KOLEKCIJA NA KLASIFIKATORI
import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
def read_file(doc):
    with open(doc) as f:
        csv_reader=csv.reader(f,delimiter=',')
        dataset=list(csv_reader)[1:]
    return dataset
if __name__=="__main__":
    dataset=read_file('cars.csv')
    encoder = OrdinalEncoder()  # treba da nauci sega kako da go pravi toa mapiranje
    encoder.fit([row[:-1] for row in
                 dataset])  # treba da nauci (da trenira) od koi podatoci treba da mapira(bez klasniot posleden)

    train_set = dataset[:int(len(dataset) * 0.7)]  # mnoz za treniranje
    train_x = [row[:-1] for row in train_set]  # karakteristiki
    train_y = [row[-1] for row in train_set]  # klasata
    train_x = encoder.transform(train_x)  # se pravi transformacija na mnozestvoto na treniranje vo brojki

    test_set = dataset[int(len(dataset) * 0.7):]  # mnoz za testiranje
    test_x = [row[:-1] for row in test_set]  # karakteristiki
    test_y = [row[-1] for row in test_set]  # klasata #NE SEKOGAS KLASATA MOZE DA BIDE NA POSLEDNA POZICIJA
    test_x = encoder.transform(test_x)  # se rpavi transformacija na mnozestvoto na testiranje vo brojki

    #NAJVAZEN ATRIBUT, KOLKU DRVA KE SE KORISTAT PO DEFAULT E 100
    classifier=RandomForestClassifier(n_estimators=150, criterion='entropy', random_state=0)
    classifier.fit(train_x,train_y)
    acc = 0  # tocnost, t.e kolku primeroci imame pogodeno
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            acc += 1

    new = acc / len(test_set)
    print(f'Accuracy: {new}')

    features_importances = list(
        classifier.feature_importances_)  # ke ni ja dade listata na vaznosti na sekoj od atributite
    print(f'Feature imporatnces: {features_importances}')
    most_important_feature = features_importances.index(max(
        features_importances))  # TUKA NAOGAME KOJA KARAKTERISTIKA E NAJMNOGU VAZNA ODNOSNOSNO SO MAX JA ZEMAME NAJGOLEMATA VREDNOST (bezbednosta)
    print(f'Most important feature: {most_important_feature}')
    least_important_feature = features_importances.index(
        min(features_importances))  # tuka e najmalku vaznata karakteristika odnsono brojot na vrati
    print(f'Least important feature: {least_important_feature}')