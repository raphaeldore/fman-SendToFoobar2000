import os
import subprocess

from fman import DirectoryPaneCommand, show_alert, show_status_message, load_json, save_json, show_file_open_dialog
from fman.url import as_human_readable
from fman.fs import resolve

DEFAULT_FOOBAR2000_EXECUTABLE_PATH = "C:\\Program Files (x86)\\foobar2000\\foobar2000.exe"
CONFIG_FILE_NAME = "SendToFoobar2000Config.json"

class SendToFoobar2000(DirectoryPaneCommand):
    def __call__(self):
        chosen_files = self.get_chosen_files()

        if chosen_files:
            chosen_files_human_readable = [as_human_readable(resolve(chosen_file)) for chosen_file in chosen_files]

            foobar2000_exe = self._get_foobar2000_exe_path()

            if foobar2000_exe:
                args = [foobar2000_exe, '/add']
                args.extend(chosen_files_human_readable)

                show_status_message("Executed command: {}".format(" ".join(args)), timeout_secs=30) 
                subprocess.call(args)
            else:
                show_alert("There seems to be an issue.")
    
    def _get_foobar2000_exe_path(self):
        config = load_json(CONFIG_FILE_NAME, default={})

        if config and "foobar2000_exe_path" in config:
            return config["foobar2000_exe_path"]
        
        selected_foobar2000_exe_path = show_file_open_dialog("First use configuration: Please locate your foobar2000 executable.", DEFAULT_FOOBAR2000_EXECUTABLE_PATH, "*.exe")

        if selected_foobar2000_exe_path:
            config['foobar2000_exe_path'] = selected_foobar2000_exe_path
            save_json(CONFIG_FILE_NAME, config)

            return selected_foobar2000_exe_path
        
        return None

