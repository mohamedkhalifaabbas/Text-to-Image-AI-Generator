# Text-to-Image AI Generator

**Text-to-Image AI Generator** is a cutting-edge web application that leverages **Artificial Intelligence** to transform textual descriptions into photorealistic images. Using **Stable Diffusion**, the app generates high-quality visuals that range from people, everyday scenes, objects, to creative artistic concepts—all from simple text prompts.

---

## 🤖 AI Overview

This project demonstrates how modern AI models can **understand language and generate visual content**:

- **Text-to-Image Generation**: The AI model takes a text prompt and converts it into an image.
- **Stable Diffusion Model**: A diffusion-based generative model capable of producing high-resolution images with incredible detail.
- **Prompt-based Control**: Users can influence the AI output by carefully crafting prompts, including style, mood, environment, and lighting.
- **Reproducibility**: Each generation can be controlled using a seed, allowing repeated creation of the same image.

---

## Features

- Generate realistic images from descriptive prompts using AI.
- Fine-tune image outputs using parameters:
  - **Steps**: Number of inference steps for quality control.
  - **Guidance Scale**: Controls adherence to the text prompt.
  - **Seed**: Reproducibility of images.
- Download generated images in high resolution (PNG).
- Works on both CPU and GPU.
- Interactive web interface with real-time generation feedback.

---
Text-to-Image-AI-Generator/
│
├─ app.py                   
├─ model_loader.py        
├─ templates/
│   └─ index.html           
├─ static/
│   ├─ script.js            
│   └─ styles2.css         
├─ Notebooks/               
└─ Generated_Images/  

