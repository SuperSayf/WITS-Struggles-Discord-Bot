import discord
from discord.ext import commands
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'cogs/drive/keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '***REMOVED***'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

sheetnames = ["Calculus", "Algebra", "Modelling", "Mechanics", "IDSA", "DCS", "INFO", "PHSC"]


class drive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def drive(self, ctx, course, link, *args):
        if course in sheetnames:
            information = " ".join(args[:])
            if not information:
                await ctx.send(f"{ctx.author.mention} No information added!")
                return
            if not link:
                await ctx.send(f"{ctx.author.mention} No link added!")
                return
            date = datetime.today().strftime('%d/%m/%Y')
            name = ctx.author.name
            data = [[information, date, link, name]]
            RANGE_NAME = course + "!A1:D1"
            res = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values":data}).execute()
            await ctx.send(f"{ctx.author.mention} Added!")
        else:
            await ctx.send(f"{ctx.author.mention} Wrong course name! - Please choose from: Calculus, Algebra, Modelling, Mechanics, IDSA, DCS, INFO, PHSC")


def setup(bot):
    bot.add_cog(drive(bot))
