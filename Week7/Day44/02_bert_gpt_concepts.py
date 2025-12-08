"""
Day 44 - BERT and GPT Concepts
==============================
Learn: BERT architecture, GPT architecture, key differences

Key Concepts:
- BERT: Bidirectional understanding, great for classification
- GPT: Unidirectional generation, great for text generation
- Both revolutionized NLP in different ways
"""

# ========== BERT OVERVIEW ==========
print("=" * 60)
print("BERT - Bidirectional Encoder Representations from Transformers")
print("=" * 60)

bert_introduction = """
BERT (2018) by Google changed NLP forever!

KEY CHARACTERISTICS:
1. Bidirectional: Reads text in both directions simultaneously
2. Encoder-only: Uses only the transformer encoder
3. Pre-training: Masked Language Model (MLM) + Next Sentence Prediction
4. Fine-tuning: Add simple output layer for downstream tasks

Architecture:
- BERT-base: 12 layers, 768 hidden, 12 heads, 110M parameters
- BERT-large: 24 layers, 1024 hidden, 16 heads, 340M parameters

Why Bidirectional Matters:
- Sentence: "The bank can guarantee deposits will be safe."
- "bank" meaning depends on context from BOTH sides
- BERT sees entire sentence when understanding each word
"""

print(bert_introduction)

# ========== BERT PRE-TRAINING ==========
print("\n" + "=" * 60)
print("BERT PRE-TRAINING TASKS")
print("=" * 60)

bert_pretraining = """
1. MASKED LANGUAGE MODELING (MLM)
   - Randomly mask 15% of tokens
   - Model predicts the original tokens
   
   Example:
   Input:  "The [MASK] sat on the [MASK]"
   Labels: "The cat sat on the mat"
   
   Masking strategy for 15% tokens:
   - 80%: Replace with [MASK]
   - 10%: Replace with random word
   - 10%: Keep original word
   
2. NEXT SENTENCE PREDICTION (NSP)
   - Given sentence A, is sentence B the next sentence?
   - Binary classification: IsNext / NotNext
   
   Example:
   [CLS] I went to the store [SEP] I bought some milk [SEP]
   Label: IsNext
   
   [CLS] I went to the store [SEP] The weather is nice [SEP]
   Label: NotNext
"""

print(bert_pretraining)

# ========== BERT INPUT FORMAT ==========
print("\n" + "=" * 60)
print("BERT INPUT FORMAT")
print("=" * 60)

def demonstrate_bert_input():
    """Show how BERT formats its input."""
    
    sentence1 = "Hello, how are you?"
    sentence2 = "I am doing great!"
    
    # BERT uses special tokens
    cls_token = "[CLS]"  # Classification token
    sep_token = "[SEP]"  # Separator token
    
    # Format for single sentence
    single_input = f"{cls_token} {sentence1} {sep_token}"
    
    # Format for sentence pair
    pair_input = f"{cls_token} {sentence1} {sep_token} {sentence2} {sep_token}"
    
    print("BERT Input Formatting:")
    print("-" * 40)
    print(f"Single sentence: {single_input}")
    print(f"\nSentence pair: {pair_input}")
    
    # Token type IDs (segment embeddings)
    print("\nToken Type IDs (Segment Embeddings):")
    print("Sentence A tokens: 0")
    print("Sentence B tokens: 1")
    
    # Example token type IDs
    print("\nExample:")
    print("[CLS]=0, Hello=0, how=0, are=0, you=0, ?=0, [SEP]=0")
    print("I=1, am=1, doing=1, great=1, !=1, [SEP]=1")

demonstrate_bert_input()

# ========== BERT FOR DOWNSTREAM TASKS ==========
print("\n" + "=" * 60)
print("BERT FOR DOWNSTREAM TASKS")
print("=" * 60)

bert_tasks = """
BERT can be fine-tuned for many tasks:

1. SENTIMENT CLASSIFICATION
   - Use [CLS] token representation
   - Add classification layer on top
   - Fine-tune on labeled data
   
   [CLS] This movie was great! [SEP] → Positive

2. NAMED ENTITY RECOGNITION (NER)
   - Use all token representations
   - Classify each token
   
   [Barack] [Obama] [visited] [Paris]
    PERSON   PERSON    O      LOCATION

3. QUESTION ANSWERING
   - Input: [CLS] Question [SEP] Context [SEP]
   - Predict start and end positions of answer
   
   Q: "What is the capital of France?"
   Context: "Paris is the capital of France."
   Answer: "Paris" (positions 0-1)

4. TEXT SIMILARITY
   - Compare [CLS] representations
   - Or use cosine similarity

5. TEXT GENERATION (Not BERT's strength)
   - BERT is not designed for generation
   - Use GPT for generation tasks
"""

