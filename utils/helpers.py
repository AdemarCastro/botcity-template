from botcity.web import By

def not_found(label):
    print(f"[WARNING] Element not found: {label}")

def click(bot, label, matching=0.97, waiting_time=10000):
    """
    Helper function to find and click an element in DesktopBot using try/except.
    """
    try:
        bot.find(label, matching=matching, waiting_time=waiting_time)
        bot.click()
        print(f"{label} clicked.")
    except Exception:
        not_found(label)

def find_and_click(webbot, selector: str, label: str = "", by=By.XPATH, waiting_time=10000):
    """
    Find an element and click it. Logs success or not found.
    """
    try:
        element = webbot.find_element(selector, by=by, waiting_time=waiting_time)
        element.click()
        print(f"[INFO] Clicked: {label or selector}")
        return True
    except Exception:
        not_found(label or selector)
        return False

def find_and_type(webbot, selector: str, text: str, label: str = "", by=By.XPATH, waiting_time=10000):
    """
    Find an element and type text into it using try/except.
    """
    try:
        webbot.find_element(selector, by=by, waiting_time=waiting_time)
        webbot.type_keys(selector, text, by=by)
        print(f"[INFO] Typed into {label or selector}: '{text}'")
        return True
    except Exception:
        not_found(label or selector)
        return False

def find_elements_safe(webbot, selector: str, label: str = "", by=By.XPATH, waiting_time=10000):
    """
    Safely find multiple elements. Returns empty list if none found.
    """
    try:
        elements = webbot.find_elements(selector, by=by, waiting_time=waiting_time)
        print(f"[INFO] Found {len(elements)} elements for {label or selector}")
        return elements
    except Exception:
        not_found(label or selector)
        return []