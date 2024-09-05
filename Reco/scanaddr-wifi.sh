#!/bin/bash

# Détermine l'interface réseau Wi-Fi
interface="wlan0"

# Obtient l'adresse IP locale et le masque de sous-réseau
ip_info=$(ip -4 addr show $interface | grep -oP '(?<=inet\s)\d+(\.\d+){3}/\d+')
local_ip=$(echo $ip_info | cut -d'/' -f1)
cidr=$(echo $ip_info | cut -d'/' -f2)

# Calcule l'adresse réseau
IFS=. read -r i1 i2 i3 i4 <<< "$local_ip"
network=$(printf "%d.%d.%d.0" "$i1" "$i2" "$i3")

# Calculer la plage d'adresses IP à scanner
start_ip=$(printf "%d.%d.%d.1" "$i1" "$i2" "$i3")
end_ip=$(printf "%d.%d.%d.254" "$i1" "$i2" "$i3")

echo "Scan du réseau $network/$cidr..."

# Fonction pour effectuer un ping et vérifier si l'hôte est actif
ping_host() {
    local ip=$1
    if ping -c 1 -W 1 $ip &> /dev/null; then
        echo "Hôte actif : $ip"
    fi
}

# Scanner la plage d'adresses IP
for i in $(seq 1 254); do
    ip=$(printf "%d.%d.%d.%d" "$i1" "$i2" "$i3" "$i")
    ping_host $ip &
done

# Attendre que tous les pings soient terminés
wait

echo "Scan terminé"
