from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest

api_id = input("input the API id here >>> ")
api_hash = input("Paste the API Hash here >>> ")
phone_number = input("input phone number here >>> ")

client = TelegramClient(phone_number, api_id, api_hash)
file = input("input the file to save the names to >>> ")
group = input("input an invite link to a group you want to scrape >>> ")
f = open(file, "r")
list1 = f.readlines()
print(list1)
async def main():

    async for dialog in client.iter_participants(group):
        if str(dialog.username) != "None":
            list1.append(str(dialog.username) + "\n")

with client:
    client.loop.run_until_complete(main())

list1 = list(dict.fromkeys(list1))
f = open(file, "w")
for el in list1:
    f.write(el)
print("Done")


