from app import app

# Vercel requires the WSGI app to be named `app` inside a file specified in vercel.json `src`
# Since we configured "src": "index.py", this file loads our Flask instance.
