#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Shrimadhav U K
#
# Copyright 2022 - TeamTele-LeechX
# 
# This is Part of < https://github.com/5MysterySD/Tele-LeechX >
# All Right Reserved

import asyncio
import logging
import os
import time

from shutil import copyfile
from tobrot import LOGGER

async def copy_file(input_file, output_dir): #Ref :https://stackoverflow.com/a/123212/4723940
    output_file = os.path.join(output_dir, str(time.time()) + ".jpg")
    copyfile(input_file, output_file)
    return output_file

async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = os.path.join(output_directory, str(time.time()) + ".jpg")
    VIDEO_SUFFIXES = ("MKV", "MP4", "MOV", "WMV", "3GP", "MPG", "WEBM", "AVI", "FLV", "M4V", "GIF")
    if video_file.upper().endswith(VIDEO_SUFFIXES):
        file_genertor_command = [
            "new-api",
            "-ss",
            str(ttl),
            "-i",
            video_file,
            "-vframes",
            "1",
            out_put_file_name,
        ]
        # Width = "90"
        process = await asyncio.create_subprocess_exec(
            *file_genertor_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    else:
        return None