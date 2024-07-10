from mactools import MacAddress
# from ipaddress import IPv6Address as IPv6

# mac = MacAddress('246D.5EBB.99CC')
# print(f'fe80::{mac.eui64_suffix}')

# # IPv6(f'{mac.get_eui64_suffix}')

# print(hex(9+2)[2:])

# print(ord('9'))
# print(ord)


# print(str(mac.get_global_address('2605:A404:27C1:1990')))

mac = MacAddress('00:11:22:AA:BB:CC')
print(mac.decimal)
print(mac.eui64_suffix)
print(mac.link_local_address)
print(mac.oui)