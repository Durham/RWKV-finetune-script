This repository contains my code and quick instruction of how to fine-tune large
RWKV (https://github.com/BlinkDL/RWKV-LM) models on your data, particularly on
Alpaca and it's derivatives.

This is quick and dirty solution, not very optimal in many aspects.

# Instruction
## Prepare your data
I train with a single text file as input. Script convert.py can load JSON file with alpaca-style data and saves *.txt. You can use it, or prepare txt file in other way. The script will make file in following format:
```
user: What are the most important values in life
bot: The most important values in life are kindness
<|endoftext|>
user: Write an 1850-word horror story.
...
```
User input is generated by appending instruction and input (in random order, since I think that in real settings users sometimes can provide input before instruction), and adds some other minor variations.
To use script, edit this
```
input_file = 'alpaca_data_cleaned.json'
output_txt_file = "alpaca_data_cleaned_for_training.txt"
```
at the beginning of the script
## Install RWKV and dependecies
I assume that you have suitable computer with GPU and cuda drivers 11.7 installed. This readme does not cover CUDA driver installation.
Clone this repository https://github.com/Blealtan/RWKV-LM-LoRA It is good for both LoRa and full fine-tuning
Install pytorch 1.13.1+cu117 (see here https://pytorch.org/get-started/previous-versions/ for details, I use command belowm but you may want to use different command depending on your OS etc)
```
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```
Install pytorch-lightning (use 1.9.x version, not 2.0! 2.0 does not work), and DeepSpeed=0.7.0 and other accelerate. I install these using pip.
Replace RWKV-LM-LoRA/RWKV-v4neo/src/dataset.py with dataset.py in this repo. I made changes so text file can be directly loaded and pre-tokenized. This is not the best (or a very good) way to do this, but it does the job for small datasets well enough.




