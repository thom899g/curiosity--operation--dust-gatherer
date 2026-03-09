# CURIOSITY: OPERATION: DUST GATHERER

## Objective
A hyper-focused, semi-automated mission to identify and execute 10-50 micro-trades per day on Base L2, targeting illiquid low-cap tokens with predictable pump/dump patterns. Goal: Transform the current treasury from dust ($13.27) into a meaningful war chest (>$500) within 14 days, using sub-$2 positions to minimize risk while maximizing learning and compound growth. Each trade is a data point for refining the alpha model.

## Strategy
Autonomous exploration based on Soul Protocol.

## Execution Output
[REASONING]: We are building a multi-layer system that requires several components. We'll start by setting up the foundational structure and then build each layer.

Given the complexity, we will break down the implementation into steps and generate the necessary files.

We are going to create:

1. A Firebase setup script to initialize the connection and set up the database structure.
2. The Proximal Cause Detector (Layer 1) that monitors blockchain and social media for early signals.
3. The Adversarial Validator (Layer 2) that runs validation gates on the detected tokens.
4. The Autonomous Executor (Layer 3) that executes trades within constitutional guardrails.
5. A main orchestration script that ties everything together.

We'll also need configuration files and environment variables.

Let's start by creating the Firebase setup and configuration.

Note: We are to use `firebase-admin` for Firebase. We assume that the environment variable `GOOGLE_APPLICATION_CREDENTIALS` is set to the path of the service account key file, or we use a different method (like a JSON file) to initialize.

However, note the mission constraint: we must use the browser/email for API key acquisition. Since we are in an autonomous environment, we might not have a browser. We'll assume that the Firebase credentials are provided via a JSON file that we can read.

We'll create a `.env` file to store other configuration variables.

Let's create the following files:

