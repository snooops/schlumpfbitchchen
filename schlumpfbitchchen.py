import discord
import subprocess
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


    def checkhub(result):
        if result == 0:
            output="Der Hub ist bereit eure Verbindung zu empfangen :heart_eyes:"
        elif result == 3:
            output="Oh nein, der Hub ist erschlafft :sob:"
        else:
            output="Ich kann den Hub nicht länger fühlen, irgendwas stimmt nicht :flushed:"
        return output



    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!sexy'):
            await message.channel.send('Oh danke, mein Süßer :kissing_heart:')

        if message.content.startswith('!ut4hubstatus'):
            output = checkhub( os.system("/bin/systemctl status isp-ut4"))
            await message.channel.send(output)

        if message.content.startswith('!ut4fullstatus'):
            output ="```" + str(subprocess.check_output("SYSTEMD_COLORS=0 systemctl status isp-ut4.service", shell=True)).replace('\\n', '\n').replace('\\t', '\t') + "```"
            await message.channel.send(output)

        if message.content.startswith('!ut4hubrestart'):
            await message.channel.send("Uuuh jaaa ich kann es kaum erwarten, ich starte den Hub neu... :star_struck:")
            output = checkhub( os.system("sudo /bin/systemctl restart isp-ut4"))
            await message.channel.send(output)

        if message.content.startswith('!ut4hubconfigdeploy'):
            await message.channel.send("oh oh OH OH ! OOOOOOOH! Ich SAUGE DIE CONFIG VON GITHUB JAAAA :dizzy_face: :face_vomiting: :relaxed:")
            os.system("cd ~/Config && git pull")





with open('apikey', 'r') as myfile:
        apikey=myfile.read().replace('\n', '')
client.run(apikey)
