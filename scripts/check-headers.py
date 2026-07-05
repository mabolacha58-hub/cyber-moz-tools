import urllib.request
import urllib.error
import sys
import json

HEADERS_SEGURANCA = {
    "Strict-Transport-Security": "Força conexão HTTPS",
    "Content-Security-Policy": "Controla o que pode ser carregado na página",
    "X-Content-Type-Options": "Evita que navegador adivinhe o tipo de arquivo",
    "X-Frame-Options": "Protege contra clickjacking",
    "X-XSS-Protection": "Proteção contra ataques XSS",
    "Referrer-Policy": "Controla envio de referência ao navegar",
}

def verificar_site(url):
    if not url.startswith("http"):
        url = "https://" + url

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            headers = resp.headers
            status = resp.status
    except urllib.error.HTTPError as e:
        headers = e.headers
        status = e.code
    except Exception as e:
        print(f"Erro ao aceder {url}: {e}")
        return

    print(f"\n{'='*50}")
    print(f"  Site: {url}")
    print(f"  Status: {status}")
    print(f"{'='*50}\n")

    encontrados = 0
    ausentes = []

    for header, descricao in HEADERS_SEGURANCA.items():
        valor = headers.get(header)
        if valor:
            print(f"  [OK] {header}")
            print(f"       Valor: {valor}")
            print(f"       O que é: {descricao}\n")
            encontrados += 1
        else:
            ausentes.append((header, descricao))

    print(f"\n  Total: {encontrados}/{len(HEADERS_SEGURANCA)} cabeçalhos presentes\n")

    if ausentes:
        print("  Ausentes:")
        for header, descricao in ausentes:
            print(f"    - {header} ({descricao})")

    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python check-headers.py <site> [site2 site3 ...]")
        print("Ex:  python check-headers.py tvsucesso.co.mz bim.co.mz")
        sys.exit(1)

    for site in sys.argv[1:]:
        verificar_site(site)
