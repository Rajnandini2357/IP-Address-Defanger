def defang_ip_address(ip_address):
    defanged_ip = ip_address.replace('.','[.]')
    return defanged_ip
ip_address = input("Enter an IP address: ")
defanged_ip = defang_ip_address(ip_address)
print("Original IP address :",ip_address)
print("Defanged IP address :",defanged_ip)








































