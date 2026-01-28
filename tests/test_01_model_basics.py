"""
Tests for Exercise 01: Model Initialization & Basic Invocation
==============================================================
"""
import pytest
from unittest.mock import Mock, patch, MagicMock


class TestModelBasics:
    """Test Exercise 01: Model Initialization & Basic Invocation"""
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_initialize_model_returns_model_object(self):
        """Test that initialize_model returns a model object."""
        # TODO: Import initialize_model from src.exercises.01_model_basics
        # TODO: Call initialize_model()
        # TODO: Assert it returns a model object
        # TODO: Assert model has required methods (invoke, stream, batch)
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_invoke_model_with_prompt(self):
        """Test that invoke_model processes a prompt and returns string."""
        # TODO: Create mock model
        # TODO: Call invoke_model with prompt
        # TODO: Assert returns string response
        # TODO: Assert model.invoke was called
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_stream_model_yields_tokens(self):
        """Test that stream_model yields tokens one at a time."""
        # TODO: Create mock model
        # TODO: Call stream_model with prompt
        # TODO: Assert yields iterable of strings
        # TODO: Assert chunks can be concatenated into response
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_batch_model_processes_multiple_prompts(self):
        """Test that batch_model processes multiple prompts."""
        # TODO: Create mock model
        # TODO: Call batch_model with list of prompts
        # TODO: Assert returns list of responses
        # TODO: Assert length equals input length
        # TODO: Assert each response is string
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_batch_model_preserves_order(self):
        """Test that batch_model returns responses in input order."""
        # TODO: Create mock model with ordered responses
        # TODO: Call batch_model with specific prompts
        # TODO: Assert responses match input order
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_compare_model_parameters_with_different_temperatures(self):
        """Test comparing outputs with different temperature values."""
        # TODO: Create mock model
        # TODO: Call compare_model_parameters with temperatures
        # TODO: Assert returns list of responses
        # TODO: Assert same length as temperature list
        pass
    
    @pytest.mark.beginner
    @pytest.mark.integration
    def test_invoke_stream_batch_consistency(self):
        """Test that invoke, stream, and batch produce consistent results."""
        # TODO: Create mock model
        # TODO: Get response from invoke
        # TODO: Get response from streaming and concatenate
        # TODO: Get response from batch
        # TODO: Assert all three produce similar output
        pass
