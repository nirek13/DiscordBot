
import discord
import random
from functions import capitals
import functions
import csv



def capitals():
    # importing csv module


# csv file name
        filename = "country-list.csv"
        capitols = []
        countries = []
# initializing the titles and rows list
        fields = []
        rows = []

# reading csv file
        with open(filename, 'r') as csvfile:
# creating a csv reader object
            csvreader = csv.reader(csvfile)
    
# extracting field names through first row
            fields = next(csvreader)

# extracting each data row one by one
            for row in csvreader:
                rows.append(row)
                capitols.append(row)
                countries.append(row)
# get total number of rows
        num = random.randint(0 , 248)
        country = countries[num]
        return country







TOKEN = "OTY0NjU3NjI1MzAyMTk2MjI1.Yln1bA.BtJmrNK1m1ZH4NCJhC4lzGtvv0I"

client = discord.Client()
Kings = ["Mr Bean#8360"]
def main():
    @client.event
    async def on_message(message):
        id = client.get_guild(903385345956139039)

        if message.content.find(".hello") != -1:
            await message.channel.send("Hello")

        elif message.content.find(".8ball")!= -1:
            responses = ["Yes" , "Reception foggy" , "Never Will it  Happen" , "No" , "Nyet" ,  "OUI" , "Shush child nobody cares" , "Fries Stink"]
            await message.channel.send(f"```{responses[random.randint(0 , len(responses) - 1)]}```")

        elif message.content == ".tc":
            country = capitals()
            await message.channel.send(f"What is the capital of {country[0]}")

            @client.event
            async def on_message(message):
                
                if message.content.lower() == country[1].lower():
                    await message.channel.send("Good job you got it!")
                    main()
                    
                elif message.content.lower() != country[1].lower():
                    await message.channel.send(f"It was {country[1]}")
                    main()


        elif message.content == ".users":
            await message.channel.send(f"Number Of Members: {id.member_count}")

main()
client.run(TOKEN)