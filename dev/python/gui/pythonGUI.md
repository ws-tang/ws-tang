# Python Dev Notes for GUI

My notes for Python Graphic User Interface (GUI) is listed herein.

<br/>

## Development Setup

Refer to [Python Dev Notes](../pythonREADME.md#develoment_setup) for information about general setup.

The option for Python GUI noted here in uses **Tk**. Here are some of its features:

- it’s free and open (we don’t need to pay for anything)
- it has been developed since 1991 (which means it’s stable and mature)
- it defines and serves more than thirty different universal widgets (which is enough even for quite complex applications)
- its implementation is available for many programming languages (of course, for Python too)

The module that brings Tk to the Python world is named **TkInter**, which is short for Tk Interface. It’s free and open, too.

The very first Python IDE **IDLE**, is written using TkInter.

Source: Sec. 1.1.1.10. _Introduction to GUI Programming in Python (TkInter)_ . [OpenEDG](https://edube.org/study/pcpp1-3)

<br/>

## Tutorials and Resources

Tcl/Tk is the option for GUI noted here.

- [Graphical User Interfaces with Tk](https://docs.python.org/3/library/tk.html)
- [tkinter — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
- [tkinter.ttk — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
- [Python Tkinter Tutorial](https://www.geeksforgeeks.org/python-tkinter-tutorial/) by Geeks for Geeks
- [Introduction to GUI Programming in Python: TkInter](https://edube.org/study/pcpp1-3) by [OpenEDG](https://openedg.org/)

<br/>

## Practices and Exercises

### Start with Python TkInter

```
import tkinter

... ...    # Do some coding here

window = tkinter.Tk()

... ...    # Do some coding here

window.mainloop()
```
