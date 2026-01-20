import os
from droidrun import DroidAgent, DroidrunConfig
from agents.prompts import get_shopping_goal

class ShoppingBot:
    def __init__(self):
        try:
            self.config = DroidrunConfig.from_yaml("config.yaml")
        except Exception as e:
            raise ValueError(f"❌ Config Error: Could not load config.yaml. Reason: {e}")

        if not os.getenv("GOOGLE_API_KEY"):
             raise ValueError("❌ GOOGLE_API_KEY is missing!")

    async def find_product(self, product_name, contact_name):
        goal_text = get_shopping_goal(product_name, contact_name)
        
        agent = DroidAgent(
            goal=goal_text,
            config=self.config
        )
        
        print(f"🤖 Agent initialized with config.yaml...")
        return await agent.run()