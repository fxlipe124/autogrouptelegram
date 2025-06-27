from telethon.sync import TelegramClient
from telethon import functions, types, errors

api_id = <your_id>
api_hash = '<your_hash>'

cliente_nome = input("Digite o nome do cliente: ")
cliente_parceiro = input("Digite o user do cliente: ")

usuarios_para_adicionar = ['user1', 'user2']

meu_username = '<your_user>'

with TelegramClient('minha_sessao', api_id, api_hash) as client:
    result = client(functions.channels.CreateChannelRequest(
        title=f'{parceiro_nome}',
        about=f'Grupo de suporte e comunicação com o cliente {cliente_nome}',
        megagroup=True,
        forum=True
    ))

    group = result.chats[0]
    peer = types.InputPeerChannel(channel_id=group.id, access_hash=group.access_hash)
    print(f"✅ Grupo criado: {group.title} (ID: {group.id})")

    usuarios_com_erro = []

    for username in usuarios_para_adicionar:
        try:
            user_entity = client.get_input_entity(username)
            client(functions.channels.InviteToChannelRequest(
                channel=peer,
                users=[user_entity]
            ))
            print(f"✅ Usuário @{username} adicionado com sucesso.")
        except errors.UserPrivacyRestrictedError:
            print(f"⚠️ @{username} tem restrição de privacidade.")
            usuarios_com_erro.append(username)
        except Exception as e:
            print(f"❌ Erro ao adicionar @{username}: {e}")
            usuarios_com_erro.append(username)

    if usuarios_com_erro:
        try:
            invite = client(functions.messages.ExportChatInviteRequest(peer))
            link = invite.link
            msg = f"⚠️ Não foi possível adicionar automaticamente os seguintes usuários:\n"
            msg += '\n'.join([f"@{u}" for u in usuarios_com_erro])
            msg += f"\n\nUse este link para acessar o grupo:\n{link}"

            client.send_message(peer, msg)
            print("🔗 Link de convite enviado no grupo.")

            meu_entity = client.get_input_entity(meu_username)
            client.send_message(meu_entity, msg)
            print(f"📬 Link também enviado no seu chat privado (@{meu_username}).")

        except Exception as e:
            print(f"❌ Erro ao gerar ou enviar link de convite: {e}")

    client(functions.channels.EditForumTopicRequest(
        channel=peer,
        topic_id=1,
        title='chat'
    ))
    print("Tópico principal renomeado para 'Chat'.")

    client(functions.channels.CreateForumTopicRequest(
        channel=peer,
        title='Mkt, Promo & Anúncios'
    ))
    print("Tópico 'Marketing' criado.")

    client(functions.channels.CreateForumTopicRequest(
        channel=peer,
        title='Compliance & Accounting'
    ))
    print("Tópico 'Compliance & Accounting' criado.")

    print(f"✅ Grupo criado: {group.title} (ID: -100{group.id})")
