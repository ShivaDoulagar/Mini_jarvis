import subprocess

def ask_llm(prompt: str) -> str:
    """
    Send a prompt to Ollama (e.g., mistral or llama3.2) and return the response as text.
    """

    # Run ollama
    process = subprocess.Popen(
        ["ollama", "run", "mistral"],   # You can replace 'mistral' with 'llama3.2' or another model
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    # Send prompt and get output
    out, err = process.communicate(prompt)

    if err:
        print(f"⚠️ Ollama error: {err}")

    # Return the raw response string
    return out.strip()
