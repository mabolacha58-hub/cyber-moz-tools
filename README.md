# cyber-moz-tools

Ferramentas e guias de cibersegurança em português para Moçambique.

## Objetivo

Disponibilizar recursos gratuitos para ajudar moçambicanos a protegerem-se online: desde pequenas empresas a utilizadores comuns.

## Guias

| Guia | Descrição |
|------|-----------|
| [passwords-seguras](guias/passwords-seguras.md) | Como criar e gerir passwords fortes |
| [phishing-golpes](guias/phishing-golpes.md) | Como identificar golpes e phishing |
| [wifi-segura](guias/wifi-segura.md) | Configurar redes Wi-Fi de forma segura |
| [contactos-uteis](guias/contactos-uteis.md) | Contactos para reportar crimes digitais em MZ |

## Scripts

```bash
# Verificar cabeçalhos de segurança de sites moçambicanos
python scripts/check-headers.py tvsucesso.co.mz bim.co.mz

# Gerar uma password forte com 20 caracteres
python scripts/gerar-senha.py 20
```

## Como contribuir

1. Faz um fork do repositório
2. Cria um branch para a tua contribuição
3. Abre um Pull Request

## Licença

MIT
