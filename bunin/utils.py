import socket

def extract_this_pc_ip_address() -> str:
    CHECK_ADDRESS: str = '10.255.255.255'
    IP: str = ''
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as st:
        try:
            st.connect((CHECK_ADDRESS, 1))
            IP = st.getsockname()[0]
        except Exception:
            IP = socket.gethostbyname(socket.getfqdn())
    return IP

print(extract_this_pc_ip_address())
