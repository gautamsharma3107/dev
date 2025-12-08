"""
Day 44 - Hugging Face Transformers Basics
=========================================
Learn: Installing transformers, loading models, pipelines

Key Concepts:
- Hugging Face is the GitHub of ML
- Transformers library makes using models easy
- Pipelines provide simple APIs for common tasks
"""

# ========== INTRODUCTION ==========
print("=" * 60)
print("HUGGING FACE TRANSFORMERS LIBRARY")
print("=" * 60)

introduction = """
Hugging Face 🤗 - The AI Community Hub

What is Hugging Face?
- Platform for sharing ML models, datasets, and spaces
- Transformers library: Easy-to-use interface for NLP models
- 200,000+ models available
- Support for PyTorch, TensorFlow, and JAX

Key Libraries:
1. transformers - Main library for using pre-trained models
2. datasets - Load and process datasets easily
3. tokenizers - Fast tokenization
4. accelerate - Distributed training
5. peft - Parameter-efficient fine-tuning

Installation:
pip install transformers torch
pip install datasets accelerate

Let's get started!
"""

print(introduction)

# ========== IMPORT CHECK ==========
print("\n" + "=" * 60)
print("CHECKING INSTALLATION")
print("=" * 60)

try:
    import transformers
    print(f"✅ Transformers version: {transformers.__version__}")
except ImportError:
    print("❌ Transformers not installed. Run: pip install transformers")

try:
    import torch
    print(f"✅ PyTorch version: {torch.__version__}")
    print(f"   CUDA available: {torch.cuda.is_available()}")
except ImportError:
    print("❌ PyTorch not installed. Run: pip install torch")

# ========== PIPELINES - THE EASIEST WAY ==========
print("\n" + "=" * 60)
print("PIPELINES - SIMPLE API FOR COMMON TASKS")
print("=" * 60)

pipelines_intro = """
Pipelines are the easiest way to use pre-trained models!

Available pipelines:
- sentiment-analysis: Classify sentiment
- text-classification: General text classification
- ner: Named Entity Recognition
- question-answering: Answer questions from context
- fill-mask: Fill in masked words
- text-generation: Generate text
- translation: Translate between languages
- summarization: Summarize long text
- zero-shot-classification: Classify without training
"""

print(pipelines_intro)

# ========== SENTIMENT ANALYSIS PIPELINE ==========
print("\n" + "=" * 60)
print("EXAMPLE: SENTIMENT ANALYSIS")
print("=" * 60)

sentiment_code = '''
from transformers import pipeline

# Create sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze sentiment
texts = [
    "I love this product! It's amazing!",
    "This is the worst experience ever.",
    "The movie was okay, nothing special."
]

for text in texts:
    result = sentiment_analyzer(text)
    print(f"Text: {text}")
    print(f"Result: {result[0]}")
    print()
'''

print("Code:")
print(sentiment_code)

# Run if transformers is available
try:
    from transformers import pipeline
    
    print("\n--- Running Sentiment Analysis ---")
    sentiment_analyzer = pipeline("sentiment-analysis")
    
    texts = [
        "I love this product! It's amazing!",
        "This is the worst experience ever.",
        "The movie was okay, nothing special."
    ]
    
    for text in texts:
        result = sentiment_analyzer(text)
        print(f"Text: {text}")
        print(f"Result: {result[0]}")
        print()
except Exception as e:
    print(f"\n(Skipping execution - {e})")
    print("Install transformers to run this example.")

# ========== TEXT GENERATION PIPELINE ==========
print("\n" + "=" * 60)
print("EXAMPLE: TEXT GENERATION")
print("=" * 60)

generation_code = '''
from transformers import pipeline

# Create text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Generate text
prompt = "Once upon a time in a land far away"
result = generator(
    prompt,
    max_length=50,
    num_return_sequences=2,
    temperature=0.7
)

for i, seq in enumerate(result):
    print(f"Generated {i+1}: {seq['generated_text']}")
'''

print("Code:")
print(generation_code)

# ========== FILL-MASK PIPELINE ==========
print("\n" + "=" * 60)
print("EXAMPLE: FILL-MASK (BERT-style)")
print("=" * 60)

fillmask_code = '''
from transformers import pipeline

# Create fill-mask pipeline (uses BERT by default)
fill_mask = pipeline("fill-mask")

# Fill in the blank
text = "Paris is the [MASK] of France."
results = fill_mask(text)

for result in results[:3]:
    print(f"Token: {result['token_str']}, Score: {result['score']:.4f}")
'''

print("Code:")
print(fillmask_code)

# Run if available
try:
    from transformers import pipeline
    
    print("\n--- Running Fill-Mask ---")
    fill_mask = pipeline("fill-mask")
    text = "Paris is the [MASK] of France."
    results = fill_mask(text)
    
    print(f"Text: {text}")
    print("Predictions:")
    for result in results[:3]:
        print(f"  '{result['token_str']}' - Score: {result['score']:.4f}")
