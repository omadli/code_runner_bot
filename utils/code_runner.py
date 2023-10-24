import html
import logging
import piston_rspy
from aiogram import Router, types, F


def run_in_message(language: dict, router: Router):
    command = language["command"]
    
    async def cmd_runner(msg: types.Message):
        client = piston_rspy.Client()
        text = msg.text
        if text.startswith(f"/{command}\n"):
            text = text.replace(f"/{command}\n", "", 1)
        stdin = ""
        code = text
        if "/stdin\n" in  text:
            code, stdin = code.split("/stdin\n", maxsplit=1)
        
        response = await client.execute(
            piston_rspy.Executor()
            .set_language(language["name"])
            .set_version(language["version"])
            .add_file(
                piston_rspy.File(
                    name=language['file_name'],
                    content=code,
                )
            ).set_stdin(stdin)
        )
        
        if response.is_err():
            logging.debug(f"FAILED TO LOAD RESPONSE: {response}")
            await msg.reply("FAILED TO LOAD RESPONSE")
        else:
            output = response.run.output
            if len(output) > 2000:
                await msg.reply("Natija hajmi juda katta, ruxsat etilgan hajm - 2000 ta belgi")
            else:
                if len(response.compile.output):
                    await msg.reply("Compilation:" + f"\n<code>{html.escape(response.compile.output)}</code>")
                error = response.run.stderr
                if error:
                    await msg.reply("Xatolik:" + f"\n<code>{html.escape(error)}</code>")
                else:
                    await msg.reply("Natija:" + f"\n<code>{html.escape(response.run.output)}</code>")
    
    # sending example code
    async def empty_cmd(msg: types.Message):
        m = await msg.bot.send_message(
            chat_id=msg.from_user.id,
            text=f"/{command}\n<pre><code class='language-{language['command']}'>{html.escape(language['example'])}</code></pre>"
        )
        await m.reply(
            text=f"Menga {language['name']} kodlaringiz manashu namunadagidek yuboring."
        )
    
    # for codes
    router.message.register(cmd_runner, F.text.startswith(f"/{command}\n"))
    
    # for edited messages
    router.edited_message.register(cmd_runner, F.text.startswith(f"/{command}\n"))
    
    # for help, if the user only sends "/command", the bot will send the example code to him
    router.message.register(empty_cmd, F.text == f"/{command}")
