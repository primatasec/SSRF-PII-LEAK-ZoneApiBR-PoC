Foram identificadas 3 falhas na plataforma Zone API (zone.api.br).

1. Exposição de PII (Information Disclosure): falha na proteção de arquivos de documentação permite acesso público a dados sensíveis de usuários (CPF, Nome, CNS, PIS, score SPC e endereço). Foram encontrados 199 exemplos com dados reais.
2. SSRF Não Autenticado (Server-Side Request Forgery): o endpoint /api/toghibli permite que atacantes alcancem a rede interna (loopback) e mapeiem portas e serviços locais sem precisar de login.
3. Cookie Tossing (Session Fixation): falha na lógica de cookies duplicados (last-wins) combinada com upload de XSS no CDN permite que um atacante forje um cookie e assuma a sessão da vítima no domínio principal (apex).

Impacto
- 1 falha crítica: vazamento massivo de dados pessoais (PII).
- 2 falhas altas: acesso à rede interna (SSRF) e sequestro de sessão (Identity Override).
- Todas as falhas foram testadas e confirmadas no ambiente de produção original.

Conclusão: as falhas demonstram que a infraestrutura expõe dados sensíveis de cidadãos e possui brechas críticas de isolamento de rede e controle de acesso. As três falhas foram corrigidas pelo time da plataforma.

PoC created on 04/10/2026
PATCHED 05/11/2026