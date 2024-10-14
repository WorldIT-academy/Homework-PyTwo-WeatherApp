import json
#
import os
#
def write_json(name_file: str, value_file: str):
    #
    path_static = os.path.abspath(__file__ + f'../../../../static/{name_file}')
    #
    with open(file= path_static, mode= "w") as file:
        #
        json.dump(
            obj= value_file, #
            fp= file, #
            indent= 4, #
            ensure_ascii= False #
        )