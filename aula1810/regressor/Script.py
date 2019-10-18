from sklearn import svm, neural_network, metrics, datasets
import numpy as np
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

db = datasets.load_boston()

X = db.data
Y = db.target

np.random.seed(0)

amostras = len(X)
divisao = 0.75

embaralhar = np.random.permutation(amostras)

X = X[embaralhar]
Y = Y[embaralhar]

X_treino = X[:int(amostras*divisao)]
Y_treino = Y[:int(amostras*divisao)]

X_teste = X[:int(amostras*divisao)]
Y_teste = Y[:int(amostras*divisao)]

parametros_srv = {'kernel':('linear','poly','sigmoid','tbf'),'C':[1,2,3]}

svr = svm.SVR(gamma = 'scale')

#parametros_srv['kernel'][0]

clf = GridSearchCV(svr,parametros_srv,n_jobs=5,verbose=3)

#print(clf.best_params_)

clf.fit(X_treino,Y_treino)

print (clf.best_params_)

predicao = clf.predict(X_teste)

mse = metrics.mean_squared_error(Y_teste,predicao)
r2 = metrics.r2_score(Y_teste,predicao)

print('MSE: ',mse)
print('R2: ',r2)

diagonal = list(range(int(min(Y_teste)),int(max(Y_teste))))

plt.title('predição: SVR')
plt.xlabel('original')
plt.ylabel('predição')

plt.scatter(Y_teste,predicao)
plt.plot(diagonal,diagonal,'r--')
plt.show()


#plt.scatter(Y_teste,predicao)
#plt.show()