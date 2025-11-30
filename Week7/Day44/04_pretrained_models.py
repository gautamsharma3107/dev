"""
Day 44 - Using Pre-trained Models
=================================
Learn: Fine-tuning, transfer learning, practical applications

Key Concepts:
- Load pre-trained models for specific tasks
- Fine-tune models on custom data
- Use models for real-world applications
"""

# ========== INTRODUCTION ==========
print("=" * 60)
print("USING PRE-TRAINED MODELS")
print("=" * 60)

introduction = """
Pre-trained models are the foundation of modern NLP!

Why Use Pre-trained Models?
1. Trained on massive datasets (billions of words)
2. Capture general language understanding
3. Transfer learning: Fine-tune for your specific task
4. State-of-the-art results with minimal data
5. Save time and compute resources

Common Use Cases:
- Sentiment analysis
- Text classification
- Named entity recognition
- Question answering
- Text generation
- Semantic similarity

Let's explore practical applications!
"""

print(introduction)

# ========== TEXT CLASSIFICATION ==========
print("\n" + "=" * 60)
print("TEXT CLASSIFICATION WITH PRE-TRAINED MODELS")
print("=" * 60)

classification_code = '''
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load pre-trained sentiment model
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def classify_sentiment(text):
    """Classify sentiment on 1-5 star scale."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    predictions = torch.softmax(outputs.logits, dim=1)
    predicted_class = torch.argmax(predictions).item() + 1  # 1-5 scale
    confidence = predictions[0][predicted_class-1].item()
    
    return predicted_class, confidence

# Test
reviews = [
    "This product is amazing! Best purchase ever!",
    "Terrible quality, complete waste of money.",
    "It's okay, nothing special but works fine."
]

for review in reviews:
    stars, conf = classify_sentiment(review)
    print(f"Review: {review}")
    print(f"Stars: {'⭐' * stars} ({conf:.2%} confidence)\\n")
'''

print("Code:")
print(classification_code)

# Run example
try:
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch
    
    print("\n--- Running Classification Example ---")
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    
    def classify_sentiment(text):
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        predictions = torch.softmax(outputs.logits, dim=1)
        predicted_class = torch.argmax(predictions).item() + 1
        confidence = predictions[0][predicted_class-1].item()
        return predicted_class, confidence
    
    reviews = [
        "This product is amazing!",
        "Terrible quality.",
        "It's okay."
    ]
    
    for review in reviews:
        stars, conf = classify_sentiment(review)
        print(f"'{review}' → {'⭐' * stars} ({conf:.2%})")
except Exception as e:
    print(f"\n(Skipping execution - {e})")

# ========== TEXT GENERATION ==========
print("\n" + "=" * 60)
print("TEXT GENERATION WITH GPT-2")
print("=" * 60)

generation_code = '''
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load GPT-2
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_text(prompt, max_length=100, temperature=0.7, top_p=0.9):
    """Generate text continuation."""
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate
    outputs = model.generate(
        inputs,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# Test different prompts
prompts = [
    "The future of artificial intelligence is",
    "Once upon a time in a magical forest",
    "Machine learning helps businesses by"
]

for prompt in prompts:
    result = generate_text(prompt, max_length=50)
    print(f"Prompt: {prompt}")
    print(f"Generated: {result}\\n")
'''

print("Code:")
print(generation_code)

# ========== QUESTION ANSWERING ==========
print("\n" + "=" * 60)
print("QUESTION ANSWERING")
print("=" * 60)

qa_code = '''
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Load QA model
model_name = "deepset/roberta-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

def answer_question(question, context):
    """Extract answer from context."""
    inputs = tokenizer(
        question, 
        context, 
        return_tensors="pt",
        truncation=True,
        max_length=512
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get answer span
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1
    
    answer_tokens = inputs["input_ids"][0][answer_start:answer_end]
    answer = tokenizer.decode(answer_tokens)
    
    return answer

# Test
context = """
Python is a high-level programming language created by Guido van Rossum 
in 1991. It emphasizes code readability and supports multiple programming 
paradigms including procedural, object-oriented, and functional programming. 
Python is widely used in web development, data science, machine learning, 
and automation.
"""

questions = [
    "Who created Python?",
    "When was Python created?",
    "What is Python used for?"
]

print(f"Context: {context[:100]}...")
print()
for q in questions:
    answer = answer_question(q, context)
    print(f"Q: {q}")
    print(f"A: {answer}\\n")
'''

