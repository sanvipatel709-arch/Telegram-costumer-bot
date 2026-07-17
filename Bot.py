import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

QR_IMAGE = "IMG_20260714_203456_755.JPG

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⏱️ 10 Minutes — ₹199", callback_data="time_10")],
        [InlineKeyboardButton("⏱️ 20 Minutes — ₹299", callback_data="time_20")],
        [InlineKeyboardButton("⏱️ 30 Minutes — ₹499", callback_data="time_30")],
    ]

    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "How much time do you need for the service?\n\n"
        "👇 Please select an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data in ["time_10", "time_20", "time_30"]:
        keyboard = [
            [InlineKeyboardButton("✅ OK DONE — I CAN BOOK MY MEETING NOW",
                                  callback_data="book_now")]
        ]

        await query.edit_message_text(
            "📋 PRICE LIST\n\n"
            "⏱️ 10 Minutes — ₹199\n"
            "⏱️ 20 Minutes — ₹299\n"
            "⏱️ 30 Minutes — ₹499\n\n"
            "Please select your preferred package to continue.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "book_now":
        keyboard = [
            [InlineKeyboardButton("💳 GPay", callback_data="payment")],
            [InlineKeyboardButton("💳 PhonePe", callback_data="payment")],
            [InlineKeyboardButton("💳 Paytm", callback_data="payment")],
            [InlineKeyboardButton("🏦 Account Transfer", callback_data="payment")],
        ]

        await query.edit_message_text(
            "💳 BOOKING PAYMENT\n\n"
            "To confirm your booking, please pay the booking amount of ₹199.\n\n"
            "Please choose your payment method:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "payment":
        keyboard = [
            [InlineKeyboardButton("💰 MAKE PAYMENT NOW", callback_data="make_payment")]
        ]

        await query.edit_message_text(
            "💳 Booking Amount: ₹199\n\n"
            "Please click below to make your payment.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "make_payment":
        await query.message.reply_photo(
            photo=open(QR_IMAGE, "rb"),
            caption=(
                "📲 SCAN & PAY\n\n"
                "Please scan the QR code and pay ₹199 booking amount.\n\n"
                "✅ After payment, please send your payment screenshot here."
            )
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()


if name == "main":
    main()
