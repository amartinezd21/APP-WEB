def conectar_api(url, timeout=30, retries=3, use_ssl=True):
    return f"conectar a {url} | timeout={timeout} / retries={retries} /  use_ssl={use_ssl}"

print(conectar_api("https://api.ejemplo.com"))