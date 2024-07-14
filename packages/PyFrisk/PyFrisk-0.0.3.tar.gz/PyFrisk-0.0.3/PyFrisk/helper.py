import requests
from lxml.html import fromstring

def get_free_proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve proxies: {response.status_code}")

    parser = fromstring(response.text)
    proxies = []

    rows = parser.xpath('//tbody/tr')
    for i in rows:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            try:
                ip = i.xpath('.//td[1]/text()')[0]
                port = i.xpath('.//td[2]/text()')[0]
                proxy = {
                    "ip": ip,
                    "port": port,
                }
                proxies.append(proxy)
            except IndexError:
                continue

    return proxies

def split_ip_port(ip_port_str):
    try:
        ip, port = ip_port_str.split(':')

        if not (0 <= int(port) <= 65535):
            raise ValueError("Port number is out of valid range")

        return ip, int(port)

    except ValueError as e:
        print(f"Error: {e}")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None