print("Code:")
print(qa_code)

# ========== NAMED ENTITY RECOGNITION ==========
print("\n" + "=" * 60)
print("NAMED ENTITY RECOGNITION (NER)")
print("=" * 60)

ner_code = '''
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import torch

# Using pipeline for simplicity
ner_pipeline = pipeline(
    "ner",
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    grouped_entities=True
)

def extract_entities(text):
    """Extract named entities from text."""
    entities = ner_pipeline(text)
    
    result = {}
    for entity in entities:
        entity_type = entity['entity_group']
        word = entity['word']
        score = entity['score']
        
        if entity_type not in result:
            result[entity_type] = []
        result[entity_type].append((word, score))
    
    return result

# Test
texts = [
    "Apple Inc. CEO Tim Cook announced new products in San Francisco.",
    "President Biden met with Prime Minister Trudeau in Washington D.C.",
    "Tesla's Elon Musk visited the Gigafactory in Berlin, Germany."
]

for text in texts:
    print(f"Text: {text}")
    entities = extract_entities(text)
    for entity_type, items in entities.items():
        print(f"  {entity_type}: {[item[0] for item in items]}")
    print()
'''

print("Code:")
print(ner_code)

# ========== SEMANTIC SIMILARITY ==========
print("\n" + "=" * 60)
print("SEMANTIC SIMILARITY")
print("=" * 60)

similarity_code = '''
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

# Load sentence transformer model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def mean_pooling(model_output, attention_mask):
    """Pool token embeddings to get sentence embedding."""
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def get_embedding(text):
    """Get sentence embedding."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    embeddings = mean_pooling(outputs, inputs['attention_mask'])
    embeddings = F.normalize(embeddings, p=2, dim=1)
    
    return embeddings

def compute_similarity(text1, text2):
    """Compute cosine similarity between two texts."""
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    
    similarity = F.cosine_similarity(emb1, emb2).item()
    return similarity

# Test
pairs = [
    ("I love programming", "Coding is my passion"),
    ("The weather is nice today", "It's a beautiful sunny day"),
    ("I love programming", "The weather is nice today"),
]

print("Similarity scores:")
for text1, text2 in pairs:
    sim = compute_similarity(text1, text2)
    print(f"'{text1}' <-> '{text2}'")
    print(f"Similarity: {sim:.4f}\\n")
'''

print("Code:")
print(similarity_code)

# ========== FINE-TUNING BASICS ==========
print("\n" + "=" * 60)
print("FINE-TUNING PRE-TRAINED MODELS")
print("=" * 60)

finetuning_code = '''
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification,
    Trainer, 
    TrainingArguments
)
from datasets import load_dataset
import numpy as np
from sklearn.metrics import accuracy_score

# 1. Load dataset
dataset = load_dataset("imdb")
train_data = dataset["train"].shuffle(seed=42).select(range(1000))  # Small subset
test_data = dataset["test"].shuffle(seed=42).select(range(200))

# 2. Load tokenizer and model
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, 
    num_labels=2
)

# 3. Tokenize data
def tokenize_function(examples):
    return tokenizer(
        examples["text"], 
        padding="max_length", 
        truncation=True,
        max_length=256
    )

train_dataset = train_data.map(tokenize_function, batched=True)
test_dataset = test_data.map(tokenize_function, batched=True)

# 4. Define metrics
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return {"accuracy": accuracy_score(labels, predictions)}

# 5. Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_steps=100,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# 6. Create Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)

# 7. Train!
trainer.train()

# 8. Evaluate
results = trainer.evaluate()
print(f"Test Accuracy: {results['eval_accuracy']:.4f}")

# 9. Save the model
model.save_pretrained("./my_finetuned_model")
tokenizer.save_pretrained("./my_finetuned_model")
'''

print("Fine-tuning Code:")
print(finetuning_code)

