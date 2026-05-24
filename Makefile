PY = ../python_embeded/python.exe

up:
	$(PY) main.py --enable-manager > log.txt 2>&1
pip:
	$(PY) -m pip install -r requirements.txt
styles:
	$(PY) convert_styles.py
	cp styles.json custom_nodes/comfyui-easy-use/styles/styles.json
