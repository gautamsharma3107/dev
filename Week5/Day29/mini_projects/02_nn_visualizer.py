"""
MINI PROJECT 2: Neural Network Visualizer
==========================================
Create functions to visualize neural network architecture

Requirements:
1. Function to display network architecture as ASCII art
2. Show connections between layers
3. Display number of parameters per layer
4. Show activation functions used
5. Calculate and display total parameters
"""

import numpy as np

# Your code here
print("=" * 50)
print("NEURAL NETWORK VISUALIZER")
print("=" * 50)

# TODO: Implement visualization functions

def visualize_network(layer_sizes, activations):
    """
    Visualize a neural network architecture
    
    Parameters:
    - layer_sizes: list of integers [input, hidden1, ..., output]
    - activations: list of activation names for each layer
    
    Example:
    visualize_network([3, 4, 2], ['relu', 'sigmoid'])
    """
    pass


def count_parameters(layer_sizes):
    """
    Count total trainable parameters
    Returns: dict with weights, biases, and total
    """
    pass


def print_layer_info(layer_sizes, activations):
    """
    Print detailed information about each layer
    """
    pass


# Test with sample networks
# TODO: Test with various architectures:
# 1. Simple: [2, 3, 1]
# 2. Medium: [784, 128, 64, 10] (like MNIST)
# 3. Deep: [100, 64, 32, 16, 8, 4, 1]
