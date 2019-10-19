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

parametros_srv = {'kernel':('linear','poly','sigmoid','rbf'),'C':[1,2,3]}

svr = svm.SVR(gamma = 'scale')

#parametros_srv['kernel'][0]

clf = GridSearchCV(svr,parametros_srv,n_jobs=5,verbose=3)

clf.fit(X_treino,Y_treino)

print (clf.best_params_)

predicao = clf.predict(X_teste)

mse = metrics.mean_squared_error(Y_teste,predicao)
r2 = metrics.r2_score(Y_teste,predicao)

print('svr')
print('MSE: ',mse)
print('R2: ',r2)

clf1 = neural_network.MLPRegressor(hidden_layer_sizes=(26,),max_iter=1500)
clf1.fit(X_treino,Y_treino)
predicao_rede = clf1.predict(X_teste)

mse_rede = metrics.mean_squared_error(Y_teste,predicao_rede)
r2_rede = metrics.r2_score(Y_teste,predicao_rede)

print('MLP')
print('MSE: ',mse_rede)
print('R2: ',r2_rede)

diagonal = list(range(int(min(Y_teste)),int(max(Y_teste))))

plt.title('predição: SVR e MLP')
plt.xlabel('original')
plt.ylabel('predição')

plt.scatter(Y_teste,predicao, label='SVR = {}'.format(r2))
plt.scatter(Y_teste,predicao_rede, label='MLP = {}'.format(r2_rede))
plt.plot(diagonal,diagonal,'r--', label='objetivo')
plt.legend(loc='upper left')

plt.show()


#plt.scatter(Y_teste,predicao)
#plt.show()