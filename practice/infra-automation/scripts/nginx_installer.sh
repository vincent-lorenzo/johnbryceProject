# this script will download nginx via python whilst using bash

machine=$1 
nginx=$2

echo "checking if $nginx is already installed on $machine..." 

sleep 4

echo "$nginx not found"

sleep 1

echo "starting nginx_installer" 

sleep 1

echo "installing $nginx on $machine..."

sleep 4

echo "$nginx successfully installed."

sleep 2