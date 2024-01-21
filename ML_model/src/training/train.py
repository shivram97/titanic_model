from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def training_split(df,y_col,test_size=0.2,random_state=42):
    x = df.drop(y_col,axis=1)
    y = df[y_col]
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=test_size,random_state=random_state)
    return X_train, X_test, y_train, y_test


def train(X_train, y_train,model_name='lr'):
    """
    Trains a machine learning model using the given training data.

    Parameters:
        X_train (array-like): The input feature array for training.
        y_train (array-like): The target array for training.
        model_name (str, optional): The name of the model to be trained. Defaults to 'lr'.

    Returns:
        model (object): The trained machine learning model.
    """
    if model_name=='lr':
        model = LogisticRegression()
    elif  model_name=='rf':
        model = RandomForestClassifier()
    else:
        raise Exception("Invalid model name")
    model = LogisticRegression()
    model.fit(X_train,y_train)
    return model