# Este exercício solicita a criação de um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Solicitar informação ao Usuário
medida = float(input('Uma distância em metros: '))

# Cálculo das medidas
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

# Exbir o resultado na tela
print('A medida de {}m corresponde a:\n {}km;\n {}hm;\n {}dam;\n {}dm;\n {}cm;\n {}mm.'.format(medida, km, hm, dam, dm, cm, mm))