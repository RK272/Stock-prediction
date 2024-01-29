from sklearn.base import BaseEstimator, TransformerMixin
import pandas_ta as ta

class NameDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(['datetime'], axis=1)

class rsi(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self


    def transform(self, X):


        X['rsi']=ta.rsi(X.close,length=14)
        X['rsi'] = ta.rsi(X.close, length=9)
        X['ema20']=ta.ema(X.close,length=20)
        X['ema5'] = ta.ema(X.close, length=5)
        X['ema100']=ta.ema(X.close,length=100)
        X['ema200'] = ta.ema(X.close, length=200)
        return X