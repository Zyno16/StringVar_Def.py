
from tools import *


frm = form()
label(frm,"name").pack(pady=5)
txt=EntryOnlyNumber(frm,False)
txt.pack(pady=5)
IV = IntVar()
txt.config(textvariable=IV)
def test():
    print(IV.get())
button(frm,"ok",test).pack(pady=5)   
frm.mainloop()
