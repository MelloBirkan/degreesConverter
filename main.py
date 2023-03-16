print('Bem vindo ao nosso programa de conversão de temperaturas')
conversao = input('Pimeiro qual conversão deseja fazer?("1" para converter de Celsius para Fahrenheit, e "2" de Fahrenheit para Celsius:) ')
if conversao == "1":
  convF_para_C = int(input("Insira aqui a temperatura em CELSIUS, que deseja converter para Fahrenheit: "))
  conversao1 = (convF_para_C *	9/5)	+ 32
  (print(f'Sua temperatura em Fahrenheit é {conversao1}.'))
elif conversao == "2":
  conC_para_F = int(input("Insira aqui a temperatura em FAHRENHEIT, que deseja converter para Celsius: "))
  conversao2 = (conC_para_F - 32) * 5/9
  (print(f'Sua temperatura em Celsius é {conversao2}.'))
else :
  print("Opção invalida certifique-se de digitar '1 ou '2")
