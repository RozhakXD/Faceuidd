import aiohttp, re, asyncio
from flask import jsonify

async def Profile_Facebook(profile_url):
    if 'facebook.com/' in profile_url:
        find_userID = re.search(re.compile(r'(?:id=|facebook\.com/)(\d+)'), str(profile_url))
        if find_userID != None:
            userID = find_userID.group(1)
            return jsonify({"Sukses": True, "Message": f"{userID}"}), 200
        else:
            urls = ('https://web.facebook.com/{}'.format(profile_url.split('facebook.com/')[1]))
            async with aiohttp.ClientSession() as session:
                session.headers.update({
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Sec-Fetch-Mode": "navigate",
                    "Host": "web.facebook.com",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-Dest": "document",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                })
                async with session.get("{}".format(urls)) as response:
                    text = await response.text()
                    find_userID = re.search(r'"userID":"(\d+)"', str(text))
                    if find_userID != None:
                        userID = (find_userID.group(1))
                        return jsonify({"Sukses": True, "Message": f"{userID}"}), 200
                    else:
                        return jsonify({"Sukses": False, "Message": "Couldn't find facebook profile ID"}), 404
    else:
        return jsonify({"Sukses": False, "Message": "There is a problem with your link"}), 400

async def Groups_Facebook(groups_urls):
    if 'facebook.com/groups/' in groups_urls:
        find_groupID = re.search(re.compile(r'facebook\.com/groups/(\d+)'), str(groups_urls))
        if find_groupID != None:
            groupID = find_groupID.group(1)
            return jsonify({"Sukses": True, "Message": f"{groupID}"}), 200
        else:
            urls = ('https://web.facebook.com/groups/{}'.format(groups_urls.split('facebook.com/groups/')[1]))
            async with aiohttp.ClientSession() as session:
                session.headers.update({
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Sec-Fetch-Mode": "navigate",
                    "Host": "web.facebook.com",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-Dest": "document",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                })
                async with session.get("{}".format(urls)) as response:
                    text = await response.text()
                    find_groupID = re.search(r'"groupID":"(\d+)"', str(text))
                    if find_groupID != None:
                        groupID = (find_groupID.group(1))
                        return jsonify({"Sukses": True, "Message": f"{groupID}"}), 200
                    else:
                        return jsonify({"Sukses": False, "Message": "Can't find facebook group ID"}), 404
    else:
        return jsonify({"Sukses": False, "Message": "There is a problem with your link"}), 400

async def Post_Facebook(post_urls):
    if 'facebook.com/' in post_urls:
        urls = ('https://web.facebook.com/{}'.format(post_urls.split('facebook.com/')[1]))
        async with aiohttp.ClientSession() as session:
            session.headers.update({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
                "Sec-Fetch-Mode": "navigate",
                "Host": "web.facebook.com",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-Dest": "document",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            })
            async with session.get("{}".format(urls)) as response:
                text = await response.text()
                find_post_id = re.search(r'"post_id":"(\d+)"', str(text))
                if find_post_id != None:
                    post_id = (find_post_id.group(1))
                    return jsonify({"Sukses": True, "Message": f"{post_id}"}), 200
                else:
                    return jsonify({"Sukses": False, "Message": "Can't find facebook post ID!"}), 404
    else:
        return jsonify({"Sukses": False, "Message": "There is a problem with your link"}), 400

async def Main(facebook_urls):
    tasks = [Profile_Facebook(facebook_urls), Groups_Facebook(facebook_urls), Post_Facebook(facebook_urls)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, tuple) and result[1] == 200:
            return (result)
    return {"Sukses": False, "Message": "Can't find Facebook ID"}, 404