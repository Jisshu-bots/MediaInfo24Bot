import subprocess 



@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    app_client.process_update(update)
    return "OK", 200

# Function to extract media information using mediainfo command
def get_mediainfo(file_path):
    process = subprocess.Popen(
        ["mediainfo", file_path, "--Output=HTML"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"Error getting media info: {stderr.decode().strip()}")
    return stdout.decode().strip()
  
