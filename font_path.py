# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:54:59 2024

@author: pjc62
"""

def fontpath():
    
    import os

    user_name = os.getlogin()

    return [f'C:/Users/{user_name}/AppData/Local/Microsoft/Windows/Fonts']

# %%
def reg():
    import matplotlib.font_manager as fm

    path = fontpath()
    font_files = fm.findSystemFonts(fontpaths=path)
    for fpath in font_files:
        
        fm.fontManager.addfont(fpath)
        
# %%

if __main__ == '__name__':
    
    pass