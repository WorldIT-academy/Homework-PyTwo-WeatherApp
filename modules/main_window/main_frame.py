import customtkinter
from ..wr_json import read_json
import json

main_window = customtkinter.CTk(fg_color="#5DA7B1")
#
main_config = read_json(name_file= "config.json")
# print(json.dumps(main_config, indent= 4))
#
WIDTH = main_config["main_frame"]["width"]
HEIGHT = main_config["main_frame"]["height"]
# 
main_window.geometry(f"{WIDTH}x{HEIGHT}")