import requests

def test_screener_get(headers,base_url):
    endpoint = "/screener.ashx?"
    url= base_url + endpoint
    params = {
        'v': '111',
        'f': 'cap_large,sh_avgvol_o400,sh_curvol_o400,sh_float_o50,sh_relvol_o1.5'
    }

    response = requests.get(url, data=params, headers=headers)
    assert response.ok
    if response.ok:
        print("API request successful")
        print("the status code:" , response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)


def test_screener_put(headers,base_url):
    endpoint = "/screener.ashx?"
    url = base_url + endpoint

    data = {
        'v': '111',
        'f': 'sh_avgvol_o400,sh_curvol_o400,sh_float_o50,sh_relvol_o1.5'
    }


    response = requests.put(url, data=data , headers=headers)

    assert response.ok
    if response.ok:
        print("API request successful")
        print("the status code:" , response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)



def test_search_stock(headers, base_url):
    endpoint = "/quote.ashx?"
    url = base_url + endpoint

    data = {
        't': 'aapl',
    }

    response = requests.get(url, data=data, headers=headers)

    assert response.ok
    if response.ok:
        print("API request successful")
        print("Status code:", response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)


def test_map_SP500(headers, base_url):
    endpoint = "/map.ashx?"
    url = base_url + endpoint

    data = {
        't': 'sec',
    }
    response = requests.get(url, data=data, headers=headers)

    assert response.ok
    if response.ok:
        print("API request successful")
        print("Status code:", response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

def test_map_world(headers, base_url):
    endpoint = "/map.ashx?"
    url = base_url + endpoint

    data = {
        't': 'geo',
    }
    response = requests.get(url, data=data, headers=headers)

    assert response.ok
    if response.ok:
        print("API request successful")
        print("Status code:", response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

def test_map_week(headers, base_url):
    endpoint = "/map.ashx?"
    url = base_url + endpoint

    data = {
        't': 'geo',
        'st': 'w1'
    }
    response = requests.get(url, data=data, headers=headers)

    assert response.ok
    if response.ok:
        print("API request successful")
        print("Status code:", response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

def test_map_month(headers, base_url):
    endpoint = "/map.ashx?"
    url = base_url + endpoint

    data = {
        't': 'geo',
        'st': 'w4'
    }
    response = requests.get(url, data=data, headers=headers)

    assert response.ok
    if response.ok:
        print("API request successful")
        print("Status code:", response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

def test_map_year(headers, base_url):
    endpoint = "/map.ashx?"
    url = base_url + endpoint

    data = {
        't': 'geo',
        'st': 'w52'
    }
    response = requests.get(url, data=data, headers=headers)

    assert response.ok
    if response.ok:
        print("API request successful")
        print("Status code:", response.status_code)
    else:
        print("API request failed")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