print(bert_tasks)

# ========== GPT OVERVIEW ==========
print("\n" + "=" * 60)
print("GPT - Generative Pre-trained Transformer")
print("=" * 60)

gpt_introduction = """
GPT (2018-2023) by OpenAI - Master of Text Generation

KEY CHARACTERISTICS:
1. Unidirectional: Reads text left-to-right only
2. Decoder-only: Uses only transformer decoder
3. Pre-training: Causal Language Modeling (next token prediction)
4. Few-shot/Zero-shot: Can perform tasks with minimal examples

Evolution:
- GPT-1 (2018): 117M parameters
- GPT-2 (2019): 1.5B parameters
- GPT-3 (2020): 175B parameters
- GPT-4 (2023): Multimodal, ~1.7T parameters (estimated)

Why Left-to-Right:
- Natural for text generation
- Generate one token at a time
- Each token depends on previous tokens
"""

print(gpt_introduction)

# ========== GPT PRE-TRAINING ==========
print("\n" + "=" * 60)
print("GPT PRE-TRAINING")
print("=" * 60)

gpt_pretraining = """
CAUSAL LANGUAGE MODELING:
- Predict the next token given all previous tokens
- Simple but powerful objective

Example:
Input:  "The cat sat on the"
Target: "mat"

Training Process:
Input:    [The] [cat] [sat] [on]  [the]
Predict:  [cat] [sat] [on]  [the] [mat]

Each position predicts the next token.
Loss is computed for all positions simultaneously.

Key Insight:
- This simple objective scales incredibly well
- More data + more parameters = better performance
- Emergent abilities appear at scale
"""

print(gpt_pretraining)

# ========== GPT GENERATION DEMO ==========
print("\n" + "=" * 60)
print("HOW GPT GENERATES TEXT")
print("=" * 60)

def simple_generation_demo():
    """
    Demonstrate the text generation process.
    (Simplified - real GPT uses neural networks)
    """
    import random
    
    # Simple vocabulary with probabilities
    vocab = {
        "The": {"cat": 0.4, "dog": 0.3, "bird": 0.2, "fish": 0.1},
        "cat": {"sat": 0.5, "slept": 0.3, "ran": 0.2},
        "dog": {"barked": 0.4, "ran": 0.3, "slept": 0.3},
        "sat": {"on": 0.7, "near": 0.3},
        "on": {"the": 0.8, "a": 0.2},
        "the": {"mat": 0.5, "floor": 0.3, "bed": 0.2},
    }
    
    def generate_next(word, vocab):
        """Generate next word based on simple probabilities."""
        if word in vocab:
            words = list(vocab[word].keys())
            probs = list(vocab[word].values())
            return random.choices(words, probs)[0]
        return None
    
    print("Simple text generation demo:")
    print("-" * 40)
    
    # Generate a sequence
    generated = ["The"]
    for _ in range(5):
        current = generated[-1]
        next_word = generate_next(current, vocab)
        if next_word:
            generated.append(next_word)
        else:
            break
    
    print(f"Generated: {' '.join(generated)}")
    
    print("\nGeneration Process:")
    print("1. Start with: 'The'")
    print("2. Predict next token based on probabilities")
    print("3. Sample from distribution (or take most likely)")
    print("4. Repeat until done")

simple_generation_demo()

# ========== DECODING STRATEGIES ==========
print("\n" + "=" * 60)
print("GPT DECODING STRATEGIES")
print("=" * 60)

