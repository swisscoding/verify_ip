#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Verify IPv4/IPv6 address | ----\n", fg("red")))

# class
class Verify:
    def valid_ip_address(self, ip):
        def is_ipv4(string):
            try:
                return str(int(string)) == string and 0 <= int(string) <= 255
            except:
                return False

        def is_ipv6(string):
            if len(string) > 4:
                return False
            try:
                return int(string, 16) >= 0 and string[0] != '-'
            except:
                return False

        if ip.count(".") == 3 and all(is_ipv4(i) for i in ip.split(".")):
            return "IPv4"

        if ip.count(":") == 7 and all(is_ipv6(i) for i in ip.split(":")):
            return "IPv6"

        return -1

# user interaction
ip = input("Enter IPv4/IPv6: ")

# output
check = Verify().valid_ip_address(ip)

if check != -1:
    check = stylize(Verify().valid_ip_address(ip), fg("red"))
    print(f"\nGiven IP Address \"{ip}\" is\nan {check}.\n")
else:
    print("\nInvalid IP Address\n")
