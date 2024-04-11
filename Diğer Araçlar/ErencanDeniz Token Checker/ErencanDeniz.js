console.log("ErencanDeniz tarafindan yapildi.");


const fs = require('fs');
const { Client } = require('discord.js-selfbot-v13');

async function checkTokenStatus(token) {
  try {
    const client = new Client({
      checkUpdate: false
    });

    client.once('ready', () => {
      console.log(`${token} | Token Durumu: \x1b[32mCalisiyor\x1b[0m`);
      client.destroy();
    });

    await client.login(token);
  } catch (error) {
    console.log(`${token} | Token Durumu: \x1b[31mCalismiyor\x1b[0m`);
  }
}

async function calistir() {
  try {
    const tokenler = fs.readFileSync('tokenler.txt', 'utf8').split('\n').map(line => line.trim());

    await Promise.all(tokenler.map(token => checkTokenStatus(token)));

    console.log('Tüm tokenler kontrol edildi.');
  } catch (error) {
    console.error(error);
  }
}
console.log("Tokenler:");

// 1 second delay
setTimeout(function(){
    console.log("Executed after 1 second");
}, 999999999);

calistir();

process.on('unhandledRejection', error => {
  console.error(error);
});

process.on('uncaughtException', error => {
  console.error(error);
});

