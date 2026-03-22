import os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

folder = "public/assets/our-work"

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        is_heic = False
        
        # Check by extension
        if filename.lower().endswith(".heic"):
            is_heic = True
        else:
            # Check by signature
            try:
                with open(path, "rb") as f:
                    header = f.read(12)
                    if b"ftypheic" in header or b"ftypmif1" in header:
                        is_heic = True
            except:
                pass

        if is_heic:
            print(f"File {filename} is HEIC. Converting to proper JPEG...")
            try:
                image = Image.open(path)
                
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                    
                # Create the new filename
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_path = os.path.join(folder, new_filename)
                
                # Save as true JPEG
                image.save(new_path, "JPEG", quality=90)
                print(f"Successfully saved {new_filename}")
                
                # Remove original if it had .HEIC extension
                if filename.lower().endswith(".heic"):
                    os.remove(path)
                    print(f"Removed original {filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")
