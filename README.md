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
```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
Instale as dependências:

```bash
pip install telethon
```

🔧 Configuração
Obtenha seu api_id e api_hash em my.telegram.org.

Edite o arquivo main.py e preencha:

api_id

api_hash

A lista usuarios_para_adicionar com os usernames dos membros

meu_username com seu username do Telegram (sem @)

```python
usuarios_para_adicionar = ['usuario1', 'usuario2']
meu_username = 'seu_username'
```
▶️ Execução
Basta rodar o script com Python:

```bash
python main.py
```

Você será solicitado a digitar o nome do parceiro/cliente. O grupo será criado e os passos executados automaticamente.

🛡️ Observações importantes
O script só consegue adicionar usuários que permitem convites em grupos nas configurações de privacidade do Telegram.

Para usuários com restrição, um link de convite é gerado e enviado no grupo e no seu privado.

Você precisa estar logado com um número de telefone que tenha permissões para criar grupos.

🧑‍💻 Autor
[GitHub](https://github.com/fxlipe124)
[Linkedin](https://www.linkedin.com/in/felipescla/)
