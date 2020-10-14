import tkinter
import os
from accesstoken import TOKEN

from oanda_chart import ChartManager
from oanda_chart.util.syntax_candy import grid
from oanda_chart import LinkColor
from oanda_candles import Gran, QuoteKind, Pair

root = tkinter.Tk()
manager = ChartManager(TOKEN)
chart = manager.create_chart(root, flags=True, width=700, height=400)

# Setting deault parameters
manager.set_pair(LinkColor.ChartDefault, Pair.EUR_USD)
manager.set_gran(LinkColor.ChartDefault, Gran.M5)
manager.set_quote_kind(LinkColor.ChartDefault, QuoteKind.BID)
chart.grid(row=0, column=0, sticky="nsew")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.attributes('-fullscreen', True)
root.mainloop()