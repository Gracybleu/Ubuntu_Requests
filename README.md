# Ubuntu-Inspired Image Fetcher

## The Wisdom of Ubuntu: "I am because we are"

This project is inspired by the Ubuntu philosophy, which emphasizes community, respect, sharing, and practicality. The script connects to the global web community, respectfully fetches images, and organizes them locally for later appreciation.

---

## Features
- Prompts the user for an image URL  
- Creates a directory called `Fetched_Images` if it does not exist  
- Downloads the image from the provided URL  
- Saves it with an appropriate filename (extracted from the URL or auto-generated)  
- Handles errors gracefully (e.g., invalid URL, connection issues, HTTP errors)  

---

## Ubuntu Principles Implemented
- **Community**: Connects to the wider web by fetching resources  
- **Respect**: Handles errors without crashing  
- **Sharing**: Organizes fetched images in a dedicated directory  
- **Practicality**: Provides a real, useful tool for saving images  

---

## Requirements
- Python 3.x  
- `requests` library  

Install dependencies with:
```bash
pip install requests
```

---

## Usage
Run the script in your terminal:

```bash
python ubuntu_fetcher.py
```

Enter a valid image URL when prompted. The image will be saved in the `Fetched_Images` directory.

---

## Example
Input:
```
Enter the image URL: https://example.com/sample.jpg
```

Output:
```
Image successfully downloaded and saved as: Fetched_Images/sample.jpg
```

---
