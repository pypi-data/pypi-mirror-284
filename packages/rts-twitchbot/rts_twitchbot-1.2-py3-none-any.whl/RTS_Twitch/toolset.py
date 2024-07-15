from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
import aiohttp
from aiohttp import ClientTimeout
async def paginate(channel_id:int, url:str, methode:str="GET",data:dict={}, headers_modifier:dict={})->dict:
    headers= {
            "Client-ID": memory.app_id,
        }


    if not channel_id is None:
        get_user = overwrites.get_user(channel_id)
        if not get_user:
            return {"error":"User not found.","issue_code":"db_user_not_found"}
        headers["Authorization"] = f"Bearer {get_user['access_token']}"
        
    headers.update(headers_modifier)
    querry = ""
    bonusdata = {}
    all_data = []
    async with aiohttp.ClientSession() as session:
        while True:
            if methode == "GET":
                response = await session.get(url + querry, headers=headers,data=data)
            elif methode == "POST":
                response = await session.post(url + querry, headers=headers,json=data)
            elif methode == "PATCH":
                response = await session.patch(url + querry, headers=headers,json=data)
            elif methode == "DELETE":
                response = await session.delete(url + querry, headers=headers)
            else:
                return {"error":"Invalid methode","issue_code":"invalid_methode"}

            data = await response.json()
            if not response.ok:
                return {"error":f"Error in paginate. @toolset.py(paginate)->{await response.text()}","issue_code":"response_not_ok"}
            all_data.extend(data["data"])

            for k,v in data.items():
                if not k in ["data", "pagination"]:
                    bonusdata[k] = v
            if "pagination" in data and "cursor" in data["pagination"]:
                if "?" in url:
                    querry = "&after="+data["pagination"]["cursor"]
                else:
                    querry = "?after="+data["pagination"]["cursor"]
            else:
                break
    await session.close()

    all_data
    return all_data, bonusdata


        

async def single(channel_id:int,url:str,methode:str="GET", headers_modifier:dict={}, data:dict={})->dict:
    get_user = overwrites.get_user(channel_id)
    if not get_user:
        return {"error":"User not found.","issue_code":"db_user_not_found"}
    headers= {
        "Client-ID": memory.app_id,
        "Authorization": f"Bearer {get_user['access_token']}"
    }
    headers.update(headers_modifier)
    timeout = ClientTimeout(total=10)  # 10 Sekunden Timeout für die gesamte Operation
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            if methode == "GET":
                response = await session.get(url, headers=headers, data=data)
            elif methode == "POST":
                response = await session.post(url, headers=headers, json=data)
            elif methode == "PATCH":
                response = await session.patch(url, headers=headers, json=data)
            elif methode == "DELETE":
                response = await session.delete(url, headers=headers)
            else:
                return {"error": "Unsupported method.", "issue_code": "unsupported_method"}

            if not response.ok:
                return {"error": f"Error in single_request. @toolset.py(single)->{await response.text()}", "issue_code": "response_not_ok"}
            return await response.json()
    except aiohttp.ClientError as e:
        return {"error": f"ClientError in single_request. @toolset.py(single)->{str(e)}", "issue_code": "client_error"}
        
        
