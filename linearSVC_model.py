SVCmodel = LinearSVC()
SVCmodel.fit(X_train, y_train)
model_Evaluate(SVCmodel)






#           precision    recall  f1-score   support

#           0       0.82      0.81      0.82     39989
#           1       0.81      0.83      0.82     40011

#    accuracy                           0.82     80000
#   macro avg       0.82      0.82      0.82     80000
#weighted avg       0.82      0.82      0.82     80000