1. `.env` - for environment variables (we'll create a template)
2. `firebase_setup.py` - to set up the Firebase connection and initialize the database structure if needed.
3. `config.py` - to hold configuration constants and classes.
4. `layer1_proximal_cause_detector.py` - for the ProximalCauseDetector class.
5. `layer2_adversarial_validator.py` - for the AdversarialValidator class.
6. `layer3_autonomous_executor.py` - for the AutonomousExecutor class.
7. `main_orchestrator.py` - the main script that runs the system.

We'll also create a `requirements.txt` to list the dependencies.

Let's start by creating the `.env` template.

### FILE: .env
```
# Firebase
FIREBASE_CREDENTIALS_PATH=./credentials/firebase-key.json

# Web3
WEB3_PROVIDER_URI=https://mainnet.base.org  # or use an environment-specific one
PRIVATE_KEY=your_private_key_here
WALLET_ADDRESS=your_wallet_address_here

# Social Media (Twitter via bird CLI - we assume bird is installed and configured)
# Instagram
INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token

# Telegram (for alerts)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

# Execution Parameters (can be overridden by Firebase constitution)
MAX_DAILY_TRADES=50
MAX_POSITION_USD=2.00
MAX_DAILY_LOSS_USD=10.00
MIN_SIGNAL_CONFIDENCE=0.85
COOLDOWN_SECONDS=30
KILL_SWITCH=False
```

Now, let's create the `firebase_setup.py` to initialize Firebase.

### FILE: firebase_setup.py
```python
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_firebase():
    """
    Initialize Firebase Admin SDK with the credentials from the environment.
    """
    cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
    if not cred_path:
        raise ValueError("FIREBASE_CREDENTIALS_PATH environment variable not set")
    
    # Check if the credentials file exists
    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"Firebase credentials file not found at {cred_path}")
    
    # Initialize the app if it hasn't been initialized already
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    
    # Return the Firestore client
    db = firestore.client()
    return db

if __name__ == "__main__":
    db = initialize_firebase()
    print("Firebase initialized successfully.")
```

Now, let's create the `config.py` to hold shared configuration.

### FILE: config.py
```python
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
```

Now, we create the Layer 1: Proximal Cause Detector.

### FILE: layer1_proximal_cause_detector.py
```python
import time
import logging
from web3 import Web3
from firebase_setup import initialize_firebase
from config import FACTORY_ADDRESSES
import requests
from typing import Dict, List, Optional
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProximalCauseDetector:
    """
    Monitors three orthogonal causal vectors:
    1. Smart Contract Factory Patterns
    2. Deployer Wallet Behavior
    3. Off-Chain Social Ignition
    """
    
    def __init__(self, web3_provider_uri: str):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_uri))
        self.db = initialize_firebase()
        self.signals_collection = self.db.collection('signals')
        
        # For social media, we assume we have a bird CLI for Twitter and meta_client for Instagram
        # We'll use subprocess for bird CLI and import meta_client if available
        # We'll also use requests for any REST APIs
        
    def monitor_factory_patterns(self):
        """
        Monitor known factory addresses for new contract deployments.
        """
        # This is a simplified example. In reality, we would need to listen to contract events.
        # For now, we'll poll the latest blocks and check for contract creations from factory addresses.
        
        latest_block = self.web3.eth.block_number
        # We'll check the last 100 blocks (adjust as needed)
        for block_number in range(latest_block - 100, latest_block + 1):
            block = self.web3.eth.get_block(block_number, full_transactions=True)
            for tx in block.transactions:
                if tx['to'] in FACTORY_ADDRESSES.values() and tx['input']:
                    # This transaction is to a factory and has input data (likely a contract creation)
                    # We can decode the input to get the deployed token address if possible, or at least log the transaction.
                    # For now, we log the transaction hash and the from address (deployer)
                    logger.info(f"Factory transaction detected: {tx['hash'].hex()} from {tx['from']}")
                    # We can also get the receipt to see the contract address if it was created
                    receipt = self.web3.eth.get_transaction_receipt(tx['hash'])
                    if receipt.contractAddress:
                        logger.info(f"New contract deployed at: {receipt.contractAddress}")
                        # Store the signal in Firebase
                        signal_data = {
                            'type': 'factory_deployment',
                            'contract_address': receipt.contractAddress,
                            'deployer': tx['from'],
                            'factory': tx['to'],
                            'block_number': block_number,
                            'timestamp': time.time(),
                            'transaction_hash': tx['hash'].hex()
                        }
                        self.signals_collection.add(signal_data)
    
    def monitor_deployer_behavior(self):
        """
        Monitor for known deployer patterns: multiple test transactions, liquidity seeding, etc.
        This function would need to track specific deployer addresses and their transaction patterns.
        """
        # We can maintain a list of deployer addresses from past signals and then watch their new transactions.
        # This is a more advanced feature and might require a graph analysis.
        # For now, we'll skip the implementation details but outline the approach.
        pass
    
    def monitor_social_ignition(self):
        """
        Use available social APIs for early signals.
        """
        # Twitter via bird CLI (assuming bird is installed and configured)
        # We can use subprocess to run bird commands and parse the output.
        # Example: bird search "'deploying on base' 'new token launch' 'test contract'"
        # We'll store the tweets that match our keywords.
        
        # Instagram via meta_client.py (if available)
        # We can use the Instagram Graph API to search for posts with specific hashtags or captions.
        
        # For now, we'll create a placeholder that logs and stores social signals.
        # We'll use a simple keyword list.
        keywords = ["deploying on base", "new token launch", "test contract"]
        
        # We'll simulate by just logging and storing a mock signal for now.
        # In a real implementation, we would call the APIs.
        for keyword in keywords:
            logger.info(f"Searching for keyword: {keyword}")
            # Mock signal
            signal_data = {
                'type': 'social_signal',
                'keyword': keyword,
                'content': f"Mock social post about {keyword}",
                'timestamp': time.time()
            }
            self.signals_collection.add(signal_data)
    
    def run(self):
        """
        Run all monitoring functions continuously.
        """
        logger.info("Starting Proximal Cause Detector")
        while True:
            try:
                self.monitor_factory_patterns()
                self.monitor_deployer_behavior()
                self.monitor_social_ignition()
                # Sleep for a while before next iteration
                time.sleep(60)  # Adjust as needed
            except Exception as e:
                logger.error(f"Error in ProximalCauseDetector: {e}")
                time.sleep(60)

if __name__ == "__main__":
    from config import WEB3_PROVIDER_URI
    detector = ProximalCauseDetector(WEB3_PROVIDER_URI)
    detector.run()
```

Now, let's create Layer 2: Adversarial Validator.

### FILE: layer2_adversarial_validator.py
```python
import logging
from firebase_setup import initialize_firebase
from config import VALIDATION_GATES
from typing import Dict, Any
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AdversarialValidator:
    """
    Runs candidate tokens through 7 validation gates.
    """
    
    def __init__(self):
        self.db = initialize_firebase()
        self.signals_collection = self.db.collection('signals')
        self.validated_tokens_collection = self.db.collection('validated_tokens')
        
    def wash_trade_detection(self, token_address: str) -> float:
        """
        Check for self-trading patterns.
        Returns a score from 0 to 1, where 1 is clean.
        """
        # Placeholder: in reality, we would analyze transaction graph for circular trading.
        # For now, we return a mock score.
        logger.info(f"Running wash trade detection for {token_address}")
        return 0.9
    
    def mev_vulnerability(self, token_address: str) -> float:
        """
        Simulate sandwich attack vulnerability.
        Returns a score from 0 to 1, where 1 is safe.
        """
        logger.info(f"Running MEV vulnerability check for {token_address}")
        return 0.8
    
    def lp_concentration_risk(self, token_address: str) -> float:
        """
        Analyze LP distribution.
        Returns a score from 0 to 1, where 1 is safe.
        """
        logger.info(f"Running LP concentration risk check for {token_address}")
        return 0.7
    
    def contract_red_flags(self, token_address: str) -> float:
        """
        Check for malicious functions in the contract.
        Returns a score from 0 to 1, where 1 is safe.
        """
        logger.info(f"Running contract red flags check for {token_address}")
        return 0.85
    
    def social_bot_analysis(self, token_address: str) -> float:
        """
        Analyze Twitter engagement quality.
        Returns a score from 0 to 1, where 1 is authentic.
        """
        logger.info(f"Running social bot analysis for {token_address}")
        return 0.75
    
    def deployer_reputation(self, token_address: str) -> float:
        """
        Check deployer history.
        Returns a score from 0 to 1, where 1 is reputable.
        """
        logger.info(f"Running deployer reputation check for {token_address}")
        return 0.6
    
    def time_series_anomaly(self, token_address: str) -> float:
        """
        Detect pump timing patterns.
        Returns a score from 0 to 1, where 1 is normal.
        """
        logger.info(f"Running time series anomaly detection for {token_address}")
        return 0.95
    
    def validate_token(self, token_address: str, signal_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the token through all validation gates and return a validation report.
        """
        logger.info(f"Validating token {token_address}")
        
        # Run each validation gate and collect scores
        scores = {}
        scores['wash_trade_detection'] = self.wash_trade_detection(token_address)
        scores['mev_vulnerability'] = self.mev_vulnerability(token_address)
        scores['lp_concentration_risk'] = self.lp_concentration_risk(token_address)
        scores['contract_red_flags'] = self.contract_red_flags(token_address)
        scores['social_bot_analysis'] = self.social_bot_analysis(token_address)
        scores['deployer_reputation'] = self.deployer_reputation(token_address)
        scores['time_series_anomaly'] = self.time_series_anomaly(token_address)
        
        # Calculate an overall score (simple average for now)
        overall_score = sum(scores.values()) / len(scores)
        
        # Prepare validation report
        report = {
            'token_address': token_address,
            'signal_data': signal_data,
            'validation_scores': scores,
            'overall_score': overall_score,
            'timestamp': time.time(),
            'passed': overall_score >= 0.85  # Example threshold
        }
        
        # Store the validation report in Firebase
        self.validated_tokens_collection.add(report)
        
        return report
    
    def run(self):
        """
        Continuously check for new signals and validate them.
        """
        logger.info("Starting Adversarial Validator")
        
        # We'll listen to the signals collection for new documents.
        # We can use a firestore listener or poll. For simplicity, we'll poll.
        
        while True:
            try:
                # Get all signals that haven't been validated yet.
                # We can add a field 'validated' to the signal document to track.
                # For now, we'll just get all signals and then check if they are in validated_tokens.
                signals = self.signals_collection.stream()
                validated_tokens = {doc.get('token_address') for doc in self.validated_tokens_collection.stream()}
                
                for signal in signals:
                    signal_data = signal.to_dict()
                    # Check if this signal is about a token and if it hasn't been validated.
                    token_address = signal_data.get('contract_address')
                    if token_address and token_address not in validated_tokens:
                        self.validate_token(token_address, signal_data)
                
                time.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                logger.error(f"Error in AdversarialValidator: {e}")
                time.sleep(30)

if __name__ == "__main__":
    validator = AdversarialValidator()
    validator.run()
```

Now, let's create Layer 3: Autonomous Executor.

### FILE: layer3_autonomous_executor.py
```python
import logging
import time
from web3 import Web3
from firebase_setup import initialize_firebase
from config import Constitution, WEB3_PROVIDER_URI
from typing import Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AutonomousExecutor:
    """
    Executes trades based on validated signals within constitutional limits.