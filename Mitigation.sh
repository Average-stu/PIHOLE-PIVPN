#!/bin/bash
#!/bin/sh
banner() {
clear
printf "************************************************************************************************ \n"
printf "███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗       ███████╗███████╗████████╗██╗   ██╗██████╗ \n"
printf "██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗      ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗\n"
printf "███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝█████╗███████╗█████╗     ██║   ██║   ██║██████╔╝\n"
printf "╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════╝╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ \n"
printf "███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║      ███████║███████╗   ██║   ╚██████╔╝██║     \n"
printf "╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝      ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     \n"
printf "**************************************************************************************************\n"    

}
menu() {
printf "\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m TO INSTALL PI-HOLE (FOR YOUR OWN DNS)\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m TO INSTALL PI-VPN (FOR YOUR VPN)\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m03\e[0m\e[1;92m]\e[0m\e[1;93m FOR MANGING THE DNS\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m04\e[0m\e[1;92m]\e[0m\e[1;93m FOR ADDING THE CLIENT FOR VPN\e[0m\n"

printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m99\e[0m\e[1;93m]\e[0m\e[1;77m Exit\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose an option:\e[0m\e[1;77m ' option

if [[ $option == 1 || $option == 01 ]]; then
curl -sSL https://install.pi-hole.net | bash
clear
banner
menu

elif [[ $option == 2 || $option == 02 ]]; then
curl -L https://install.pivpn.io | bash
clear
banner
menu

elif [[ $option == 3 || $option == 03 ]]; then
bash yourblacklist.sh
clear
banner
menu

elif [[ $option == 4 || $option == 04 ]]; then
bash Addclient.sh
clear
banner
menu



elif [[ $option  == 99 ]]; then
exit 1
else
printf "\e[5;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
sleep 0.5
clear
menu
fi
}
banner
menu

