import pyrogram

# Replace the values below with your own API ID, API Hash and session name
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
session_name = 'my_session'
session_string = 'YOUR_PYROGRAM_SESSION'
# Replace the value below with the chat ID of the chat you want to fetch the last message from
chat_id = '777000'

# Replace the value below with the bot token of your Telegram bot
bot_token = 'YOUR_BOT_TOKEN'

# Create a new Pyrogram client and attach it to the bot account
bot_client = pyrogram.Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Create a new Pyrogram client and attach it to the user account
user_client = pyrogram.Client(session_name, api_id=api_id, api_hash=api_hash, session_string=session_string)

# Define the event handler for incoming messages in the user account
@user_client.on_message()
def handle_incoming_message(client, message):
    # Ignore all incoming messages, since we only want to fetch the last two message in a specific chat
    pass

# Start the user account client
user_client.start()

# Fetch the last message in the specified chat using the user account client
last_message = user_client.get_history(chat_id, limit=2)[0]

# Start the bot account client
bot_client.start()

# Send the text of the last message as a reply from the bot
bot_client.send_message(chat_id, last_message.text, reply_to_message_id=last_message.message_id)

# Stop the bot account client
bot_client.stop()

# Stop the user account client
user_client.stop()
