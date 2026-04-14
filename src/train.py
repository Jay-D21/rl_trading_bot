import yfinance as yf
from stable_baselines3 import DQN
from env import SimpleTradingEnv

def train_bot():
    print("Fetching historical data for AAPL...")
    ticker = yf.Ticker("AAPL")
    df = ticker.history(period="1y")
    prices = df['Close'].values
    
    print("Initializing environment...")
    env = SimpleTradingEnv(prices)
    
    print("Training DQN Agent (1000 timesteps)...")
    model = DQN("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=1000)
    
    print("Training complete! Model ready for evaluation.")

if __name__ == "__main__":
    train_bot()
