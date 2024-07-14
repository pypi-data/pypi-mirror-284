import winreg as reg


def enable_proxy():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0,
                          reg.KEY_WRITE)
        reg.SetValueEx(key, 'ProxyEnable', 0, reg.REG_DWORD, 1)
        reg.CloseKey(key)
        return True
    except Exception as e:
        return False

def change_proxy(ip, port):
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0,
                          reg.KEY_WRITE)
        proxy_server = f"{ip}:{port}"
        reg.SetValueEx(key, 'ProxyServer', 0, reg.REG_SZ, proxy_server)
        reg.CloseKey(key)
        return True
    except Exception as e:
        return False

def disable_proxy():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0,
                          reg.KEY_WRITE)
        reg.SetValueEx(key, 'ProxyEnable', 0, reg.REG_DWORD, 0)
        reg.CloseKey(key)
        print("\nProxy disabled.")
        return True
    except Exception as e:
        print(f"\nError disabling proxy: {e}")
        return False