import requests
from tools import request,calculate
import json
import configloader
c = configloader.config()
handler = request.request_handler()

message = calculate.base64_encode("Hello World!")
message_id = calculate.genuuid()
destination = "c831cf2d-5bde-4ba9-9a9a-4e1ef7dff00f"
source = c.getkey("client_id")
data = {
    "message_id":message_id,
    "message":message,
    "source":source,
    "destination":destination,
}
ret = handler.post_request("/v0/east/addmessage",data)
data = {
    "message_id":message_id,
    "message":message,
    "source":source,
    "destination":destination,
}
ret = handler.post_request("/v0/east/getstatus",data)
print(ret)

data = {
    "messages":[
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        }
    ]
}
ret = handler.post_request("/v0/east/addmessages",data)
print(ret)
ret = handler.post_request("/v0/east/getmultistatus",data)
print(ret)
