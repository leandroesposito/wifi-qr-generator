import qrcode
import argparse
import re

def main(argv):    
    # regex to add backslash "\" to problematic characters
    reg = r"([\\\,\;\"\:])"

    # add backslash "\" to problematic characters
    ssid = re.sub(reg, r"\\\1", argv.ssid)
    password = re.sub(reg, r"\\\1", argv.password)

    # generate wifi connection string
    qrtext = "WIFI:S:" + ssid + ";P:" + password + ";T:" + argv.type + ";"
    if argv.hidden is True:
        qrtext += "H:true;"
    qrtext += ";"

    print(qrtext)

    # encoding data using make() function
    img = qrcode.make(qrtext)

    filename = "".join(i for i in ssid if i not in "\/:*?<>|")
    # saving as an image file
    img.save(filename + '.png')

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate a qr code to connect to a wifi network", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--ssid", "-s", action="store", help="SSID or name of wifi network")
    parser.add_argument("--password", "-p", action="store", help="Password of wifi network")
    parser.add_argument("--type", "-t", action="store", help="Authentication type; can be WEP or WPA or WPA2-EAP, or nopass for no password. Or, omit for no password.", default="WPA")
    parser.add_argument("--hidden", "-hi", action="store_true", help="Optional. True if the network SSID is hidden.")

    argv = parser.parse_args()

    main(argv)
