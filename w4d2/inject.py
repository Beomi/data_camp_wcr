# inject.py
from bs4 import BeautifulSoup
from mitmproxy import ctx

def response(flow):
    if flow.response.headers['Content-Type'] != 'text/html':
        return
    if not flow.response.status_code == 200:
        return

    html = BeautifulSoup(flow.response.text, 'lxml')
    container = html.select_one('head')
    if container:
        script = html.new_tag('script', type='text/javascript')
        content_js = open('content.js').read()
        script.string = content_js
        container.insert(0, script)
        flow.response.text = str(html)
        ctx.log.info('Successfully injected the content.js script.')
