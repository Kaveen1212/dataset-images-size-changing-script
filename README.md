# Image Resizing Script

A Python script for batch resizing images from betel leaf dataset folders. This script processes images from source folders and creates resized versions in corresponding destination folders.

## What This Script Does

This script performs the following operations:

1. **Reads images** from two source folders:
   - `betel_diseased` - Contains images of diseased betel leaves
   - `betel_healthy` - Contains images of healthy betel leaves

2. **Resizes all images** to a uniform size of **512x512 pixels** using high-quality LANCZOS resampling

3. **Saves resized images** to new destination folders:
   - `betel_diseased_resized` - Resized diseased leaf images
   - `betel_healthy_resized` - Resized healthy leaf images

4. **Preserves original files** - The script creates new folders and doesn't modify source images

5. **Provides progress feedback** - Shows real-time progress and completion status for each image

## Prerequisites

### Python Version
- Python 3.6 or higher

### Required Libraries
Install the required library using pip:

```bash
pip install Pillow
```

## Project Structure

```
Datasets/
├── size.py                        # The main script
├── betel_diseased/               # Source folder for diseased images
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
├── betel_healthy/                # Source folder for healthy images
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
├── betel_diseased_resized/       # Created by script - resized diseased images
└── betel_healthy_resized/        # Created by script - resized healthy images
```

## How to Use This Script

### Step 1: Prepare Your Data

1. Create the source folders in the same directory as [size.py](size.py):
   - `betel_diseased`
   - `betel_healthy`

2. Place your images in the respective folders

### Step 2: Run the Script

Navigate to the directory containing the script and run:

```bash
python size.py
```

### Step 3: Check the Output

- The script will create two new folders: `betel_diseased_resized` and `betel_healthy_resized`
- Resized images will be saved in these folders with the same filenames
- Progress will be displayed in the terminal

## Supported Image Formats

The script supports the following image formats:
- `.jpg` / `.JPG`
- `.jpeg` / `.JPEG`
- `.png` / `.PNG`

## Configuration Options

You can modify these variables in the script to customize behavior:

### Change Target Size

Modify line 10 in [size.py](size.py#L10):
```python
target_size = (512, 512)  # Change to your desired dimensions
```

### Change Source/Destination Folders

Modify lines 6-7 in [size.py](size.py#L6):
```python
source_folders = ['betel_diseased', 'betel_healthy']
destination_folders = ['betel_diseased_resized', 'betel_healthy_resized']
```

### Add More Folders

You can add more folder pairs to process:
```python
source_folders = ['folder1', 'folder2', 'folder3']
destination_folders = ['folder1_resized', 'folder2_resized', 'folder3_resized']
```

## Example Output

```
Processing 150 images from 'betel_diseased' to 'betel_diseased_resized'...
  [1/150] Resized: leaf001.jpg
  [2/150] Resized: leaf002.png
  [3/150] Resized: leaf003.jpg
  ...
  [150/150] Resized: leaf150.jpg
✓ Completed 'betel_diseased' - 150 images resized to 250x250

Processing 200 images from 'betel_healthy' to 'betel_healthy_resized'...
  [1/200] Resized: healthy001.jpg
  ...
✓ Completed 'betel_healthy' - 200 images resized to 250x250

✓ All images have been resized and saved to the new folders!
```

## Error Handling

The script includes error handling for:
- **Missing source folders** - Displays a warning if a source folder doesn't exist
- **Image processing errors** - Continues processing other images if one fails
- **Invalid image files** - Skips files that cannot be opened or processed

## Technical Details

- **Resampling Method**: Uses `Image.LANCZOS` for high-quality downsampling
- **Aspect Ratio**: Images are resized to exact dimensions (may distort aspect ratio)
- **Output Format**: Preserves the original image format (JPG, PNG, etc.)
- **Color Mode**: Preserves the original color mode (RGB, RGBA, etc.)

## Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'PIL'"
**Solution**: Install Pillow using `pip install Pillow`

### Issue: "Warning: Source folder not found!"
**Solution**: Ensure the source folders exist in the same directory as the script

### Issue: Images look stretched or distorted
**Solution**: The script resizes to exact dimensions. To maintain aspect ratio, you'll need to modify the script to use thumbnail() instead of resize()

## License

This project is licensed under the Academic Free License 3.0 (AFL-3.0) - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Kaveen C Deshapriya
