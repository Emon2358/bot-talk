import asyncio
import discord

async def send_message_to_channel(client, channel_id, message):
    try:
        channel = client.get_channel(channel_id)
        if channel:
            await channel.send(message)
            print("メッセージを送信しました。")
        else:
            print("チャンネルが見つかりません。")
    except discord.errors.NotFound:
        print("無効なチャンネルIDです。")

# メニューを表示する関数
def display_menu():
    print("")
    print("▄███▄   █▀▄▀█ ████▄    ▄   ")
    print("█▀   ▀  █ █ █ █   █     █  ")
    print("██▄▄    █ ▄ █ █   █ ██   █ ▀░▀▀")
    print("█▄   ▄▀ █   █ ▀████ █ █  █ ")
    print("▀███▀      █        █  █ █ ")
    print("          ▀         █   ██ ")
    print("                                     ")
    print("                                      Made by emon2358")

async def main():
    # DiscordのBotトークンを取得
    TOKEN = input("Botのトークンを入力してください: ")

    # クライアントを作成
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    # Botが起動したときに実行されるイベント
    @client.event
    async def on_ready():
        print(f'{client.user} がログインしました')

        # ターミナル上でチャンネルIDとメッセージを入力
        while True:
            channel_id = int(input("チャンネルIDを入力してください: "))
            message = input("送信するメッセージを入力してください: ")

            # メッセージを送信
            await send_message_to_channel(client, channel_id, message)

            # 別のメッセージを送信するか確認
            another_message = input("別のメッセージを送信しますか？ (y/n): ")
            if another_message.lower() != "y":
                break

    # Botを起動
    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
