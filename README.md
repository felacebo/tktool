1、原始包来源：https://github.com/skywind3000/PyStand
2、补充tkinter包，来源：https://stackoverflow.com/questions/37710205/python-embeddable-zip-install-tkinter
Assuming you are on Windows and you also have a regular Python distribution installed (same version of the embedded distribution), to install Tkinter in the embedded distribution you can copy the following files from the regular Python distribution:
  tcl folder to embedded_distribution_folder\ (root folder of the embedded distribution)
  tkinter folder (which is under Lib) either to embedded_distribution_folder\Lib or to embedded_distribution_folder\
  files _tkinter.pyd tcl86t.dll tk86t.dll zlib1.dll (which are under DLLs, zlib1.dll for python >= 3.12) either to embedded_distribution_folder\DLLs or to embedded_distribution_folder\
