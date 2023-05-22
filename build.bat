rm *.spec
rm ./dist/*.exe

pyinstaller --onefile -w --icon=panel_admin\images\iconoAzul.ico '.\first run.py'
pyinstaller --onefile -w --icon=panel_admin\images\icono.ico .\intAdm.pyw   
pyinstaller --onefile -w --icon=panel_admin\images\iconoAzul.ico .\lector_cajones.py 
pyinstaller --onefile -w --icon=panel_admin\images\iconoAzul.ico .\lector_salida.py  
pyinstaller --onefile -w --icon=panel_admin\images\icono.ico .\main.py           