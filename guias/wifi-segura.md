# Guia de Redes Wi-Fi Seguras

Proteger a tua rede Wi-Fi é essencial para evitar que vizinhos ou estranhos usem a tua internet ou acessem os teus dispositivos.

## 1. Altera a senha do router

A maioria dos routers em Moçambique vêm com senhas padrão:
- **Admin:** admin / admin
- **Admin:** admin / 1234
- **Admin:** admin / (em branco)

Muda a senha de acesso ao router (não a senha do Wi-Fi).

### Como fazer

1. Abre o navegador e digita: `192.168.0.1` ou `192.168.1.1`
2. Faz login (ver etiqueta do router)
3. Vai a **System Tools > Password** ou **Administration > Password**
4. Escolhe uma senha forte (vê o guia de passwords seguras)

## 2. Altera o nome da rede (SSID)

Não uses o nome padrão do router (`TMhome`, `Tp-Link_XXXX`, `FibraXXXX`).
Isso ajuda atacantes a saberem o modelo do router.

Escolhe um nome que não te identifique:
- ❌ `Casa do João`, `Rua 1234`
- ✅ `RedeMZ2026`, `LaranjaSecure`

## 3. Usa a encriptação correta

No router, na secção **Wireless Settings > Security**:

| Tipo | Segurança | Recomendado? |
|------|-----------|:---:|
| WEP  | Muito fraca (quebrada em minutos) | ❌ |
| WPA  | Fraca | ❌ |
| WPA2 | Segura | ✅ |
| WPA3 | Muito segura (se o teu router suportar) | ✅✅ |

Senha do Wi-Fi: mínimo 12 caracteres.

## 4. Desativa WPS

WPS permite ligares-te com um PIN de 8 dígitos. É vulnerável.
Desativa em: **Wireless > WPS > Disable**

## 5. Filtro MAC (opcional)

Cada dispositivo tem um endereço único (MAC). Podes configurar o router para aceitar só os dispositivos que conheces: **Wireless > MAC Filter**

Aviso: é trabalhoso quando vierem visitas.

## 6. Mantém o router atualizado

Verifica no site do fabricante se há nova versão do firmware.
Em Moçambique é comum routers da **Tp-Link**, **Tenda**, **Huawei**.
Acede a: **System Tools > Firmware Upgrade**

## Para internet de vizinho

Se usas internet partilhada (vizinho cedeu-te a senha):

1. Não mudes nada no router
2. Usa uma **VPN** para proteger os teus dados do dono da rede
3. O dono da rede consegue ver os sites que visitas (se não usares VPN)

## Próximo guia

Script gerador de passwords.