# ========== INFERENCE OPTIMIZATION ==========
print("\n" + "=" * 60)
print("INFERENCE OPTIMIZATION TIPS")
print("=" * 60)

optimization_tips = """
Speed Up Inference:

1. USE BATCH PROCESSING
   # Instead of one at a time
   texts = ["text1", "text2", "text3"]
   inputs = tokenizer(texts, return_tensors="pt", padding=True)
   outputs = model(**inputs)

2. USE MIXED PRECISION (FP16)
   from transformers import pipeline
   pipe = pipeline("text-classification", torch_dtype=torch.float16)

3. USE ONNX RUNTIME
   from optimum.onnxruntime import ORTModelForSequenceClassification
   model = ORTModelForSequenceClassification.from_pretrained("model", export=True)

4. QUANTIZATION
   from transformers import AutoModelForSequenceClassification
   model = AutoModelForSequenceClassification.from_pretrained(
       "model",
       load_in_8bit=True  # Requires bitsandbytes
   )

5. USE SMALLER MODELS
   - DistilBERT: 40% smaller, 60% faster
   - TinyBERT: Even smaller
   - MobileBERT: Optimized for mobile

6. CACHING
   # Cache tokenized inputs for repeated inference
   tokenized_cache = {}
   def tokenize_cached(text):
       if text not in tokenized_cache:
           tokenized_cache[text] = tokenizer(text)
       return tokenized_cache[text]
"""

print(optimization_tips)

# ========== PRACTICAL PROJECT: DOCUMENT CLASSIFIER ==========
print("\n" + "=" * 60)
print("PRACTICAL PROJECT: DOCUMENT CLASSIFIER")
print("=" * 60)

classifier_project = '''
"""
Build a Document Classifier
"""
from transformers import pipeline
import json

class DocumentClassifier:
    def __init__(self):
        # Use zero-shot for flexibility
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        
        # Define categories
        self.categories = [
            "Technology",
            "Business",
            "Sports",
            "Entertainment",
            "Science",
            "Politics",
            "Health"
        ]
    
    def classify(self, text, threshold=0.3):
        """Classify document into categories."""
        result = self.classifier(text, self.categories)
        
        # Get top categories above threshold
        classifications = []
        for label, score in zip(result['labels'], result['scores']):
            if score > threshold:
                classifications.append({
                    "category": label,
                    "confidence": round(score, 4)
                })
        
        return classifications
    
    def batch_classify(self, documents):
        """Classify multiple documents."""
        results = []
        for doc in documents:
            classification = self.classify(doc)
            results.append({
                "text": doc[:100] + "...",
                "classifications": classification
            })
        return results

# Usage
classifier = DocumentClassifier()

documents = [
    "Apple announced the new iPhone 15 with advanced AI capabilities.",
    "The Lakers won the championship after an incredible playoff run.",
    "New study reveals breakthrough in cancer treatment research.",
    "Stock markets reached all-time highs amid economic recovery."
]

for doc in documents:
    result = classifier.classify(doc)
    print(f"Document: {doc[:50]}...")
    print(f"Categories: {result}\\n")
'''

print("Project Code:")
print(classifier_project)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

summary = """
Using Pre-trained Models:

1. CLASSIFICATION:
   model = AutoModelForSequenceClassification.from_pretrained(name)

2. GENERATION:
   model = GPT2LMHeadModel.from_pretrained("gpt2")
   model.generate(inputs, max_length=100, temperature=0.7)

3. QUESTION ANSWERING:
   model = AutoModelForQuestionAnswering.from_pretrained(name)

4. NER:
   pipeline("ner", grouped_entities=True)

5. SEMANTIC SIMILARITY:
   Use sentence-transformers for embeddings
   Compute cosine similarity

6. FINE-TUNING:
   - Load pre-trained model
   - Prepare dataset with tokenization
   - Use Trainer API
   - Save fine-tuned model

7. OPTIMIZATION:
   - Batch processing
   - Use smaller models (DistilBERT)
   - Mixed precision (FP16)
   - Quantization

Next: Build a chatbot/text generator project!
"""

print(summary)

print("\n" + "=" * 60)
print("✅ Pre-trained Models - Complete!")
print("=" * 60)
