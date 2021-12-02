## How to setup your Gaia-X Full Node

```bash
# Create a new folder
mkdir gaia-x-node && cd gaia-x-node
# Download the openethereum client
wget https://github.com/openethereum/openethereum/releases/download/v3.2.6/openethereum-linux-v3.2.6.zip
# unzip the client
sudo apt-get install unzip
unzip openethereum-linux-v3.2.6.zip

# update your config file
vim config.toml

# run your client with the config file
chmod +x openethereum
sudo ./openethereum --config config.toml --reserved-peers bootnodes.txt
```