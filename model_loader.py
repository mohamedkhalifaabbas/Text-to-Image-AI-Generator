import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image

# ========================
# 1️⃣ تحميل الموديل
# ========================
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=dtype
        )
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe = pipe.to(device)

        if device == "cuda":
            pipe.enable_attention_slicing()
            try:
                pipe.enable_xformers_memory_efficient_attention()
            except Exception:
                pass

        return pipe
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e

# ========================
# 2️⃣ تحميل الموديل مرة واحدة عند تشغيل السيرفر
# ========================
model_pipe = load_model()

# ========================
# 3️⃣ دالة لتوليد الصور
# ========================
def generate_image(prompt, steps=30, guidance=7.5, seed=None):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    if seed is None:
        seed = torch.randint(0, 1000000, (1,)).item()

    generator = torch.Generator(device=device).manual_seed(seed)

    image = model_pipe(
        prompt,
        num_inference_steps=steps,
        guidance_scale=guidance,
        generator=generator
    ).images[0]

    return image
