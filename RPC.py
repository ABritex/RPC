import pypresence
import time

CLIENT_ID = '' 

RPC = pypresence.Presence(CLIENT_ID)


def start_discord_presence():
    print("Discord Rich Presence is Active")
    RPC.connect()
    start_time = int(time.time())
    try:
        while True:
            elapsed_time = int(time.time()) - start_time
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            uptime_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            RPC.update(
                state='AFK..',
                details='Python Language',
                large_image='https://imgur.com/SoHeP0b.png',
                large_text='Visual Studio Code',
                small_image='https://imgur.com/BYZcRL9.png',
                small_text='Python',
                buttons=[
                    {"label": "Youtube", "url": "https://youtu.be/BBJa32lCaaY?si=kGOw1-4O-hGvJB3L"}
                ],
                
                start=start_time
            )
            time.sleep(15)
    except KeyboardInterrupt:
        stop_discord_presence()


def stop_discord_presence():
    print("Turning off Discord Rich Presence...")
    RPC.close()
    print("Discord Rich Presence is now off.")


start_discord_presence()