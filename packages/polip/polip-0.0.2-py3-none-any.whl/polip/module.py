import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as tr

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import inspect

import torchvision.transforms as transforms

import shutil
import itertools

from PIL import Image
import numpy as np
import sys
import os



#transforms
def get_rgb_transform(resize=(256, 256), mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
    """
    Create a torchvision transforms composition for RGB images.

    Args:
    - resize (tuple): Target size for the Resize transform, as (width, height).
    - mean (list): Mean for each channel for normalization.
    - std (list): Standard deviation for each channel for normalization.

    Returns:
    - A torchvision.transforms.Compose object with the specified transformations.
    """
    return transforms.Compose([
        transforms.Resize(resize),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),
    ])

def get_gray_transform(resize=(256, 256), mean=[0.5], std=[0.5]):
    """
    Create a torchvision transforms composition for grayscale images.

    Args:
    - resize (tuple): Target size for the Resize transform, as (width, height).
    - mean (list): Mean for normalization (single value in a list for grayscale).
    - std (list): Standard deviation for normalization (single value in a list for grayscale).

    Returns:
    - A torchvision.transforms.Compose object with the specified transformations.
    """
    return transforms.Compose([
        transforms.Resize(resize),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),
    ])


#weights init
def weights_init(m):
    """
    Custom weights initializer for the network.

    Args:
    - m (torch.nn.Module): PyTorch layer to initialize.
    """
    if isinstance(m, nn.Conv2d):
        # Initialize Conv2d layers with a normal distribution with mean=0.0 and std=0.02
        nn.init.normal_(m.weight.data, 0.0, 0.02)
    elif isinstance(m, nn.BatchNorm2d):
        # Initialize BatchNorm2d layers' weights with a normal distribution with mean=1.0 and std=0.02
        nn.init.normal_(m.weight.data, 1.0, 0.02)
        # Initialize BatchNorm2d layers' biases to 0
        nn.init.constant_(m.bias.data, 0)


