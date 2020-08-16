from discord import Embed
import hashlib

def make_embed(date, sex, age_group, dhb, overseas_travel, country_source, flight_number, departure_date, arrival_date):
    
    # generate description
    description = "Via Community Transmittion"
    if overseas_travel.lower() == "yes":
        description = "From overseas"
        if country_source:
            description += f" ({country_source})"

    # create embed
    embed = Embed(title=":warning:New Infection:warning:",
                  description=f"{date} " + description, 
                  color=0xFF0000)

    # fields
    if age_group:
        embed.add_field(name=":man_mage: Age", value=age_group, inline=False)

    if dhb:
        embed.add_field(name=":newspaper: Status", value=dhb, inline=False)

    if flight_number:
        embed.add_field(name=":airplane_arriving: Flight Number", value=flight_number, inline=False)

    if departure_date:
        embed.add_field(name=":date: Departure Date", value=departure_date, inline=False)

    if arrival_date:
        embed.add_field(name=":date: Arrival Date", value=arrival_date, inline=False)

    return embed

def case_to_json(case):
    return {
        "date": case[0],
        "sex": case[1],
        "age_group": case[2],
        "dhb": case[3],
        "overseas_travel": case[4],
        "country_source": case[5],
        "flight_number": case[6],
        "departure_date": case[7],
        "arrival_date": case[8]
    }

def hex(json):
    return hashlib.md5(str(json)).hexdigest()  