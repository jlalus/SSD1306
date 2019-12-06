#welcome in initil script!
#change SSID and PASSWORD to  your names
#sudo nmcli dev wifi connect "SSID" password "PASSWORD" infname wlan0
cd ~
sudo apt-get update
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install Adafruit-SSD1306
sudo pip install Pillow

sudo apt install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential libopenjp2-7 libtiff5
sudo apt install libsdl-dev libportmidi-dev libsdl-ttf2.0-dev libsdl-mixer1.2-dev libsdl-image1.2-dev
git clone https://github.com/rm-hull/luma.examples.git
cd luma.examples
sudo -H pip install --upgrade luma.oled

# run example
sudo python ~/SSD1306/luma.examples/examples/clock.py --i2c-port 0

# Y Y