"""
Utility Functions
Common utility functions for data engineering tasks
"""

import logging
from typing import Any, List, Dict

logger = logging.getLogger(__name__)


def validate_data(data: List[Dict[str, Any]]) -> bool:
    """
    Validate data structure and content
    
    Args:
        data: List of data dictionaries to validate
        
    Returns:
        Boolean indicating validation status
    """
    if not data:
        logger.warning("Empty data provided")
        return False
    
    return True


def transform_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Transform raw data to processed format
    
    Args:
        data: Raw data to transform
        
    Returns:
        Transformed data
    """
    logger.info("Transforming data")
    return data


def load_data(data: List[Dict[str, Any]], destination: str) -> bool:
    """
    Load data to specified destination
    
    Args:
        data: Data to load
        destination: Target destination
        
    Returns:
        Boolean indicating success
    """
    logger.info(f"Loading data to {destination}")
    return True
