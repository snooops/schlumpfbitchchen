#!/bin/bash


for map in `ls $HOME/maps`; do
	# copy the map into the ut4 server dir
	cp $HOME/maps/$map $HOME/LinuxServer/UnrealTournament/Content/Paks/

	# copy the map into the web dir
	cp $HOME/maps/$map /var/www/dns-serve.de/html/ut4-paks/
	
	# remove .pak suffix
	modname=${map:0:${#map}-4};
	
	# let ut4 generate a game.ini for the map, so clients now where they can download the content
	$HOME/LinuxServer/Engine/Binaries/Linux/UE4Server-Linux-Shipping UnrealTournament -run=UTGenerateRedirects -Package=$modname -WebAddress=https://dns-serve.de/ut4-paks/$map

	# remove the map from the ftp
	rm -r $HOME/maps/$map
done

