import socket

import requests
import ipaddress

def get_geolocation(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Failed to retrieve geolocation data: {e}")
        return {}


def get_ip_from_domain(domain_name):
    try:
        ip_addresses = socket.gethostbyname_ex(domain_name)[2]

        return ip_addresses
    except socket.gaierror as e:
        print(f"Error resolving domain '{domain_name}': {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
