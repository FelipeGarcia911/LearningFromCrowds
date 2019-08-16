def createDbAttributes(X):
    X.to_csv('database_attr.csv', sep=',',index=False)
    
def createDbLabels(Y):
    Y.to_csv('database_labels.csv', sep=',',index=False)
    
def createDbSGS(Z):
    Z.to_csv('database_labels_sgs.csv', sep=',',index=False)
    
def saveDataframe(dataframe, path, filename):
    dataframe.to_csv(path + filename, sep=',',index=False)