import discord
import asyncio
import config
from src import util
from src.stats import Stats


class Client(discord.Client):

    async def on_ready(self):
        print(f'[DISCORD]: Logged on as {self.user}')

        # init checker
        self.loop.create_task(self.updater())

        # display status 
        activity = discord.Activity(name='COVID-19 Stats', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)

    async def updater(self):
        stats = Stats()
        channel = client.get_channel(config.channel)

        while True:
            await client.wait_until_ready()

            # new case reports
            cases = stats.new_cases()
            for case in cases:
                print("[ALERT] New case!")
                embed = util.make_embed(
                    case['date'],
                    case['sex'],
                    case['age_group'],
                    case['dhb'],
                    case['overseas_travel'],
                    case['country_source'],
                    case['flight_number'],
                    case['departure_date'],
                    case['arrival_date']
                )
                await channel.send(embed=embed)

            # TODO: end of day summary
            # ...

            await asyncio.sleep(10)

if __name__ == '__main__':
    print("[BOT] Stay safe New Zealand")
    client = Client()
    client.run(config.token)