#dataset custom
class CustomImageDataset(Dataset):
    def __init__(self, image_dir, transform=None):
        """
        Args:
            image_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.image_dir = image_dir
        self.transform = transform
        self.image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_name = os.path.join(self.image_dir, self.image_files[idx])
        image = Image.open(img_name).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image
    

#print progress bar

def print_progress_bar(iteration, total, mode=1, epoch=None, total_epochs=None, loss=None, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        mode        - Required  : mode of the progress bar (1 or 2) (Int)
        epoch       - Optional  : current epoch (Int, required for mode 2)
        total_epochs- Optional  : total epochs (Int, required for mode 2)
        loss        - Optional  : current loss (Float, required for mode 2)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    
    if mode == 1:
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    elif mode == 2 and epoch is not None and total_epochs is not None and loss is not None:
        sys.stdout.write(f'\rEpoch {epoch}/{total_epochs} | {prefix} |{bar}| {percent}% | Loss: {loss:.4f} {suffix}')
    sys.stdout.flush()
    
    if iteration == total: 
        print(print_end)










def visualize_model(model, max_layers_per_subplot=10):
    """
    Visualizes the architecture of a PyTorch model by plotting its layers as colored blocks.

    Parameters:
    - model: The PyTorch model to visualize. The model should be an instance of a class derived from torch.nn.Module.
    - max_layers_per_subplot: The maximum number of layers to display in a single subplot. Default is 10.

    The function parses the model's layers, organizes them into a readable format, and then uses matplotlib to draw a diagram with each layer represented as a block. The layers are arranged vertically, with connections indicated by lines between blocks. This visualization helps in understanding the model's structure at a glance.
    """

    def convert_layers_to_architecture(layers_dict):
        architecture = []
        for name, layer in layers_dict.items():
            if name:
                parent_name = name.rsplit('.', 1)[0] if '.' in name else name
                if not any(parent_name in d.get('parent', '') for d in architecture):
                    layer_info = {"layer": str(layer), "parent": parent_name}
                    architecture.append(layer_info)
        return architecture

    layers_dict = {name: module for name, module in model.named_modules() if name}
    architecture = convert_layers_to_architecture(layers_dict)

    # Determine the number of subplots needed
    num_layers = len(architecture)
    num_subplots = (num_layers + max_layers_per_subplot - 1) // max_layers_per_subplot

    def draw_block(ax, center_x, center_y, width, height, text, color='lightgrey'):
        block = patches.Rectangle((center_x - width / 2, center_y - height / 2), width, height,
                                  linewidth=1, edgecolor='black', facecolor=color)
        ax.add_patch(block)
        ax.text(center_x, center_y, text, ha='center', va='center', fontsize=8, wrap=True)
        return center_y - height / 2

    def draw_architecture(ax, architecture_subset):
        layer_width = 0.8
        layer_height = 0.1
        vertical_spacing = 0.1
        current_y = 0

        for i, layer in enumerate(architecture_subset):
            layer_text = layer["layer"]
            if len(layer_text) > 30:
                layer_text = '\n'.join([layer_text[:30], layer_text[30:]])
            color = 'lightblue' if 'block' in layer['parent'].lower() else 'lightgrey'
            bottom_y = draw_block(ax, 0.5, current_y, layer_width, layer_height, layer_text, color=color)

            if i < len(architecture_subset) - 1:
                next_layer_top_y = bottom_y - vertical_spacing + layer_height / 2
                ax.plot([0.5, 0.5], [bottom_y, next_layer_top_y], 'k-')
                current_y = next_layer_top_y - layer_height / 2

        ax.set_xlim(0, 1)
        ax.set_ylim(bottom_y - 0.1, 0.1)
        ax.axis('off')

    fig, axs = plt.subplots(num_subplots, 1, figsize=(6, 8 * num_subplots))

    if num_subplots == 1:
        axs = [axs]  

    for i, ax in enumerate(axs):
        start_idx = i * max_layers_per_subplot
        end_idx = start_idx + max_layers_per_subplot
        architecture_subset = architecture[start_idx:end_idx]
        draw_architecture(ax, architecture_subset)

    plt.show()
    
    
def decider(preferred_device=None, mode = 0):
    """
    Decides which device to use based on availability and preference.

    Args:
    - preferred_device (str, optional): The preferred device to use. Options are 'mps', 'cpu', 'gpu'. 
                                         If not specified, the function will automatically choose the best available device.

    Returns:
    - torch.device: The selected PyTorch device.
    """

    if mode == 1:
        if preferred_device is not None:
            preferred_device = preferred_device.lower()
            if preferred_device == 'mps' and torch.backends.mps.is_available():
                print("Using MPS (Metal Performance Shaders) for acceleration.")
                return torch.device('mps')
            elif preferred_device == 'gpu' and torch.cuda.is_available():
                print("Using GPU for acceleration.")
                return torch.device('cuda')
            elif preferred_device == 'cpu':
                print("Using CPU.")
                return torch.device('cpu')
            else:
                print(f"Preferred device '{preferred_device}' not available. Choosing automatically.")

        if torch.backends.mps.is_available():
            print("Automatically selected MPS (Metal Performance Shaders) for acceleration.")
            return torch.device('mps')
        elif torch.cuda.is_available():
            print("Automatically selected GPU for acceleration.")
            return torch.device('cuda')
        else:
            print("GPU and MPS not available. Using CPU.")
            return torch.device('cpu')
    elif mode == 0:
        if preferred_device is not None:
            preferred_device = preferred_device.lower()
            if preferred_device == 'mps' and torch.backends.mps.is_available():
                return torch.device('mps')
            elif preferred_device == 'gpu' and torch.cuda.is_available():
                return torch.device('cuda')
            elif preferred_device == 'cpu':
                return torch.device('cpu')

        if torch.backends.mps.is_available():
            return torch.device('mps')
        elif torch.cuda.is_available():
            return torch.device('cuda')
        else:
            return torch.device('cpu')        
    

    

def gradient_penalty(critic, real, fake, alpha, train_step, device="cpu"):
    """
    Calculates the gradient penalty for enforcing Lipschitz constraint in WGAN-GP.

    Args:
    - critic (torch.nn.Module): The critic (or discriminator) network.
    - real (torch.Tensor): Real images tensor.
    - fake (torch.Tensor): Fake images tensor generated by the generator.
    - alpha (float): The alpha parameter for mixing real and fake images.
    - train_step (int): Current training step (used if the critic's behavior changes over training).
    - device (str, optional): The device tensors are stored on ("cpu", "cuda", etc.).

    Returns:
    - torch.Tensor: The calculated gradient penalty.
    """
    BATCH_SIZE, C, H, W = real.shape
    beta = torch.rand((BATCH_SIZE, 1, 1, 1), device=device).repeat(1, C, H, W)
    interpolated_images = real * beta + fake.detach() * (1 - beta)
    interpolated_images.requires_grad_(True)

    mixed_scores = critic(interpolated_images, alpha, train_step)

    gradient = torch.autograd.grad(
        inputs=interpolated_images,
        outputs=mixed_scores,
        grad_outputs=torch.ones_like(mixed_scores, device=device),
        create_graph=True,
        retain_graph=True,
    )[0]

    gradient = gradient.view(BATCH_SIZE, -1)
    gradient_norm = gradient.norm(2, dim=1) 
    gradient_penalty = torch.mean((gradient_norm - 1) ** 2)
    return gradient_penalty




    
def count_files_in_folder(folder_path, subfolder=False):
    """
    Counts the number of files in the specified folder.

    Args:
    - folder_path (str): The path to the folder whose files you want to count.
    - subfolder (bool): If True, counts files in subfolders as well. Default is False.

    Returns:
    - int: The number of files in the folder.
    """
    total_files = 0
    
    if subfolder:
        # Iterate over each subfolder
        for root, dirs, files in os.walk(folder_path):
            # Count the files in the current subfolder
            total_files += len(files)
    else:
        # Count the files directly in the folder
        all_entries = os.listdir(folder_path)
        total_files = sum(os.path.isfile(os.path.join(folder_path, entry)) for entry in all_entries)
    
    return total_files





def save_model(model, folder_path, filename='model.pt'):
    """
    Saves a PyTorch model to the specified folder.

    Args:
    - model (torch.nn.Module or tuple): The model or a tuple of models to save.
    - folder_path (str): The folder path where the model will be saved.
    - filename (str, optional): The filename for the saved model. Default is 'model.pt'.
    """
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, filename)

    torch.save(model, file_path)
    
    
def check_model_device(model):
    
    '''
    This function checks the model instance for a type of device
    '''
    return next(model.parameters()).device






# def random_image(np = False, pil = False, tensor = False, resize = True,
#                  static = True):
    
#     random_int = random.randint(0, 10)
#     if static:
#         random_int = 4
#     temp_list = list()
#     for file in os.listdir(path_for_random_images_directory):
#         filepath = os.path.join(path_for_random_images_directory, file)
#         temp_list.append(filepath)
#     random_image_filepath = temp_list[random_int]
    
#     if np:
#         random_image_numpy = cv2.imread(random_image_filepath, cv2.COLOR_BGR2RGB)
#         random_image_numpy = cv2.resize(random_image_numpy, (224, 224))
#         random_image_numpy = np.asarray(random_image_numpy)
#         return random_image_numpy
#     elif pil:
#         random_image_pillow = Image.open(random_image_filepath)
#         random_image_pillow = random_image_pillow.resize((224, 224))
#         random_image_pillow = random_image_pillow.convert("RGB")
#         return random_image_pillow
#     elif tensor:
#         random_image_pillow = Image.open(random_image_filepath)
#         random_image_pillow = random_image_pillow.resize((224, 224))
#         random_image_pillow = random_image_pillow.convert("RGB")
#         random_image_tensor = transforms.Compose([transforms.ToTensor()])(random_image_pillow)
#         return random_image_tensor
#     else:
#         return random_image_filepath
    


    




def save_model_to_onnx(model, input_tensor, filename):
    """
    Save a PyTorch model to the ONNX format.

    Parameters:
    model (torch.nn.Module): The PyTorch model to save.
    input_tensor (torch.Tensor): A sample input tensor to trace the model.
    filename (str): The filename to save the ONNX model to.
    """
    model.eval()
    torch.onnx.export(
        model, 
        input_tensor, 
        filename, 
        export_params=True,
        opset_version=11,
        do_constant_folding=True,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
    )
    print(f"Model saved to {filename}")



def random_tensor(channels=3, b_size=1):
    """
    Generates a random tensor with specified channels and batch size.

    Parameters:
    channels (int): Number of channels in the tensor. Default is 3.
    b_size (int): Batch size. Default is 1.

    Returns:
    torch.Tensor: A tensor of shape (b_size, channels, 32, 32) with random values.
    """
    return torch.randn(b_size, channels, 32, 32)


def printer(variable):
    """
    Prints the name and value of a given variable.

    Parameters:
    variable: The variable to print.

    The function uses the inspect module to find the variable name in the calling context.
    """
    caller_frame = inspect.currentframe().f_back
    line = inspect.getframeinfo(caller_frame).code_context[0].strip()
    variable_name = line[line.find('(') + 1 : line.rfind(')')].strip()
    print(f"{variable_name}: {variable}")



def calculate_parameters(model):
    """
    Calculates the total number of parameters in a given model.

    Parameters:
    model (torch.nn.Module): The model to calculate parameters for.

    Returns:
    int: Total number of parameters in the model.
    """
    return sum(p.numel() for p in model.parameters())


def iterator_pr(dl):
    """
    Iterates through a dataloader and prints the shape of the first batch of inputs and labels.

    Parameters:
    dl (DataLoader): The dataloader to iterate through.

    Prints:
    Shapes of the input and label tensors for the first batch.
    """
    for i, (x, y) in enumerate(dl):
        print("X shape:", x.shape)
        print("Y shape:", y.shape)
        if i == 0: 
            break


def combine_images(folder_name, subfolder1, subfolder2):
    """
    Combines images from two subfolders into a single folder.

    Parameters:
    folder_name (str): The name of the folder to store combined images.
    subfolder1 (str): The path to the first subfolder.
    subfolder2 (str): The path to the second subfolder.

    The function creates the folder if it does not exist and copies all image files from the subfolders.
    """
    os.makedirs(folder_name, exist_ok=True)
    for subfolder in [subfolder1, subfolder2]:
        for file_name in os.listdir(subfolder):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                shutil.copy(os.path.join(subfolder, file_name), folder_name)


def check_ex(file_path):
    """
    Checks if a file exists at the given path and prints a message.

    Parameters:
    file_path (str): The path to the file.

    Prints:
    A message indicating whether the file exists.
    """
    if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")
    else:
        print(f"The file '{file_path}' does not exist.")


def flatten_ll(list_of_lists):
    """
    Flattens a list of lists into a single list.

    Parameters:
    list_of_lists (list of lists): The list of lists to flatten.

    Returns:
    iterator: An iterator that yields items from the flattened list of lists.
    """
    return itertools.chain.from_iterable(list_of_lists)



def generate_random_images(number_of_images, height=100, width=100, output_dir="generated_images"):
    """
    Generate a specified number of random RGB images, save them to a directory, and create the directory if it doesn't exist.

    Parameters:
    number_of_images (int): The number of random images to generate.
    height (int): The height of each image. Default is 100.
    width (int): The width of each image. Default is 100.
    output_dir (str): The directory to save the generated images. Default is 'generated_images'.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i in range(number_of_images):
        random_image = np.random.rand(height, width, 3)
        plt.imshow(random_image)
        plt.axis('off')  

        filename = os.path.join(output_dir, f"random_image_{i+1}.png")
        plt.savefig(filename, bbox_inches='tight', pad_inches=0)
        plt.close()  
        print(f"Generated {filename}")








import inspect

def print_message(message):
    frame = inspect.currentframe().f_back
    line_no = frame.f_lineno
    func_name = frame.f_code.co_name
    file_name = frame.f_code.co_filename
    
    print(f"{message} - [Function: {func_name}, Line: {line_no}]")

def check_p():
    print_message("Triggered")




def iterator_ls(list_, bord = 3):
    for i in range(len(list_)):
        print(f"item{[i]}:",list_[i].shape)
        if i == bord: break

def divider_mainer(text='', length=50):
    if len(text) + 4 > length:
        length = len(text) + 4  

    top_border = "╔" + "═" * (length - 2) + "╗"
    middle_pattern = "║ " + text.center(length - 4) + " ║"
    bottom_border = "╚" + "═" * (length - 2) + "╝"
    
    print(top_border)
    print(middle_pattern)
    print(bottom_border)

def divider_f(length=50):
    start_pattern = '</>'
    end_pattern = '</>'
    middle_pattern = '-'
    
    middle_length = length - len(start_pattern) - len(end_pattern)
    
    middle_section = middle_pattern * middle_length
    
    separator_line = f"{start_pattern}{middle_section}{end_pattern}"
    print(separator_line)




def sender(*tensors):
    """
    Sends multiple tensors to the appropriate device based on availability.

    The function will check for available devices in the following order:
    1. MPS (for Apple Silicon)
    2. CUDA (for NVIDIA GPUs)
    3. CPU (default)

    Parameters:
    *tensors (torch.Tensor): Variable number of tensor arguments.

    Returns:
    list: A list of tensors moved to the determined device.
    """
    def decider():
        if torch.backends.mps.is_available():
            return torch.device('mps')
        elif torch.cuda.is_available():
            return torch.device('cuda')
        else:
            return torch.device('cpu')
    
    device = decider()
    return [tensor.to(device) for tensor in tensors]





def zipper_splitter(file_path, output_dir=None, chunk_size=1024*1024*1024):
    """
    Splits a large file into smaller chunks.
    
    Args:
        file_path (str): Path to the large file to be split.
        output_dir (str): Directory to save the file chunks. Defaults to the same directory as the input file.
        chunk_size (int): Size of each chunk in bytes. Default is 1GB.
    
    Returns:
        List of str: Paths to the created file chunks.
    """
    if output_dir is None:
        output_dir = os.path.dirname(file_path)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    base_name = os.path.basename(file_path)
    base_name_without_ext = os.path.splitext(base_name)[0]
    part = 1
    chunk_paths = []

    with open(file_path, 'rb') as f:
        chunk = f.read(chunk_size)
        while chunk:
            part_name = f"{base_name_without_ext}_part{part}.zip"
            part_path = os.path.join(output_dir, part_name)
            with open(part_path, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(f"Created {part_path}")
            chunk_paths.append(part_path)
            part += 1
            chunk = f.read(chunk_size)
    
    return chunk_paths





def analyze_MM(tensor):
    """
    Analyzes a PyTorch tensor and prints its minimum, maximum, mean, and standard deviation values.
    
    Parameters:
    tensor (torch.Tensor): The input tensor to be analyzed.
    """
    print('Tensor Min Value:', tensor.min())
    print('Tensor Max Value:', tensor.max())
    print('-'*30)
    print('Tensor Mean Value:', tensor.mean())
    print('Tensor std Value:', tensor.std())