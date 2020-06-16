import os

class configs:
    def __init__(self):
        self.current_path = os.path.dirname(os.path.realpath(__file__))

    def dictionary_path(self):
        dic_path =  self.current_path + "\\doc_data\\new_dict.txt"
        return dic_path
    
    def ContentsList_path(self):
        contents_list_path = self.current_path + "\\doc_data\\iGate_Contents_list.docx"
        return contents_list_path
    
    def Json_path(self):
        json_path = self.current_path + "\\result\\iGate Introduction.json"
        return json_path

    def __del__(self):
        pass