except Exception as e:
    print(f"\n(Skipping execution - {e})")

# ========== QUESTION ANSWERING ==========
print("\n" + "=" * 60)
print("EXAMPLE: QUESTION ANSWERING")
print("=" * 60)

qa_code = '''
from transformers import pipeline

# Create QA pipeline
qa_pipeline = pipeline("question-answering")

context = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars 
in Paris, France. It is named after the engineer Gustave Eiffel, whose 
company designed and built the tower. It was constructed from 1887 to 1889.
"""

questions = [
    "Where is the Eiffel Tower located?",
    "Who designed the Eiffel Tower?",
    "When was it built?"
]

for question in questions:
    result = qa_pipeline(question=question, context=context)
    print(f"Q: {question}")
    print(f"A: {result['answer']} (score: {result['score']:.4f})")
    print()
'''

print("Code:")
print(qa_code)

# ========== ZERO-SHOT CLASSIFICATION ==========
print("\n" + "=" * 60)
print("EXAMPLE: ZERO-SHOT CLASSIFICATION")
print("=" * 60)

zeroshot_code = '''
from transformers import pipeline

# Create zero-shot classifier
classifier = pipeline("zero-shot-classification")

# Classify without training!
text = "I need to book a flight to New York next week"
candidate_labels = ["travel", "cooking", "sports", "technology"]

result = classifier(text, candidate_labels)
print(f"Text: {text}")
print("Classifications:")
for label, score in zip(result['labels'], result['scores']):
    print(f"  {label}: {score:.4f}")
'''

print("Code:")
print(zeroshot_code)

# ========== NAMED ENTITY RECOGNITION ==========
print("\n" + "=" * 60)
print("EXAMPLE: NAMED ENTITY RECOGNITION")
print("=" * 60)

ner_code = '''
from transformers import pipeline

# Create NER pipeline
ner = pipeline("ner", grouped_entities=True)

# Extract entities
text = "Apple Inc. was founded by Steve Jobs in California."
entities = ner(text)

print(f"Text: {text}")
print("Entities found:")
for entity in entities:
    print(f"  {entity['word']}: {entity['entity_group']} ({entity['score']:.4f})")
'''

print("Code:")
print(ner_code)

# ========== SUMMARIZATION ==========
print("\n" + "=" * 60)
print("EXAMPLE: SUMMARIZATION")
print("=" * 60)

summarization_code = '''
from transformers import pipeline

# Create summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

article = """
    The Amazon rainforest is the world's largest tropical rainforest, 
    covering over 5.5 million square kilometers. It is home to more 
    than 10% of all species on Earth, including countless plants, 
    animals, and insects. The rainforest plays a crucial role in 
    regulating the global climate by absorbing carbon dioxide and 
    releasing oxygen. However, deforestation poses a significant 
    threat to this vital ecosystem, with thousands of square 
    kilometers being destroyed each year.
"""

summary = summarizer(article, max_length=50, min_length=20, do_sample=False)
print("Original length:", len(article.split()))
print("Summary:", summary[0]['summary_text'])
'''

print("Code:")
print(summarization_code)

# ========== LOADING SPECIFIC MODELS ==========
print("\n" + "=" * 60)
print("LOADING SPECIFIC MODELS")
print("=" * 60)

loading_models = '''
from transformers import AutoModel, AutoTokenizer

# Load any model by name
model_name = "bert-base-uncased"

# Load tokenizer and model separately
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Tokenize text
text = "Hello, how are you?"
inputs = tokenizer(text, return_tensors="pt")
print(f"Input IDs: {inputs['input_ids']}")

# Get model outputs
outputs = model(**inputs)
print(f"Output shape: {outputs.last_hidden_state.shape}")
# Shape: (batch_size, sequence_length, hidden_size)
'''

print("Code:")
print(loading_models)

# ========== TOKENIZATION DETAILS ==========
print("\n" + "=" * 60)
print("TOKENIZATION DEEP DIVE")
print("=" * 60)

tokenization_code = '''
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Hello, I'm learning NLP with Transformers!"

# Basic tokenization
tokens = tokenizer.tokenize(text)
print(f"Tokens: {tokens}")

# Convert to IDs
ids = tokenizer.convert_tokens_to_ids(tokens)
print(f"Token IDs: {ids}")

# Full encoding (includes special tokens)
encoding = tokenizer(
    text,
    padding=True,
    truncation=True,
    max_length=128,
    return_tensors="pt"  # or "tf" for TensorFlow
)

print(f"Input IDs: {encoding['input_ids']}")
print(f"Attention Mask: {encoding['attention_mask']}")

# Decode back to text
decoded = tokenizer.decode(encoding['input_ids'][0])
print(f"Decoded: {decoded}")
'''

print("Code:")
print(tokenization_code)

