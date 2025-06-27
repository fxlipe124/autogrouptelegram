# 🤖 AutoTeleg - Criador de Grupos com Tópicos no Telegram via Telethon

Este projeto automatiza a criação de grupos do Telegram com suporte a tópicos (fórum), inclusão de usuários e envio de mensagens automáticas. Ele também gera e envia links de convite caso algum usuário não possa ser adicionado diretamente devido às configurações de privacidade.

## 🚀 Funcionalidades

- Criação automatizada de grupos com nome e descrição personalizados.
- Ativação do modo **fórum** com tópicos organizados:
  - `Chat`
  - `Marketing`
  - `Compliance & Accounting`
- Tentativa de adicionar usuários automaticamente ao grupo.
- Geração de **link de convite** para usuários com restrições de privacidade.
- Envio do link de convite:
  - Dentro do próprio grupo.
  - No privado do administrador.

## 🧠 Tecnologias

- [Python 3.8+](https://www.python.org/)
- [Telethon](https://github.com/LonamiWebs/Telethon)

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/AutoTeleg.git
cd AutoTeleg
