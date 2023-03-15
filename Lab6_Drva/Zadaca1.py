import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
def read_file(doc):
    with open(doc) as f:
        csv_reader=csv.reader(f,delimiter=',')
        dataset=list(csv_reader)[1:]
    return dataset
if __name__=="__main__":
    dataset=read_file('cars.csv')

    encoder = OrdinalEncoder()  # treba da nauci sega kako da go pravi toa mapiranje
    encoder.fit([row[:-1] for row in dataset])  # treba da nauci (da trenira) od koi podatoci treba da mapira(bez klasniot posleden)

    train_set = dataset[:int(len(dataset) * 0.7)]  # mnoz za treniranje
    train_x = [row[:-1] for row in train_set]  # karakteristiki
    train_y = [row[-1] for row in train_set]  # klasata
    train_x = encoder.transform(train_x)  # se pravi transformacija na mnozestvoto na treniranje vo brojki

    test_set = dataset[int(len(dataset) * 0.7):]  # mnoz za testiranje
    test_x = [row[:-1] for row in test_set]  # karakteristiki
    test_y = [row[-1] for row in test_set]  # klasata #NE SEKOGAS KLASATA MOZE DA BIDE NA POSLEDNA POZICIJA
    test_x = encoder.transform(test_x)  # se rpavi transformacija na mnozestvoto na testiranje vo brojki

    #SE STAVAAT ATRIBUTI VO KLASIFIKATOR
    #PRVIOT ATRIBUT STO KE GO DEFINIRAME E SPORED KOJ KRITERIUM SAKAME DA SE PRAVI PODELBA NA ATRIBUTITE VO DRVOTO, ako ne definirime po default e gini
    #max_depth e maksimalnata vrednost na dlabocina na drvoto, po default e ke se najde optimalno nekoe
    #max_leaf_nodes ke ni kaze kolku najnogu listovi smeeme da imame vo drvoto
    #random state e da bideme sigurno deka vo sekoe izvrsuvanje ke gi dobieme istite rezultati so nula ke se kontrolira slucajnosta na podelba i ke bideme sigurni deka sekogas ke dobivame isti rezultati
    #classifier=DecisionTreeClassifier(criterion='entropy', max_depth=5, max_leaf_nodes=20, random_state=0)
    classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
    classifier.fit(train_x,train_y)

    print(f'Depth: {classifier.get_depth()}') #dlabocina
    print(f'Number of leaves: {classifier.get_n_leaves()}') #broj na lisja

    acc = 0  # tocnost, t.e kolku primeroci imame pogodeno
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            acc += 1

    new = acc / len(test_set)
    print(f'Accuracy: {new}')

    #SAMO KAJ DRVA MOZEME DA VIDIME KOJA KARAKTERSTIKA VLIJAELA NAJMNOGU A KOJA NAJMALKU VO PROCESOT NA TRENIRANJE, T.E KOJA E NAJVAZNA A KOJA E NAJMALKU VAZNA
    features_importances=list(classifier.feature_importances_) #ke ni ja dade listata na vaznosti na sekoj od atributite
    print(f'Feature imporatnces: {features_importances}')
    most_important_feature=features_importances.index(max(features_importances)) #TUKA NAOGAME KOJA KARAKTERISTIKA E NAJMNOGU VAZNA ODNOSNOSNO SO MAX JA ZEMAME NAJGOLEMATA VREDNOST (bezbednosta)
    print(f'Most important feature: {most_important_feature}')
    least_important_feature = features_importances.index(min(features_importances)) #tuka e najmalku vaznata karakteristika odnsono brojot na vrati
    print(f'Least important feature: {least_important_feature}')

    #NAREDNO KE OTSTRANIME KARAKTERISTIKA, AKO JA OTSTRANIME NAJVAZNATA PROCENTOT NA TOCNOST KE BIDE POMAL ZS GO TRGAME ONA STO E NAJVAZNO ZA MODELOT
    #AKO SE OTSTRANI NAJMALKU VAZNATA KE DOBIEME NA VREME

    #OTSTRANUVANJE NA MOST IMPORTANT FEATURE
    train_x_2=list()
    for t in train_x:
        row=[t[i] for i in range(len(t)) if i!=most_important_feature]
        train_x_2.append(row)
    test_x_2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x_2.append(row)

    #OTSTRANUVANJE NA LEAST IMPORTANT FEATURE
    train_x_3 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        train_x_3.append(row)
    test_x_3 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        test_x_3.append(row)
    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(train_x_2, train_y)

    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(train_x_3, train_y)
    print(f'Depth(without most important): {classifier2.get_depth()}')  # dlabocina
    print(f'Number of leaves: {classifier2.get_n_leaves()}')  # broj na lisja
    print(f'Depth(without least important): {classifier3.get_depth()}')  # dlabocina
    print(f'Number of leaves: {classifier3.get_n_leaves()}')  # broj na lisja

    acc2 = 0  # tocnost, t.e kolku primeroci imame pogodeno
    for i in range(len(test_set)):
        predicted_class = classifier2.predict([test_x_2[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            acc2 += 1

    new = acc2 / len(test_set)
    print(f'Accuracy2: {new}')

    acc3 = 0  # tocnost, t.e kolku primeroci imame pogodeno
    for i in range(len(test_set)):
        predicted_class = classifier3.predict([test_x_3[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            acc3 += 1

    new = acc3 / len(test_set)
    print(f'Accuracy3: {new}')

    #AKO SE OTSTRANI NAJVAZNATA TOCNOSTA KE SE NAMALI, AKO SE OTSRANI NAJMALKU VAZNATA MOZE DA SE ZGOLEMI PROCENTOT
    print()