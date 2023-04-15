# wifi-qr-generator

Generate a QR code to connect to a WIFI network.

## Usage

 ```
 py wifi_qr_generator.py --ssid SSID --password PASSWORD --type TYPE --hidden
 ```
 
 --ssid SSID < SSID or name of wifi network
 
 --password PASSWORD < Password of wifi network
 
 --type TYPE < Authentication type; can be WEP or WPA or WPA2-EAP, or nopass for no password. (default: WPA)
 
 --hidden < If the network SSID is hidden. (default: False)
