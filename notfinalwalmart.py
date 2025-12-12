from bs4 import BeautifulSoup
import requests
import json

walmart_url = "https://www.walmart.com/ip/Samsung-25-Odyssey-FHD-IPS-240Hz-G-Sync-Gaming-Monitor-LS25BG400ENXGO/16987913337?classType=REGULAR&from=/search"

HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language" : "en-US",
    "Cookie": "isoLoc=GE__t3; adblocked=true; ACID=3b345011-cfe6-475a-88e9-6da65f1d7276; _m=9; hasACID=true; sod=torbit1761723862; abqme=true; vtc=T7a0Y6YhrNxfAZgJOWPTy0; _pxhd=a48f4efdc90d039e8c6d59bf9c12f2566fd2c762b9d3ff182c50ae8818e6e418:15720249-b49b-11f0-8bd9-3e52e4e0c42c; io_id=e373d352-9440-486f-9ed2-ecc1e74810a1; assortmentStoreId=3081; hasLocData=1; AID=wmlspartner=0:reflectorid=0000000000000000000000:lastupd=1761723891906; ipSessionTrafficType=Internal; _astc=fb531e1ae40aee1fd598bf53a2d7c0e5; _intlbu=false; _shcc=US; bm_mi=4F49433A3C95FFCE1DCBB837AD876637~YAAQPWd7XHrlEBOaAQAAt5NcLx0BUjBenMCI5XNJGkD35g72QZeHWxZR7JGD6cQ1G1mdAAP/+GakEPmQDKZVMTEzWqLmrT6x0JrlT6IRjDdaXuypPYwtJ2QCnSc8KiwGv7JniFlEBwMIfVuIfKvJDqMlV6UzTq3zcy34aupeGaAT1k8tKg3lgJPIXGIWH/BnSdnmk4GBkIxh0XqqZdpFz8/IW3OTXawAAhrCzHYeXF0H6IQPJL0FzUHxlTuYyk/1iItHz9d8jgBEP3aEYzdmlay+YtH2uZZOp3YAOcblj9s3IYmOYNEzZhZsZNmWmpUNkAKB3Vpq2BLQJFuUpmncXNWuYife91dZ+nofLB1Rdjy8jp7dtP7Br5uvoSV8hsv4SVL5ISoQm5HcVe+MRkyOSoI+0EvRAvPyW8zdso4KmRh24g==~1; userAppVersion=usweb-1.231.0-b97723bf2aef979c130854d06a7a3f4ce114722a-0281814r; bm_sv=E800F226796594915A8D4D36A85567E3~YAAQPWd7XK7rEBOaAQAA/s5cLx0Zx21MYPfvLAB2xBAI61TI5FP71bagXH4rHkeGCz8A585HbZhpaO2iuLbN891xY77065zzwacTYpB1YkUE8SnuALvBwZMwWWmwux3wzBpnc9OJTpQ7/yjEGBDfMVtbVsWsv9Wxol1vMEKtJ03h1ebPWAEkM2c6dzMUnfJDXU7pUayUS3K0bDVMFMVXAbdHovfZg6RjalTPIcT3Vs5wKm5nxfS7uyvuBdGouoy7QnU=~1; ak_bmsc=81E8F5EA7C4B86F3C73FB2F27A414B1D~000000000000000000000000000000~YAAQPWd7XD/sEBOaAQAAj9VcLx1wmE8nRAtg+pQBYrKj4B6IUc7D1yExfmYMDwTAMliI3sOFAVRo9cjO+7lArgBX2y6NJOs8KscJqjvwKRZDglPP14Lvoh4xI8ULh62lvhd3vzETn2KuTh8EDHECsITkF9V4zZXlKNib+4vg+AaT+FRfockmEZtRGXSs6OjmzLgcLibr2sj5C4C7rTT0qRZU3bALgpyrsHGu9im2wrF5lgxSI4YgO5ZAwQgtE6BHvn8QcCT9YCueHw4qkuyxgE++eAjX5dAy+XDIQkeihZuL1SRmWmmO9VVSnjHh77iih57ikF4ZPjIiSxjjThBG74rqBsI1kD8HaftIH1lr/zdUxxKNAZTqRjA9W1L86NUsQShiQkC6Uqw+c6+l3VusgEMf57r+6+fjG5aGvSVvwIikH3lrFPLwYPVPkCoW2FF9yLI1/0HlJwmOEVrYSDQKJG0+q/Pd8X2wmjQKqEv6TKkWfxzIf190wqC3HDmFNDoaX0X99cE2rGSH7VI5lr919iiTeg==; bstc=bv2C3OI3Mtb2HE3EmsdwFU; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=1AWnT|7AcKQ|Gvrfy|LJ--3|LWUOz|TCS94|alITu|fdm-7|jM1ax|pQ-wz|tUYXu|uwH_b|zOu8D; exp-ck=1AWnT27AcKQ1Gvrfy2TCS941fdm-71tUYXu1uwH_b4zOu8D1; xpm=1%2B1761733777%2BT7a0Y6YhrNxfAZgJOWPTy0~%2B0; pxcts=2c539d89-b4b6-11f0-975f-c0573211c7a5; _pxvid=15720249-b49b-11f0-8bd9-3e52e4e0c42c; _xrps=false; if_id=FMEZARSF7wCzrlzxRy6nbXgRoi+A9E1jCTy+cdhq6cDXLZD4Z4uEXJen5869KRBhNOJAWcXLKqx0OxAozt5W6BcCAOHyj0Vtvh/FbT+J2j89Pl+Kwx0fDzLg/0mDmLEmUjFico5XdeNsZK2DpG1Y6CSlkYds2btpFU4sT+Br4JlxdF4VV1cn+H/Z356aGky1RPlmxAR2Z+WS6zvkcHDWbOIzez64W6KnlU/Rs/GeWgiOA3fQCYlvL+xHboeyYrFZ7kMGz1yDAwaoj2+EHQFXiJG1GdBfe111rIgi5YsE7J7I61Urcf4jnselSmxO74VcpKx9pr4lkLhteSj6TpE=; TS016ef4c8=019db772aebae4851ee9b19572c5017795111fdb48bfd37e108c37de80e221cfe66ab9a09e53ddacdf652e52ec9429a8e50af8e4f2; TS01f89308=019db772aebae4851ee9b19572c5017795111fdb48bfd37e108c37de80e221cfe66ab9a09e53ddacdf652e52ec9429a8e50af8e4f2; TS8cb5a80e027=08f595d3f7ab2000817a2a7151dbd52581a998e4e83898ec48ffb990b7f84bfe459ad89804cd019808437132071130007e3f37dc4ec5c3fdefbffd7c6f247adf7a007457a986d5e17fe6aec6c59108e8d511bcdf0729403c906aa35b231c9919; com.wm.reflector=reflectorid:0000000000000000000000@lastupd:1761736034485@firstcreate:1761723891906; locDataV3=eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJub2RlSWQiOiIzMDgxIiwiZGlzcGxheU5hbWUiOiJTYWNyYW1lbnRvIFN1cGVyY2VudGVyIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdFUkJFUiBST0FEIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJhbGxvd2VkV0lDQWdlbmNpZXMiOlsiQ0EiXSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX1NQRUNJQUxfRVZFTlQiLCJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdLCJ0aW1lWm9uZSI6IkFtZXJpY2EvTG9zX0FuZ2VsZXMiLCJzdG9yZUJyYW5kRm9ybWF0IjoiV2FsbWFydCBTdXBlcmNlbnRlciIsInNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQifV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6MzguNDgyNjc3LCJsb25naXR1ZGUiOi0xMjEuMzY5MDI2LCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTIiwibG9jYXRpb25BY2N1cmFjeSI6ImxvdyIsImdpZnRBZGRyZXNzIjpmYWxzZSwiYWxsb3dlZFdJQ0FnZW5jaWVzIjpbIkNBIl19LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR0VSQkVSIFJPQUQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sInNjaGVkdWxlZEVuYWJsZWQiOmZhbHNlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOmZhbHNlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJpc0V4cHJlc3NEZWxpdmVyeU9ubHkiOmZhbHNlLCJhbGxvd2VkV0lDQWdlbmNpZXMiOlsiQ0EiXSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdLCJ0aW1lWm9uZSI6IkFtZXJpY2EvTG9zX0FuZ2VsZXMiLCJzdG9yZUJyYW5kRm9ybWF0IjoiV2FsbWFydCBTdXBlcmNlbnRlciIsInNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQifSwiaXNnZW9JbnRsVXNlciI6ZmFsc2UsIm1wRGVsU3RvcmVDb3VudCI6MCwicmVmcmVzaEF0IjoxNzYxNzQ1NDY2ODU2LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6M2IzNDUwMTEtY2ZlNi00NzVhLTg4ZTktNmRhNjVmMWQ3Mjc2In0=; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTc2MTcyMzg2Njg1NCwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9LCJzaGlwcGluZ0FkZHJlc3MiOnsidGltZXN0YW1wIjoxNzYxNzIzODY2ODU0LCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6Ijk1ODI5IiwiZGVsaXZlcnlTdG9yZUxpc3QiOlt7Im5vZGVJZCI6IjMwODEiLCJ0eXBlIjoiREVMSVZFUlkiLCJ0aW1lc3RhbXAiOjE3NjE3MjM4NjY4NTMsImRlbGl2ZXJ5VGllciI6bnVsbCwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCIsInNlbGVjdGlvblNvdXJjZSI6bnVsbH1dLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EifSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE3NjE3MjM4NjY4NTQsImJhc2UiOiI5NTgyOSJ9LCJtcCI6W10sIm1zcCI6eyJub2RlSWRzIjpbXSwidGltZXN0YW1wIjpudWxsfSwibXBEZWxTdG9yZUNvdW50IjowLCJzaG93TG9jYWxFeHBlcmllbmNlIjpmYWxzZSwic2hvd0xNUEVudHJ5UG9pbnQiOmZhbHNlLCJtcFVuaXF1ZVNlbGxlckNvdW50IjowLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6M2IzNDUwMTEtY2ZlNi00NzVhLTg4ZTktNmRhNjVmMWQ3Mjc2In0=; xptc=_m%2B9~assortmentStoreId%2B3081; xptwg=1449664310:19C084A6D76BAD0:3EC8042:F74E550D:A6EF29C6:2C85CC49:; xptwj=uz:f64dcb8e033869c6b09a:tMYjqn1sIRNgmidMOSekIL15p/UJP72j4GvHsyufykIE6LQ/lr9JbxXnnwHJ74MaYXVvWa4G6DjXCyNDz2QQq/VkPW9Z1CQyRnWPWAEhb4gU7abs9lCI+rUqo4O5ME4ANty1luStL5njt1PM+/YAw/SUjaeE5uDlecB5rPvv8dmz5jkav8O12S82OS9HLwJUypp8owikGntkatseqtLV; TS012768cf=0109a50f0b58ac304ca1938bec2dd4babe2066e5c24438fb8d1236013ca6519b097770a7dd6ec9d5a6bd6a19e61704ffb294697a59; TS01a90220=0109a50f0b58ac304ca1938bec2dd4babe2066e5c24438fb8d1236013ca6519b097770a7dd6ec9d5a6bd6a19e61704ffb294697a59; TS2a5e0c5c027=083adf28b9ab2000ecf4590ee5f2414588af29c12a556b0bc102bcb5f475d6ffc3be86b1fc44b4b70808431f62113000d2b0145c60ef5f9fa32d0ecb6779f8e11245cbbf0f61bd5b4f4c6a8c85213fe132dc2dddcde334082f5bd2f6bfc57f67; akavpau_p2=1761736635~id=0feef78e7dbdcd6ee365614948aed180",
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

