# test_echoveil.py
"""
Tests for EchoVeil module.
"""

import unittest
from echoveil import EchoVeil

class TestEchoVeil(unittest.TestCase):
    """Test cases for EchoVeil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EchoVeil()
        self.assertIsInstance(instance, EchoVeil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EchoVeil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
