import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Dict, List

load_dotenv()

@dataclass
class Constitution:
    """Constitutional parameters for trading."""
    max_daily_trades: int = int(os.getenv('MAX_DAILY_TRADES', 50))
    max_position_usd: float = float(os.getenv('MAX_POSITION_USD', 2.00))
    max_daily_loss_usd: float = float(os.getenv('MAX_DAILY_LOSS_USD', 10.00))
    min_signal_confidence: float = float(os.getenv('MIN_SIGNAL_CONFIDENCE', 0.85))
    cooldown_seconds: int = int(os.getenv('COOLDOWN_SECONDS', 30))
    kill_switch: bool = os.getenv('KILL_SWITCH', 'False').lower() == 'true'

# Factory addresses for Base (example addresses, need to be verified)
FACTORY_ADDRESSES = {
    'UniswapV2': '0x...',  # Replace with actual Base UniswapV2 factory
    'ERC20MemeTemplate': '0x...',
    'CommonProxyDeployer': '0x...'
}

# Validation gates
VALIDATION_GATES = [
    'wash_trade_detection',
    'mev_vulnerability',
    'lp_concentration_risk',
    'contract_red_flags',
    'social_bot_analysis',
    'deployer_reputation',
    'time_series_anomaly'
]

# Web3 provider
WEB3_PROVIDER_URI = os.getenv('WEB3_PROVIDER_URI', 'https://mainnet.base.org')

# Social media
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')