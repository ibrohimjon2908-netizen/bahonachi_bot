import random, os
from telegram import InlineKeyboardButton as B, InlineKeyboardMarkup as M, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOSHLANISH = ["Kechirasiz,", "Aytishga uyalaman, lekin", "Ishoning,", "Bilasizmi,"]

BAHONA = {
 "ish": [
  "telefonim o'chib qolgan edi, hozir zaryad topdim",
  "yo'lda tirbandlik bo'ldi, mashinalar qimirlamay qoldi",
  "buyurtma manzili noto'g'ri chiqdi, uzoq qidirdim",
 ],
 "dostlar": [
  "onam birdan sizga yordam so'rab qoldi",
  "velosipedim shinasi teshilib qoldi",
  "uxlab qolibman, budilnik ishlamabdi",
 ],
 "uy": [
  "internet o'chib qoldi, xabarni ko'rmabman",
  "kalitni ichkarida qoldirib, eshik yopilib qoldi",
  "qo'shnimning mushugi uyimga kirib qoldi, uni chiqarib yubordim",
 ],
}
OXIRI = ["Keyingi safar bunday bo'lmaydi.", "Uzr, tushunganingiz uchun rahmat.", "Hozir yo'ldaman!", ""]

def tugmalar():
    return M([[B("Ish", callback_data="ish"), B("Do'stlar", callback_data="dostlar"), B("Uy", callback_data="uy")]])

async def start(u: Update, c: ContextTypes.DEFAULT_TYPE):
    await u.message.reply_text("Kimga bahona kerak?", reply_markup=tugmalar())

async def bosildi(u: Update, c: ContextTypes.DEFAULT_TYPE):
    q = u.callback_query
    await q.answer()
    t = f"{random.choice(BOSHLANISH)} {random.choice(BAHONA[q.data])}. {random.choice(OXIRI)}"
    await q.message.reply_text(t.strip(), reply_markup=tugmalar())

app = Application.builder().token(os.environ["TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(bosildi))
app.run_polling()
