import requests

def check_openai_balance(api_key):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        url = "https://api.openai.com/dashboard/billing/credit_grants"

        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return False, f"Error: {response.status_code} - {response.text}"

        data = response.json()
        total = data.get("total_granted", 0)
        used = data.get("total_used", 0)
        available = data.get("total_available", 0)

        result = f"Total: ${total:.2f}, Used: ${used:.2f}, Available: ${available:.2f}"
        return True, result

    except Exception as e:
        return False, f"Exception: {str(e)}"