# Run tokenization example
try:
    from transformers import AutoTokenizer
    
    print("\n--- Running Tokenization Example ---")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    
    text = "Hello, I'm learning NLP with Transformers!"
    
    tokens = tokenizer.tokenize(text)
    print(f"Original: {text}")
    print(f"Tokens: {tokens}")
    
    encoding = tokenizer(text, return_tensors="pt")
    print(f"Token IDs: {encoding['input_ids'].tolist()[0]}")
    
    decoded = tokenizer.decode(encoding['input_ids'][0])
    print(f"Decoded: {decoded}")
except Exception as e:
    print(f"\n(Skipping execution - {e})")

# ========== MODEL CONFIGURATION ==========
print("\n" + "=" * 60)
print("MODEL CONFIGURATION")
print("=" * 60)

config_code = '''
from transformers import AutoConfig

# Load model configuration
config = AutoConfig.from_pretrained("bert-base-uncased")

print(f"Hidden size: {config.hidden_size}")
print(f"Number of layers: {config.num_hidden_layers}")
print(f"Number of heads: {config.num_attention_heads}")
print(f"Vocab size: {config.vocab_size}")
print(f"Max position: {config.max_position_embeddings}")

# You can also modify config for custom models
custom_config = AutoConfig.from_pretrained(
    "bert-base-uncased",
    num_hidden_layers=6,  # Smaller model
    hidden_size=512
)
'''

print("Code:")
print(config_code)

# ========== POPULAR MODEL NAMES ==========
print("\n" + "=" * 60)
print("POPULAR MODEL NAMES")
print("=" * 60)

models_list = """
BERT Models:
- bert-base-uncased
- bert-large-uncased
- bert-base-cased
- distilbert-base-uncased

GPT Models:
- gpt2
- gpt2-medium
- gpt2-large
- gpt2-xl

Sentiment/Classification:
- nlptown/bert-base-multilingual-uncased-sentiment
- cardiffnlp/twitter-roberta-base-sentiment

Question Answering:
- deepset/roberta-base-squad2
- distilbert-base-uncased-distilled-squad

Summarization:
- facebook/bart-large-cnn
- t5-small, t5-base, t5-large

Translation:
- Helsinki-NLP/opus-mt-en-de (English to German)
- Helsinki-NLP/opus-mt-en-fr (English to French)

Zero-shot:
- facebook/bart-large-mnli
- MoritzLaworthy/bart-large-mnli

Code:
- microsoft/codebert-base
- Salesforce/codegen-350M-mono
"""

print(models_list)

# ========== SAVING AND LOADING MODELS ==========
print("\n" + "=" * 60)
print("SAVING AND LOADING MODELS")
print("=" * 60)

save_load_code = '''
from transformers import AutoModel, AutoTokenizer

# Load a model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Save to local directory
save_path = "./my_bert_model"
tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

# Load from local directory
loaded_tokenizer = AutoTokenizer.from_pretrained(save_path)
loaded_model = AutoModel.from_pretrained(save_path)

print("Model saved and loaded successfully!")
'''

print("Code:")
print(save_load_code)

# ========== GPU USAGE ==========
print("\n" + "=" * 60)
print("USING GPU")
print("=" * 60)

gpu_code = '''
import torch
from transformers import AutoModel, AutoTokenizer

# Check GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load model to GPU
model = AutoModel.from_pretrained("bert-base-uncased").to(device)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Ensure inputs are on GPU
text = "Hello, world!"
inputs = tokenizer(text, return_tensors="pt").to(device)

# Forward pass on GPU
with torch.no_grad():
    outputs = model(**inputs)

print(f"Output device: {outputs.last_hidden_state.device}")

# For pipelines, specify device
from transformers import pipeline
pipe = pipeline("sentiment-analysis", device=0)  # GPU 0
# or device=-1 for CPU
'''

print("Code:")
print(gpu_code)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

summary = """
Hugging Face Transformers Quick Reference:

1. PIPELINES (Easiest):
   pipeline("sentiment-analysis")
   pipeline("text-generation", model="gpt2")
   pipeline("question-answering")
   pipeline("ner")
   pipeline("summarization")

2. LOADING MODELS:
   AutoTokenizer.from_pretrained("bert-base-uncased")
   AutoModel.from_pretrained("bert-base-uncased")

3. TOKENIZATION:
   inputs = tokenizer(text, return_tensors="pt")
   outputs = model(**inputs)

4. POPULAR MODELS:
   - BERT: bert-base-uncased
   - GPT-2: gpt2, gpt2-medium
   - T5: t5-small, t5-base

5. SAVE/LOAD:
   model.save_pretrained("./path")
   model = AutoModel.from_pretrained("./path")

Next: Learn to use pre-trained models for specific tasks!
"""

print(summary)

print("\n" + "=" * 60)
print("✅ Hugging Face Basics - Complete!")
print("=" * 60)
