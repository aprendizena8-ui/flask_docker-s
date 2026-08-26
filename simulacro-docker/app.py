from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a mi API con CI/CD 🚀"

if __name__ == "__main__":
    import os

    
    docker_mode = os.environ.get("DOCKER_MODE", "false").lower() == "true"

    if docker_mode:
        
        app.run(host="0.0.0.0", port=5000) # nosec
    else:
        
        app.run(host="127.0.0.1", port=5000)
