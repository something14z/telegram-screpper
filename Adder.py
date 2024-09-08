from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerChannel, InputUser
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetParticipantsRequest

api_id = 20818234
api_hash = '59562963353626f164e921c308b287cb'
phone = '+17758422809'
# client = TelegramClient(phone, api_id, api_hash);
# client.connect()
# ----------------------------------------------



# async def main():
#     my_chan = await client.get_entity('https://t.me/testchanellty')
#     channel_id = my_chan.id;
#     channel_access_hash = my_chan.access_hash
#     chanal=InputPeerChannel(channel_id, channel_access_hash)
#
#
#     result = client(ResolveUsernameRequest(username='ViktorProgerov'))
#     print(result.stringify())
#
#
#     # user =  client(ResolveUsernameRequest('ViktorProgerov'))
#     # user=  InputUser(user.users[0].id, user.users[0].access_hash,)
#     # client(InviteToChannelRequest(chanal, [user]))
#     print('action completted')
#
#
#     # async for dialog in client.iter_participants(group):
#     #     pass
#
#
# with client:
#     client.loop.run_until_complete(main())






with TelegramClient(phone, api_id, api_hash) as client:
        my_chan =  client.get_entity('https://t.me/testchanellty')
        channel_id = my_chan.id;
        channel_access_hash = my_chan.access_hash
        chanal=InputPeerChannel(channel_id, channel_access_hash)
        user = client(ResolveUsernameRequest(username='ViktorProgerov'))
        user = InputUser(user.users[0].id, user.users[0].access_hash,)
        client(InviteToChannelRequest(chanal, [user]))
        print('action completted')

