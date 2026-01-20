import asyncio
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.shopper import ShoppingBot

load_dotenv()

async def main():
    print("--- DroidRun Shopping Agent --- ")
    
    product = input("🛍️ Enter Product Name : ")
    contact = input("👤 Enter WhatsApp Contact Name : ")
    
    try:
        bot = ShoppingBot()
        
        print("\n⚡ Launching DealDroid...")
        result = await bot.find_product(product, contact)
        
        print("\n ---Mission Complete!---")
        
        print(f"📝 Output Log: {str(result)}") 
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())