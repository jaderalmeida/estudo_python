def main():
   total_segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

   dias = total_segundos // 86400
   resto_dia = total_segundos % 86400
   
   horas = resto_dia // 3600
   resto_hora = resto_dia % 3600 

   minutos = resto_hora // 60
   segundos = resto_hora % 60

   print(dias,"dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")

main()