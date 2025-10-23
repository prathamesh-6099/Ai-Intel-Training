from huggingface_hub import InferenceClient
import os

from dotenv import load_dotenv
load_dotenv()

HF_API_TOKEN=os.environ.get("HF_API_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_API_TOKEN
)

result = client.text_generation(
    model="google/gemma-2-2b-it",
    prompt="Can you please let us know more details about your "
)

print(result)
