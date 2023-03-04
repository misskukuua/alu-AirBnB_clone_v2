#!/usr/bin/env bash
# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create fake HTML file for testing
echo "<html><head><title>Test Page</title></head><body><h1>This is a test page.</h1></body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Set ownership of directories
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_block="location /hbnb_static/ { alias /data/web_static/current/; }"
if ! grep -q "$config_block" "$config_file"; then
  sudo sed -i "/^\s*location\s*\/\s*{\s*$/a $config_block" "$config_file"
fi

# Restart Nginx
sudo service nginx restart