decoding_strategies = """
How to select the next token:

1. GREEDY DECODING
   - Always pick highest probability token
   - Fast but can be repetitive
   - P(next) = argmax P(token|context)

2. BEAM SEARCH
   - Keep top k sequences at each step
   - Good for translation/summarization
   - More likely to find optimal sequence

3. TEMPERATURE SAMPLING
   - Higher temp = more random/creative
   - Lower temp = more deterministic
   - P_new = softmax(logits / temperature)
   
   Example:
   - temp=0.1: Very focused, repetitive
   - temp=1.0: Balanced
   - temp=2.0: Very creative, may be incoherent

4. TOP-K SAMPLING
   - Only consider top k most likely tokens
   - Then sample from those
   - k=50 is common

5. TOP-P (NUCLEUS) SAMPLING
   - Consider smallest set where prob sum > p
   - More dynamic than top-k
   - p=0.9 is common

Best Practice:
- Use temperature + top-p together
- temp=0.7, top_p=0.9 often works well
"""

print(decoding_strategies)

# ========== BERT vs GPT COMPARISON ==========
print("\n" + "=" * 60)
print("BERT vs GPT COMPARISON")
print("=" * 60)

comparison = """
                    BERT                    GPT
                    ----                    ---
Architecture:       Encoder-only            Decoder-only
Direction:          Bidirectional           Left-to-right
Pre-training:       MLM + NSP               Causal LM
Best for:           Understanding           Generation
Fine-tuning:        Task-specific head      Few-shot prompting

USE BERT FOR:
✅ Sentiment analysis
✅ Named entity recognition
✅ Question answering (extractive)
✅ Text classification
✅ Similarity/matching

USE GPT FOR:
✅ Text generation
✅ Creative writing
✅ Chatbots
✅ Code generation
✅ Translation
✅ Few-shot learning

HYBRID APPROACHES:
- T5: Text-to-text format, encoder-decoder
- BART: Denoising autoencoder, encoder-decoder
- UniLM: Can do both understanding and generation
"""

print(comparison)

# ========== MODERN VARIATIONS ==========
print("\n" + "=" * 60)
print("MODERN BERT & GPT VARIATIONS")
print("=" * 60)

variations = """
BERT FAMILY:
- RoBERTa: Better training, removes NSP
- ALBERT: Parameter sharing, efficient
- DistilBERT: Smaller, faster, 97% performance
- ELECTRA: Replaced token detection, efficient
- DeBERTa: Disentangled attention, strong performance

GPT FAMILY:
- GPT-2: Open-source, 1.5B params
- GPT-3: API access, few-shot learning
- InstructGPT: RLHF for better following instructions
- ChatGPT: Conversational fine-tuning
- GPT-4: Multimodal, most capable

OPEN ALTERNATIVES:
- LLaMA/LLaMA 2: Meta's open models
- Falcon: Strong open model
- Mistral: Efficient open model
- MPT: MosaicML's models
- Phi: Microsoft's small but capable models
"""

print(variations)

# ========== PRACTICAL CONSIDERATIONS ==========
print("\n" + "=" * 60)
print("PRACTICAL CONSIDERATIONS")
print("=" * 60)

practical = """
CHOOSING THE RIGHT MODEL:

1. Task Type:
   - Classification/NER → BERT-style
   - Generation → GPT-style
   - Translation → Encoder-decoder (T5)

2. Resource Constraints:
   - Limited GPU → DistilBERT, GPT-2 small
   - Cloud API → GPT-3.5/4
   - On-device → TinyBERT, MobileBERT

3. Domain:
   - Biomedical → BioBERT, PubMedBERT
   - Legal → LegalBERT
   - Code → CodeBERT, Codex
   - Finance → FinBERT

4. Language:
   - Multilingual → mBERT, XLM-RoBERTa
   - Specific language → Language-specific BERT

FINE-TUNING TIPS:
- Start with smaller learning rate (2e-5 to 5e-5)
- Train for 3-5 epochs typically
- Use warmup scheduler
- Monitor validation loss for early stopping
"""

print(practical)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

summary = """
BERT:
✅ Bidirectional understanding
✅ MLM + NSP pre-training
✅ Best for classification, NER, Q&A
✅ [CLS] token for sentence representation
✅ Fine-tune for specific tasks

GPT:
✅ Autoregressive generation
✅ Left-to-right, causal attention
✅ Best for text generation
✅ Few-shot learning capability
✅ Prompt engineering for tasks

When to Use What:
- Need to understand text → BERT
- Need to generate text → GPT
- Need both → T5/BART or use both models

Next: Learn to use Hugging Face transformers library!
"""

print(summary)

print("\n" + "=" * 60)
print("✅ BERT and GPT Concepts - Complete!")
print("=" * 60)
