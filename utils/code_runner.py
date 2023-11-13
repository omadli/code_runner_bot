import html
import hashlib
import logging
import piston_rspy
from aiogram import Router, types, F, enums

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
                if response.compile and len(response.compile.output):
                    if len(response.compile.output) < 3000:
                        await msg.reply("Compilation:" + f"\n<code>{html.escape(response.compile.output)}</code>")
                    else:
                        await msg.reply("Compilation:" + f"\n<code>{html.escape(response.compile.output[:3000])}</code> ......")
                        
                error = response.run.stderr
                if error:
                    if len(error) < 3000:
                        await msg.reply("Xatolik:" + f"\n<code>{html.escape(error)}</code>")
                    else:
                        await msg.reply("Xatolik:" + f"\n<code>{html.escape(error[:1000])} ....</code>")
                else:
                    await msg.reply("Natija:" + f"\n<code>{html.escape(response.run.output)}</code>")

   
    async def inline_handler(query: types.InlineQuery):
        text = query.query
        client = piston_rspy.Client()
        if text.startswith(f"{command}"):
            text = text.replace(f"{command}", "", 1)
        stdin = ""
        code = text.strip()
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
            await query.answer(
                results=[],
                cache_time=0,
                button=types.InlineQueryResultsButton(
                    text="FAILED TO LOAD RESPONSE",
                    start_parameter="help"
                )
            )
        else:
            output = response.run.output
            if len(output) > 2000:
                await query.answer(
                    results=[],
                    cache_time=0,
                    button=types.InlineQueryResultsButton(
                        text="Natija hajmi juda katta, ruxsat etilgan hajm - 2000 ta belgi",
                        start_parameter="help"
                    )
                )
            else:
                if response.compile and len(response.compile.output):
                    pass
                    # await msg.reply("Compilation:" + f"\n<code>{html.escape(response.compile.output)}</code>")
                error = response.run.stderr
                if error:
                    await query.answer(
                        results=[],
                        cache_time=0,
                        button=types.InlineQueryResultsButton(
                            text="Kodingizda xatolik borga o'xshaydi🤔",
                            start_parameter="help"
                        ),
                    )
                    
                else:
                    msg_result = [
                        f"<b>Language:</b> {command}",
                        "<b>Code:</b>",
                        f"<pre><code class='language-{command}'>{code}</code></pre>\n",
                        "<b>Result: </b>",
                        f"<code>{html.escape(response.run.output)}</code>"
                    ]
                    if len(stdin):
                        msg_result = msg_result[:3] + [
                            "<b>stdin:</b>",
                            f"<code>{stdin}</code>\n"
                        ] + msg_result[3:]
                    
                    await query.answer(
                        results=[
                            types.InlineQueryResultArticle(
                                type='article',
                                id=hashlib.md5(text.encode("UTF8")).hexdigest(),
                                title="Natija",
                                input_message_content=types.InputTextMessageContent(
                                    message_text="\n".join(msg_result),
                                    parse_mode=enums.parse_mode.ParseMode.HTML
                                ),
                                description=response.run.output
                            )    
                        ],
                    )
    
    async def empty_inline_handler(query: types.InlineQuery):
        await query.answer(
            results=[],
            button=types.InlineQueryResultsButton(
                text="Yordam uchun bu yerga bosing",
                start_parameter="help"
            )
        )
        return            
        
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
    
    router.inline_query.register(inline_handler, F.query.startswith(f"{command}"))
    router.inline_query.register(empty_inline_handler, F.query == "")
    
    # for help, if the user only sends "/command", the bot will send the example code to him
    router.message.register(empty_cmd, F.text == f"/{command}")
