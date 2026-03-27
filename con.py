rom sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_train_5, y_train_pred)
y_train_perfect_predictions = y_train_5 # pretend we reached perfection
confusion_matrix(y_train_5, y_train_perfect_predictions
