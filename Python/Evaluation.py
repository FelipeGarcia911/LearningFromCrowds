import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt

def split_train_test_ma_rd(attr_df, labels_df):
    return train_test_split(attr_df, labels_df, test_size=0.3, random_state = 0, shuffle = True)

def split_train_test_ma(attr_df, labels_df):
    X_train, X_test, y_train, y_test =  train_test_split(attr_df, labels_df, test_size=0.3, random_state = 0, shuffle = True)
    y_train = y_train.drop(columns=['y'])
    y_test = y_test[['y']]
    return X_train, X_test, y_train, y_test
    
def split_train_test(attr_df, labels_df):
    train_dfs = split_gold_standard(attr_df, labels_df)
    test_dfs = split_estimated(attr_df, labels_df)
    return train_dfs[0], train_dfs[1], test_dfs[1], train_dfs[2], train_dfs[3], test_dfs[3]

def split_gold_standard(attr_df, labels_df):
    return train_test_split(attr_df, labels_df[['y']], test_size=0.3, random_state = 0, shuffle = True)

def split_estimated(attr_df, labels_df):
    return train_test_split(attr_df, labels_df[['Z']], test_size=0.3, random_state = 0, shuffle = True)

def train_model(X_train, y_train):
    model = LogisticRegression(random_state=0, solver='liblinear', penalty='l2')
    return model.fit(X_train, y_train.values.ravel())

def test_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    eval_model_roc(y_test, y_pred, model, X_test)

def compute_roc_curve(y_test, y_score):
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    return fpr, tpr, roc_auc 
    
def plot_roc_curve(fpr, tpr, roc_auc):
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange', lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()

def eval_model(y_test, y_pred):
    print("-- Global Precision --")
    print(accuracy_score(y_test, y_pred))
    print("\n")

    print("-- General Report --")
    print(classification_report(y_test, y_pred, target_names=['yes','no']))
    print("\n")

    print("-- Confusion Matrix --")
    matriz_confusion = confusion_matrix(y_test, y_pred)
    table = pd.DataFrame(matriz_confusion)
    print(table)
    
def eval_model_roc(y_test, y_pred, model, X_test):
    eval_model(y_test, y_pred)
    
    print("\nROC Curve: \n")
    y_score = model.decision_function(X_test)
    fpr, tpr, roc_auc = compute_roc_curve(y_test, y_score)
    print("ROC AUC: ", roc_auc)
    plot_roc_curve(fpr, tpr, roc_auc)
    
def eval_model_roc_2(y_test, y_pred, y_score):
    eval_model(y_test, y_pred)

    print("\nROC Curve: \n")
    fpr, tpr, roc_auc = compute_roc_curve(y_test, y_score)
    print("ROC AUC: ", roc_auc)
    plot_roc_curve(fpr, tpr, roc_auc)