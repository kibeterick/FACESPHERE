"""Check if SMTP port is accessible"""
import socket

def check_port(host, port, timeout=5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False

print("Checking SMTP connectivity...")
print(f"Port 587 (TLS): {'✅ Open' if check_port('smtp.gmail.com', 587) else '❌ Blocked'}")
print(f"Port 465 (SSL): {'✅ Open' if check_port('smtp.gmail.com', 465) else '❌ Blocked'}")
print(f"Port 25 (Plain): {'✅ Open' if check_port('smtp.gmail.com', 25) else '❌ Blocked'}")
