import os

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
os.system('huggingface-cli download --resume-download hpcai-tech/Open-Sora --local-dir /home/dist/hpcai/duanjunwen/Open-Sora/pretrained_models/stdit/OpenSora --local-dir-use-symlinks False')
