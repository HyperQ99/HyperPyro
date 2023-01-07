# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/HyperSupportQ 

import os

from pyrogram import *
from pyrogram.types import *

from config import CMD_HANDLER as cmd
from HyperPyro.helpers.basic import edit_or_reply, get_text, get_user

from .help import *

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "HyperPyro-Bot")


@Client.on_message(filters.command("clone", cmd) & filters.me)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await edit_or_reply(message, "`Menyamar...`")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("`Whom i should clone:(`")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**Sekarang Saya menyamar sebagai** __{f_name}__")


@Client.on_message(filters.command("rclone", cmd) & filters.me)
async def revert(client: Client, message: Message):
    await message.edit("`Mengembalikan penyamaran...`")
    r_bio = BIO

    # Get ur Name back
    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    # Delte first photo to get ur identify
    photos = await client.get_profile_photos("me")
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("`Saya Kembali!`")


add_command_help(
    "clone",
    [
        ["clone", "To Clone someone Profile."],
        ["rclone", "To Get Your Account Back."],
    ],
)
