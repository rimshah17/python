from typing import Dict, Optional
import time
from dataclasses import dataclass
from config import config

@dataclass
class AuthAttempt:
    count: int = 0
    lockout_time: float = 0

class AuthenticationManager:
    def __init__(self):
        self._failed_attempts: Dict[str, AuthAttempt] = {}
    
    def reset_attempts(self, username: str) -> None:
        """Reset failed attempts for a user."""
        self._failed_attempts[username] = AuthAttempt()
    
    def increment_attempts(self, username: str) -> None:
        """Increment failed attempts and set lockout if needed."""
        if username not in self._failed_attempts:
            self._failed_attempts[username] = AuthAttempt()
        
        self._failed_attempts[username].count += 1
        if self._failed_attempts[username].count >= config.MAX_ATTEMPTS:
            self._failed_attempts[username].lockout_time = time.time() + config.LOCKOUT_TIME
    
    def is_locked(self, username: str) -> bool:
        """Check if a user is locked out."""
        if username not in self._failed_attempts:
            return False
        
        attempt = self._failed_attempts[username]
        if attempt.lockout_time > time.time():
            return True
        
        # Reset after lockout expires
        if attempt.count >= config.MAX_ATTEMPTS:
            self.reset_attempts(username)
        return False
    
    def get_attempts(self, username: str) -> int:
        """Get the number of failed attempts for a user."""
        return self._failed_attempts.get(username, AuthAttempt()).count
    
    def get_lockout_remaining(self, username: str) -> Optional[int]:
        """Get remaining lockout time in seconds."""
        if username not in self._failed_attempts:
            return None
        
        remaining = int(self._failed_attempts[username].lockout_time - time.time())
        return max(0, remaining) if remaining > 0 else None

# Create a global instance
auth_manager = AuthenticationManager()
