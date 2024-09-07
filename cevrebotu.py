
import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$petşişeler'):
        await message.channel.send("Pet şişeler, genellikle polietilen tereftalat (PET) adı verilen bir plastik türünden yapılır. PET, hafif, dayanıklı ve şeffaf bir malzemedir ve sıvıların saklanması için yaygın olarak kullanılır. Ancak, çevresel etkileri konusunda bazı endişeler bulunmaktadır:")
    elif message.content.startswith('$kağıt atıklar'):
        await message.channel.send("Kağıt atıklar, çeşitli kaynaklardan elde edilen kağıt ürünlerinin atılması sonucu oluşur")
    elif message.content.startswith('$piller'):
        await message.channel.send("Piller, kimyasal enerjiyi elektrik enerjisine dönüştüren cihazlardır ve çeşitli malzemelerden yapılır")
    else:
        await message.channel.send(message.content)

client.run("")
