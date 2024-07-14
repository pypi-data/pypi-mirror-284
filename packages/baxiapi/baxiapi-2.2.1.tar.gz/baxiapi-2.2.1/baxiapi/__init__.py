import requests
import wavelink
import discord
from discord.ext import commands
from typing import cast
from reds_simple_logger import Logger

logger = Logger()

class Baxi_API:
    def __init__(self, api_key):
        self.api_key = api_key

    def create_welcome_banner(self, background_url, text1, text2, profile_pic_url):
        url = 'http://api.pyropixle.com/v1/create-banner'
        data = {
            "background_url": background_url,
            "text1": text1,
            "text2": text2,
            "profile_pic_url": profile_pic_url,
            "api_key": self.api_key
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return str(response.json()["image_url"])
        else:
            return str(response.json()["error"])
        
    def get_chatfilter_event(self, request_id):
        url = 'http://api.pyropixle.com/v1/chatfilter_event_data'
        data = {
            "request_id": request_id,
            "api_key": self.api_key
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return str(response.json())
        else:
            return str(response.json()["error"])
        
class Music:
    def __init__(self, api_key: str, bot, log: bool):
        self.api_key = api_key
        self.client = bot
        self.log = log
        self.wavelink_server = "http://sparkle3.pyropixle.com:1670"
        self.players = {}
        logger.info("MUSIC RETURN INFORMATION:\nUse music.response for API resonse.")

    class Music_response:
        def __init__(self, message: str, song_name: str, artwork: str, artist: str, error: bool):
            self.response = message
            self.song_name = song_name
            self.artwork = artwork
            self.artist = artist
            self.error = error

    async def connect_to_server(self):
        try:
            if self.log:
                logger.waiting("MUSIC: Connecting to external server...")
            await wavelink.Pool.connect(nodes=[wavelink.Node(uri=self.wavelink_server, password="PyroPixleAdmin", client=self.client, retries=5, identifier="Main")], client=self.client)
            if self.log:
                logger.success("MUSIC: Connected to Server!")
        except Exception as e:
            logger.error("ERROR MUSIC CONNECT: " + str(e))
        

    async def play(self, search:str, autoplay: bool, interaction: discord.Interaction, volume: int = 30):
        try:
            if self.log:
                logger.waiting("MUSIC: Checking API_key...")
                check_api = requests.get("https://baxi.pyropixle.com/api/check_api_key",
                            params={"key": str(self.api_key)})
            if check_api.status_code != 200:
                logger.error("ERROR PLAYING MUSIC: " + check_api.json()["error"])
                return self.Music_response("ERROR PLAYING MUSIC: " + check_api.json()["error"], song_name=None, artist=None, artwork=None, error=True)
            
            if self.log:
                logger.success("MUSIC: API_key valid!")

            player: wavelink.Player = self.players.get(interaction.guild.id)
    
            
            if not player:
                try:
                    player = await interaction.user.voice.channel.connect(cls=wavelink.Player)
                    self.players[interaction.guild.id] = player
                except AttributeError:
                    logger.warn("MUSIC ERROR: User not connected to voice channel!")
                    return self.Music_response("User not connected to voice channel!", song_name=None, artist=None, artwork=None, error=True)
                except discord.ClientException:
                    logger.warn("MUSIC ERROR: UNKNOWN")
                    return self.Music_response("Unknown Error", song_name=None, artist=None, artwork=None, error=True)
                
            if autoplay:
                player.autoplay = wavelink.AutoPlayMode.enabled
            else:
                player.autoplay = wavelink.AutoPlayMode.disabled

            tracks: wavelink.Search = await wavelink.Playable.search(search, source=wavelink.TrackSource.SoundCloud)
            if not tracks:
                return self.Music_response("MUSIC ERROR: Song not found!", song_name=None, artist=None, artwork=None, error=True)
            
            if isinstance(tracks, wavelink.Playlist):
                added: int = await player.queue.put_wait(tracks)
                track_name = tracks.name
                artist = tracks.author
                artwork = tracks.artwork
            
            else:
                track: wavelink.Playable = tracks[0]
                track_name = track
                artist = track.artist
                artwork = track.artwork
                await player.queue.put_wait(track)
            
            if self.log:
                logger.info("Request prossesed!")
            
            if not player.playing:
                await player.play(player.queue.get(), volume=volume)

            return self.Music_response("MUSIC: Song added to queue!", song_name=track_name, artist=artist, artwork=artwork, error=False)
        except Exception as e:
            return self.Music_response(f"MUSIC ERROR: {str(e)}", song_name=None, artist=None, artwork=None, error=True)
        
    async def stop(self, interaction: discord.Interaction):
        try:
            if self.log:
                logger.waiting("MUSIC: Checking API_key...")
            check_api = requests.get("https://baxi.pyropixle.com/api/check_api_key",
                                    params={"key": str(self.api_key)})
            if check_api.status_code != 200:
                logger.error("ERROR PLAYING MUSIC: " + check_api.json()["error"])
                return self.Music_response("ERROR PLAYING MUSIC: " + check_api.json()["error"], song_name=None, artist=None, artwork=None, error=True)
            
            player: wavelink.Player = self.players.get(interaction.guild.id)
            if player:
                await player.disconnect()
                del self.players[interaction.guild.id]
            else:
                logger.success("MUSIC ERROR: Bot not connected to channel!")
                return self.Music_response(f"MUSIC ERROR: Bot not connected to channel", song_name=None, artist=None, artwork=None, error=True)

            if self.log:
                logger.success("MUSIC: Request prossesed successfully!")
            return self.Music_response(f"MUSIC: Success", song_name=None, artist=None, artwork=None, error=False)
        
        except Exception as e:
            logger.error("MUSIC ERROR: UNKNOWN")
            return self.Music_response(f"MUSIC ERROR: {str(e)}", song_name=None, artist=None, artwork=None, error=True)
        
    async def skip(self, interaction: discord.Interaction):
        try:
            if self.log:
                logger.waiting("MUSIC: Checking API_key...")
                check_api = requests.get("https://baxi.pyropixle.com/api/check_api_key",
                            params={"key": str(self.api_key)})
            if check_api.status_code != 200:
                logger.error("ERROR PLAYING MUSIC: " + check_api.json()["error"])
                return self.Music_response("ERROR PLAYING MUSIC: " + check_api.json()["error"], song_name=None, artist=None, artwork=None, error=True)
            
            player: wavelink.Player = self.players.get(interaction.guild.id)
            if not player:
                return

            await player.skip(force=True)
            if self.log:
                logger.success("MUSIC: Song skipped")

            return self.Music_response(f"MUSIC: Song skipped", song_name=None, artist=None, artwork=None, error=False)

        except Exception as e:
            logger.error("MUSIC ERROR: UNKNOWN")
            return self.Music_response(f"MUSIC ERROR: {str(e)}", song_name=None, artist=None, artwork=None, error=True)

        
