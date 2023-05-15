import requests
from tools import request,calculate
import json
import configloader
c = configloader.config()
handler = request.request_handler()
data = {
}
ret = handler.post_request("/v0/west/getmessages",data)
print(ret)
messages = ret["messages"]
data = {
    "messages":[]
}
source = c.getkey("client_id")
is_first = True
for message_id,message in messages.items():
    print(".".join([message["source"],message["message"]]))
    if is_first:
        is_first = False
        sign = calculate.sha512(".".join([message_id, c.getkey("client_id"), message["source"], message["message"]]))
        once_data = {
            "message_id":message_id,
            "source":message["source"],
            "sign":sign
        }
        ret = handler.post_request("/v0/west/updatestatus",once_data)
        print(ret)
        continue
    sign = calculate.sha512(".".join([message_id, c.getkey("client_id"), message["source"], message["message"]]))
    data["messages"].append({
        "message_id":message_id,
        "source":message["source"],
        "sign":sign
    })
ret = handler.post_request("/v0/west/updatemultistatus",data)
print(ret)
