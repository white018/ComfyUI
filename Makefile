up:
	python3 main.py
pip:
	pip3 install -r requirements.txt
styles:
	python3 convert_styles.py
	cp styles.json custom_nodes/comfyui-easy-use/styles/styles.json
