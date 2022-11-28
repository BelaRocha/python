#algoritimo senha 
import random
senhaCerta = random.randint (1,50)
#se quiser mostrar a senha: 
#print(senhaCerta)
senhaUsuario = 0
while senhaUsuario != senhaCerta:
	senhaUsuario = int(input('insira sua senha:'))
	if senhaUsuario > senhaCerta:
		print('A senha certa é menor do que a tentativa anterior, tente novamente ')
	elif senhaUsuario < senhaCerta:
		print('A senha certa é maior do que a tentativa anterior, tente novamente ')
		
print('senha correta, acesso liberado!')
print('fim =3')