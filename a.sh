echo 'Loading Script'
sleep 3
echo 'loading remote configs from Abhilashs_RPI_in_chennai..'
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
echo 'Starting Extraction...'
sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
echo 'Extraction Complete'
sleep 2
echo 'Sending Status to Abhilashs_RPI_in_chennai..'
sleep 3
echo 'DONE'
