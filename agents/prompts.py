def _step_flipkart(product_name: str) -> str:
    return (
        "STEP 1: FLIPKART CHECK\n"
        "- Open Flipkart using package name 'com.flipkart.android'.\n"
        "- Tap the Search Bar at the second top.\n"
        f"- Type '{product_name}' and hit search.\n"
        "- Wait for results to load completely.\n"
        "- CHECK FOR ADS: If the first result says 'Sponsored' or 'Ad', SCROLL down to find the real organic result.\n"
        "- FIND PRODUCT: Look for the exact product match.\n"
        "- IF found:Click the product Read the Price and Rating.\n"
        "- Click Add to cart/bag if available search by scrolling."
        "-Move if Not available."
        "  - IF NOT found: Note down 'Not available on Flipkart'.\n"
        "- REMEMBER this data exactly."
    )

def _step_myntra(product_name: str) -> str:
    return (
        "STEP 2: Myntra CHECK\n"
        "- Open Myntra using package name 'com.myntra.android'.\n"
        "- Tap the Search Bar at the top.\n"
        f"- Type '{product_name}' and hit search.\n"
        "- Wait for results to load completely.\n"
        "- CHECK FOR ADS: If the first result says 'Sponsored' or 'Ad', SCROLL down to find the real organic result.\n"
        "- FIND PRODUCT: Look for the exact product match.\n"
        "  - IF found: click the product Read the Price and Rating.\n"
        "- Click Add to cart/bag if available search by scrolling."
        "-Move if Not available."
       
        "- IF NOT found: Note down 'Not available on Myntra'.\n"
        "- REMEMBER this data exactly." \
        "-go back to home screen."
    )

def _step_amazon(product_name: str) -> str:
    
    return (
        "STEP 3: AMAZON CHECK\n"
        "- Open Amazon using package name 'com.amazon.mShop.android.shopping"
        "- Wait for results to load completely.\n"
        "- CHECK FOR ADS: Look at the first result. If you see text like 'Sponsored', 'Ad', or 'Promoted', SCROLL down to skip it.\n"
        "- FIND PRODUCT: Look for the exact product match.\n"
        "- IF found:click the product Read the Price (e.g., ₹50,000) and Rating (e.g., 4.5 stars).\n"
        "- Click Add to cart/bag if available search by scrolling."
        "-Move if Not available."
        "- IF NOT found (or out of stock): Note down 'Not available on Amazon'.\n"
        "- REMEMBER this data exactly (e.g., 'Amazon: ₹50,000, 4.5 stars' OR 'Amazon: Not available')."
    )

def _step_report(product_name: str) -> str:
    return (
        "STEP 3: COMPILE REPORT\n"
        "- Create a structured summary like this:\n"
        f"  'Shopping Report for {product_name}:\n"
        "  - Amazon: [Price/Status] | [Rating]\n"
        "  - Flipkart: [Price/Status] | [Rating]\n'"
        "  - Myntra: [Price/Status] | [Rating]'"

    )

def _step_whatsapp(contact_name: str,product_name: str) -> str:
    return (
        "STEP 4: SEND ON WHATSAPP\n"
        "- Open 'WhatsApp' (com.whatsapp).\n"
        f"- Tap search and find contact '{contact_name}'.\n"
        "- Click their name to open chat.\n"
        "- Type the summary report in format: "
        """f"  ' 🎯* DealDroid Report: {product_name}*\n"
              --------------------------------------\n"
                  🔶 *Flipkart:*\n"
                  💰 Price: [Price]\n"
                  ⭐ Rating: [Rating]\n"

                  🛒 *Amazon Check:*\n"
                  💰 Price: [Price]\n"
                  ⭐ Rating: [Rating]\n\n"

                  🔶 *Myntra Check:*\n"
                  💰 Price: [Price]\n"
                  ⭐ Rating: [Rating]\n"
             ---------------------------------------\n"
        💡  -> Compare the prices above and grab the deal!\n"
            -> Products are added to cart.
            -> Sent via DealDroid 🤖_'\n\n"""
        " and Click Send."
    )

def get_shopping_goal(product_name: str, contact_name: str) -> str:
    """
    Combines all robust steps into the final mission.
    """
    return (
        f"You are a Smart Shopping Agent. Your goal is to find the best price for '{product_name}'.\n"
        "Follow these exact steps:\n\n"
        f"{_step_flipkart(product_name)}\n\n"
        f"{_step_myntra(product_name)}\n\n"
        f"{_step_amazon(product_name)}\n\n"
        f"{_step_report(product_name)}\n\n"
        f"{_step_whatsapp(contact_name,product_name)}\n\n"
        "Do NOT stop until the message is sent."
    )