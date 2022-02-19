# Cat-Userbot
# Thanks Sandy
# Recode by Fariz <Flicks-Userbot>
# Don't Remove Credits ⚠️

import io
import sys
import traceback

from userbot import CMD_HELP, bot
from userbot.events import register edit_or_reply


@register(outgoing=True, pattern=r"^\.calc")
async def calculator(event):
    "Untuk menyelesaikan persamaan matematika dasar."
    cmd = event.text.split(" ", maxsplit=1)[1]
    event = await edit_or_reply(event, "Calculating ...")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Maaf saya tidak dapat menemukan hasil untuk persamaan yang diberikan"
    final_output = "**PERSAMAAN**: `{}` \n\n **SOLUSI**: \n`{}` \n".format(
        cmd, evaluation
    )
    await event.edit(final_output)


async def aexec(code, event):
    exec("async def __aexec(event): " +
         "".join(f"\n {l}" for l in code.split("\n")))

    return await locals()["__aexec"](event)


CMD_HELP.update({"calkulator": f".calc\n"
                 f"usage : Menyelesaikan permasalahan matematika dasar.\n"
                 "Memecahkan persamaan matematika yang diberikan dengan aturan BODMAS.\n"
                 f"contoh : `.calc 2+9`, `.calc 2*2`, `.calc 7-2`, `.calc 9/3`"})
