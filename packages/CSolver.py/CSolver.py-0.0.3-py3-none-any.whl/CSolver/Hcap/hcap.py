import requests

class Solver:
    def solve(api_key, sitekey, site, proxy=None, rqdata=None):
        headers = {'API-Key': api_key}
        payload = {
            'sitekey': sitekey,
            'site': site,
            'proxy': proxy,
            'rqdata': rqdata
        }
        
        response = requests.post("https://api.csolver.xyz/solve", headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            solution = data.get('solution')
            return solution
        else:
            return None