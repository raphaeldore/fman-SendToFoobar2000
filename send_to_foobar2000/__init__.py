import os
import subprocess

from fman import DirectoryPaneCommand, show_alert, show_status_message
from fman.url import as_human_readable
from fman.fs import resolve

DEFAULT_FOOBAR2000_EXECUTABLE_PATH = "C:\\Program Files (x86)\\foobar2000\\foobar2000.exe"

class SendToFoobar2000(DirectoryPaneCommand):
    def __call__(self):
        chosen_files = self.get_chosen_files()

        if chosen_files:
            chosen_files_human_readable = [as_human_readable(resolve(chosen_file)) for chosen_file in chosen_files]

            args = [DEFAULT_FOOBAR2000_EXECUTABLE_PATH, '/add']
            args.extend(chosen_files_human_readable)

            show_status_message("Executed command: {}".format(" ".join(args)), timeout_secs=30) 
            subprocess.call(args)