def get_product_links(query, page_number=1):
    search_url = f"https://www.walmart.com/search?q={query}&page={page_number}"

    response = requests.get(search_url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all('a', href=True)

    product_links = []

    for link in links:
        link_href = link['href']
        if "/ip/" in link_href:
            if "https" in link_href:
                full_url = link_href
            else:
                full_url = "https://www.walmart.com" + link_href
            
            product_links.append(full_url)

    return product_links



def extract_product_info(product_url):
    response = requests.get(product_url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    script_tag = soup.find("script", id="__NEXT_DATA__")

    data = json.loads(script_tag.string)
    initial_data = data["props"]["pageProps"]["initialData"]["data"]
    product_data = initial_data["product"]
    reviews_data = initial_data.get("reviews", {})

    product_info = {
        "price": product_data["priceInfo"]["currentPrice"]["price"],
        "review_count": reviews_data.get("totalReviewCount", 0),
        "item_id": product_data["usItemId"],
        "avg_rating": reviews_data.get("averageOverallRating", 0),
        "product_name": product_data["name"],
        "brand": product_data.get("brand", ""),
        "availability": product_data["availabilityStatus"],
        "image_url": product_data["imageInfo"]["thumbnailUrl"],
        "short_description": product_data.get("shortDescription", "")
    }

    return product_info

def main():
    OUTPUT_FILE = "product_info1.jsonl"

    with open(OUTPUT_FILE, 'w') as file:
        page_number = 1
        while True:
            links = get_product_links("computers", page_number)
            if not links or page_number > 99:
                break

            for link in links:
                try:
                    product_info = extract_product_info(link)
                    if product_info:
                        file.write(json.dumps(product_info)+"\n")
                except Exception as e:
                    print(f"Failed to process URL {link}. Error {e}")
            page_number += 1
            print(f"Search page {page_number}")


if __name__ == "__main__":
    main()
