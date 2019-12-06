udo nmcli dev wifi connect "SSID" password "PASSWORD" infname wlan0
sudo apt update
sudo apt install ufw
sudo apt install openssh-server
#sudo systemctl status ssh
git clone https://github.com/jlalus/SSD1306.git
sudo cp SSD1306/sshd_config /etc/ssh/sshd_config
sudo service ssh restart
sudo ufw enable
sudo ufw allow ssh


sudo cp ~/SSD1306/sshd_config /etc/ssh/sshd_config
