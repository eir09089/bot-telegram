const token = require('./config');
const TeleBot = require('telebot');
const bot = new TeleBot(token);
bot.on('*', (msg) => {
 msg.reply.text(msg.text)
});

bot.start();
