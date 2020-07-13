#!/bin/bash
#!/bin/sh

banner() {
clear

printf "*********************************************************************************************************************\n"
printf "██████╗ ██╗      ██████╗  ██████╗██╗  ██╗        ██╗    ██╗   ██╗███╗   ██╗██████╗ ██╗      ██████╗  ██████╗██╗  ██╗\n"
printf "██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝       ██╔╝    ██║   ██║████╗  ██║██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝\n"
printf "██████╔╝██║     ██║   ██║██║     █████╔╝       ██╔╝     ██║   ██║██╔██╗ ██║██████╔╝██║     ██║   ██║██║     █████╔╝ \n"
printf "██╔══██╗██║     ██║   ██║██║     ██╔═██╗      ██╔╝      ██║   ██║██║╚██╗██║██╔══██╗██║     ██║   ██║██║     ██╔═██╗ \n"
printf "██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗    ██╔╝       ╚██████╔╝██║ ╚████║██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗\n"
printf "╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝         ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝\n"
printf "********************************************************************************************************************\n"   

}
menu() {
printf "\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m BLOCK\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m UNBLOCK\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m03\e[0m\e[1;92m]\e[0m\e[1;93m WHITELIST\e[0m\n"
printf  "\n"
printf "\e[1;93m[\e[0m\e[1;77m99\e[0m\e[1;93m]\e[0m\e[1;77m DONE YOUR SETTING\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose an option:\e[0m\e[1;77m ' option

if [[ $option == 1 || $option == 01 ]]; then
printf "\n"
printf "\n"
printf "\e[1;92m\e[0m\e[1;77m\e[0m\e[1;92m\e[0m\e[1;93m BLOCK\e[0m\n"
read -p 'DOMAIN: ' domain
pihole --regex '(^|\.)'$domain'\.com$'
sleep 2
clear
menu


elif [[ $option == 2 || $option == 02 ]]; then
printf "\n"
printf "\n"
printf "\e[1;92m\e[0m\e[1;77m\e[0m\e[1;92m\e[0m\e[1;93m UNBLOCK\e[0m\n"
read -p 'DOMAIN:' domain
pihole -b -d --regex '(^|\.)'$domain'\.com$'
sleep 2
clear
menu

elif [[ $option == 3 || $option == 03 ]]; then
printf "\n"
printf "\n"
printf "\e[1;92m\e[0m\e[1;77m\e[0m\e[1;92m\e[0m\e[1;93m UNBLOCK\e[0m\n"
read -p 'DOMAIN:' domain
pihole -w $domain'\.com$'
sleep 2
clear
menu
elif [[ $option  == 99 ]]; then
exit 1
else
printf "\e[5;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
sleep 0.5
clear
menu
banner
fi
}
banner
menu
