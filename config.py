#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6187751987:AAHTFlvQTDNl4HBmByLPazex37SEhweMTQM")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "23560088"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5862418356").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCD3LA2rnK_-W4po-NCP-cZCy22VXAwdToO9uAL0ILznmpFeHGHLRk23aFvaqbI2XDqqImHcLfFV9zj4vj4Mvq1C8lzq4THKSk8RZAXhpMoMn4UmHXt03lHsdIJG0e2PUvKkMCgmmqwNHFn6quon3KOutP2J97Qt5r8IGVYEDAwi9YA5fxgBCsRAG1VMb94yt0-ZQiuzWmUCNAhuswBP1Dj9bPRP37Cdi7B74i1UFyFeqWoTHaGDnGlk0cldcOnZeOBZxrgd2fqu8DsX53_YzmKeYZoAMnUO2G1kW0W50tDxWuQpPvpIEkC4-pLFvA2g7ur5rebux6LofedGCmGxOzaAAAAAV1tZ7QA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
