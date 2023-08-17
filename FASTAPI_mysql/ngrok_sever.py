from pyngrok import ngrok
import uvicorn

# Run FastAPI with Uvicorn
uvicorn.run("main:app", host="127.0.0.1", port=8000)

# Set up Ngrok tunnel
public_url = ngrok.connect(8000)
print("Public URL:", public_url)

# Keep the program running to maintain the ngrok tunnel
ngrok_process = ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    ngrok.kill()
    