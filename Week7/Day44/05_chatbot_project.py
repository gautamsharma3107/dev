"""
Day 44 - Chatbot/Text Generator Project
========================================
Learn: Build a simple chatbot using transformers

Key Concepts:
- Conversational AI basics
- Using DialoGPT for conversations
- Building a simple chatbot interface
- Text generation with context
"""

# ========== PROJECT INTRODUCTION ==========
print("=" * 60)
print("🤖 CHATBOT / TEXT GENERATOR PROJECT")
print("=" * 60)

introduction = """
In this project, we'll build:
1. A simple conversation-based chatbot
2. A creative text generator
3. A question-answering assistant

These demonstrate practical NLP applications!

Prerequisites:
- pip install transformers torch
"""

print(introduction)

# ========== SIMPLE CHATBOT WITH DIALOGPT ==========
print("\n" + "=" * 60)
print("PROJECT 1: CONVERSATIONAL CHATBOT")
print("=" * 60)

chatbot_code = '''
"""
Simple Chatbot using DialoGPT
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class SimpleChatbot:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):
        """Initialize the chatbot with DialoGPT model."""
        print("Loading chatbot model... This may take a moment.")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history_ids = None
        print("Chatbot ready!")
    
    def respond(self, user_input):
        """Generate a response to user input."""
        # Encode user input
        new_input_ids = self.tokenizer.encode(
            user_input + self.tokenizer.eos_token,
            return_tensors='pt'
        )
        
        # Append to chat history
        if self.chat_history_ids is not None:
            bot_input_ids = torch.cat([self.chat_history_ids, new_input_ids], dim=-1)
        else:
            bot_input_ids = new_input_ids
        
        # Generate response
        self.chat_history_ids = self.model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
        
        # Decode response
        response = self.tokenizer.decode(
            self.chat_history_ids[:, bot_input_ids.shape[-1]:][0],
            skip_special_tokens=True
        )
        
        return response
    
    def reset_conversation(self):
        """Reset the conversation history."""
        self.chat_history_ids = None
        print("Conversation reset!")
    
    def chat(self):
        """Run interactive chat session."""
        print("\\n" + "=" * 40)
        print("Chat started! Type 'quit' to exit, 'reset' to start over.")
        print("=" * 40)
        
        while True:
            user_input = input("\\nYou: ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'reset':
                self.reset_conversation()
                continue
            elif not user_input:
                continue
            
            response = self.respond(user_input)
            print(f"Bot: {response}")

# Example usage
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    
    # Demo conversation
    demo_messages = [
        "Hi there! How are you today?",
        "What do you like to do for fun?",
        "That sounds interesting! Tell me more."
    ]
    
    print("\\n--- Demo Conversation ---")
    for msg in demo_messages:
        print(f"\\nYou: {msg}")
        response = chatbot.respond(msg)
        print(f"Bot: {response}")
'''

print("Chatbot Code:")
print(chatbot_code)

# ========== CREATIVE TEXT GENERATOR ==========
print("\n" + "=" * 60)
print("PROJECT 2: CREATIVE TEXT GENERATOR")
print("=" * 60)

generator_code = '''
"""
Creative Text Generator
Generate stories, poems, and creative content
"""
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class CreativeWriter:
    def __init__(self, model_name="gpt2-medium"):
        """Initialize the creative writer."""
        print("Loading creative writing model...")
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.model.eval()
        print("Writer ready!")
    
    def generate(
        self,
        prompt,
        max_length=200,
        temperature=0.8,
        top_p=0.92,
        top_k=50,
        num_sequences=1
    ):
        """Generate creative text from a prompt."""
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        
        # Generate
        outputs = self.model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            num_return_sequences=num_sequences,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=3
        )
        
        results = []
        for output in outputs:
            text = self.tokenizer.decode(output, skip_special_tokens=True)
            results.append(text)
        
        return results
    
    def write_story(self, beginning, length=300):
        """Generate a short story."""
        prompt = f"Story: {beginning}"
        return self.generate(prompt, max_length=length, temperature=0.9)
    
    def write_poem(self, theme, length=150):
        """Generate a poem."""
        prompt = f"A poem about {theme}:\\n\\n"
        return self.generate(prompt, max_length=length, temperature=0.85)
    
    def continue_text(self, text, length=100):
        """Continue a piece of text."""
        return self.generate(text, max_length=len(text.split()) + length)
    
    def write_multiple_endings(self, beginning, num_endings=3):
        """Generate multiple story endings."""
        return self.generate(
            beginning,
            num_sequences=num_endings,
            temperature=1.0
        )

# Example usage
if __name__ == "__main__":
    writer = CreativeWriter()
    
    # Generate a story
    story_beginning = "In a world where robots had feelings"
    print("\\n--- Story Generation ---")
    print(f"Beginning: {story_beginning}")
    stories = writer.write_story(story_beginning)
    print(f"\\nGenerated:\\n{stories[0]}")
    
    # Generate a poem
    print("\\n--- Poem Generation ---")
    poems = writer.write_poem("the beauty of sunrise")
    print(poems[0])
    
    # Multiple endings
    print("\\n--- Multiple Endings ---")
    prompt = "The detective opened the door and saw"
    endings = writer.write_multiple_endings(prompt, 2)
    for i, ending in enumerate(endings):
        print(f"\\nEnding {i+1}: {ending}")
'''

print("Creative Writer Code:")
print(generator_code)

# ========== QUESTION ANSWERING ASSISTANT ==========
print("\n" + "=" * 60)
print("PROJECT 3: Q&A ASSISTANT")
print("=" * 60)

qa_assistant_code = '''
"""
Question Answering Assistant
Answer questions from provided context
"""
from transformers import pipeline
import textwrap

class QAAssistant:
    def __init__(self):
        """Initialize the QA assistant."""
        print("Loading QA model...")
        self.qa_pipeline = pipeline(
            "question-answering",
            model="deepset/roberta-base-squad2"
        )
        self.knowledge_base = {}
        print("Assistant ready!")
    
    def add_knowledge(self, topic, content):
        """Add knowledge to the assistant."""
        self.knowledge_base[topic.lower()] = content
        print(f"Added knowledge about: {topic}")
    
    def answer(self, question, context=None):
        """Answer a question based on context."""
        if context is None:
            # Try to find relevant context from knowledge base
            for topic, content in self.knowledge_base.items():
                if topic in question.lower():
                    context = content
                    break
        
        if context is None:
            return "I don't have enough context to answer that question."
        
        result = self.qa_pipeline(question=question, context=context)
        
        return {
            "answer": result["answer"],
            "confidence": round(result["score"], 4),
            "context_used": context[:100] + "..."
        }
    
    def interactive_qa(self, context):
        """Run interactive Q&A session."""
        print("\\n" + "=" * 40)
        print("Q&A Session - Type 'quit' to exit")
        print("=" * 40)
        print(f"\\nContext: {context[:200]}...")
        
        while True:
            question = input("\\nYour question: ").strip()
            
            if question.lower() == 'quit':
                print("Session ended!")
                break
            elif not question:
                continue
            
            result = self.answer(question, context)
            print(f"Answer: {result['answer']}")
            print(f"Confidence: {result['confidence']:.2%}")

# Example usage
if __name__ == "__main__":
    assistant = QAAssistant()
    
    # Add knowledge
    python_knowledge = """
    Python is a high-level, general-purpose programming language created 
    by Guido van Rossum and first released in 1991. Python's design 
    philosophy emphasizes code readability with its use of significant 
    indentation. Python supports multiple programming paradigms, including 
    procedural, object-oriented, and functional programming. It has a 
    comprehensive standard library and is dynamically typed.
    """
    
    assistant.add_knowledge("Python", python_knowledge)
    
    # Answer questions
    questions = [
        "Who created Python?",
        "When was Python first released?",
        "What programming paradigms does Python support?",
    ]
    
    print("\\n--- Q&A Demo ---")
    for q in questions:
        result = assistant.answer(q, python_knowledge)
        print(f"\\nQ: {q}")
        print(f"A: {result['answer']} (confidence: {result['confidence']:.2%})")
'''

print("Q&A Assistant Code:")
print(qa_assistant_code)

# ========== COMBINED CHATBOT APPLICATION ==========
print("\n" + "=" * 60)
print("PROJECT 4: FULL CHATBOT APPLICATION")
print("=" * 60)

full_chatbot_code = '''
"""
Full-Featured Chatbot Application
Combines conversation, creativity, and Q&A
"""
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

class SmartChatbot:
    def __init__(self):
        """Initialize the smart chatbot."""
        print("Initializing Smart Chatbot...")
        
        # Conversation model
        self.conv_tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
        self.conv_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
        self.chat_history = None
        
        # Sentiment analyzer
        self.sentiment = pipeline("sentiment-analysis")
        
        # QA pipeline
        self.qa = pipeline("question-answering")
        
        # Zero-shot classifier
        self.classifier = pipeline("zero-shot-classification")
        
        print("Smart Chatbot ready!")
    
    def analyze_intent(self, text):
        """Classify user intent."""
        labels = ["question", "conversation", "request", "greeting", "farewell"]
        result = self.classifier(text, labels)
        return result["labels"][0], result["scores"][0]
    
    def analyze_sentiment(self, text):
        """Analyze user sentiment."""
        result = self.sentiment(text)[0]
        return result["label"], result["score"]
    
    def chat(self, user_input):
        """Process user input and generate response."""
        # Analyze intent
        intent, intent_conf = self.analyze_intent(user_input)
        
        # Analyze sentiment
        sentiment, sent_conf = self.analyze_sentiment(user_input)
        
        # Generate conversational response
        new_input_ids = self.conv_tokenizer.encode(
            user_input + self.conv_tokenizer.eos_token,
            return_tensors='pt'
        )
        
        if self.chat_history is not None:
            bot_input_ids = torch.cat([self.chat_history, new_input_ids], dim=-1)
        else:
            bot_input_ids = new_input_ids
        
        self.chat_history = self.conv_model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=self.conv_tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
        
        response = self.conv_tokenizer.decode(
            self.chat_history[:, bot_input_ids.shape[-1]:][0],
            skip_special_tokens=True
        )
        
        return {
            "response": response,
            "intent": intent,
            "intent_confidence": intent_conf,
            "sentiment": sentiment,
            "sentiment_confidence": sent_conf
        }
    
    def answer_from_context(self, question, context):
        """Answer a factual question."""
        result = self.qa(question=question, context=context)
        return result["answer"], result["score"]
    
    def reset(self):
        """Reset conversation history."""
        self.chat_history = None

# Example usage
if __name__ == "__main__":
    bot = SmartChatbot()
    
    print("\\n--- Smart Chatbot Demo ---")
    
    messages = [
        "Hello! How are you today?",
        "I'm feeling great! What's your favorite thing to talk about?",
        "That's interesting! Can you help me with something?",
        "Goodbye, nice chatting with you!"
    ]
    
    for msg in messages:
        print(f"\\nUser: {msg}")
        result = bot.chat(msg)
        print(f"Bot: {result['response']}")
        print(f"  [Intent: {result['intent']} ({result['intent_confidence']:.2f})]")
        print(f"  [Sentiment: {result['sentiment']} ({result['sentiment_confidence']:.2f})]")
'''

print("Full Chatbot Code:")
print(full_chatbot_code)

# ========== RUNNING DEMO ==========
print("\n" + "=" * 60)
print("RUNNING SIMPLE DEMO")
print("=" * 60)

# Simple demonstration without heavy model loading
demo_code = """
# Quick demo with lightweight model
try:
    from transformers import pipeline
    
    # Use a small, fast model for demo
    generator = pipeline('text-generation', model='distilgpt2')
    
    prompts = [
        "Once upon a time",
        "The secret to happiness is",
        "In the year 2050"
    ]
    
    print("Text Generation Demo:")
    print("-" * 40)
    
    for prompt in prompts:
        result = generator(prompt, max_length=30, num_return_sequences=1)
        print(f"Prompt: {prompt}")
        print(f"Generated: {result[0]['generated_text']}")
        print()
        
except Exception as e:
    print(f"Demo skipped: {e}")
    print("Install transformers to run: pip install transformers torch")
"""

print("Demo Code:")
print(demo_code)

# Actually run the demo
try:
    from transformers import pipeline
    
    print("\n--- Running Demo ---")
    generator = pipeline('text-generation', model='distilgpt2')
    
    prompts = [
        "Once upon a time",
        "The secret to happiness is"
    ]
    
    for prompt in prompts:
        result = generator(prompt, max_length=30, num_return_sequences=1)
        print(f"\nPrompt: {prompt}")
        print(f"Generated: {result[0]['generated_text']}")
        
except Exception as e:
    print(f"\n(Demo skipped - {e})")

# ========== DEPLOYMENT TIPS ==========
print("\n" + "=" * 60)
print("DEPLOYMENT TIPS")
print("=" * 60)

deployment_tips = """
Deploying Your Chatbot:

1. FLASK API
```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = chatbot.respond(data['message'])
    return jsonify({'response': response})
```

2. FASTAPI (Recommended)
```python
from fastapi import FastAPI
app = FastAPI()

@app.post("/chat")
async def chat(message: str):
    response = chatbot.respond(message)
    return {"response": response}
```

3. GRADIO (Easy UI)
```python
import gradio as gr

def respond(message, history):
    return chatbot.respond(message)

gr.ChatInterface(respond).launch()
```

4. STREAMLIT (Quick Prototyping)
```python
import streamlit as st

if prompt := st.chat_input("Say something"):
    st.write(chatbot.respond(prompt))
```

Performance Tips:
- Use smaller models for production (distilgpt2, DialoGPT-small)
- Cache model loading
- Use GPU when available
- Consider batching requests
- Add rate limiting
"""

print(deployment_tips)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

summary = """
Chatbot/Text Generator Projects Built:

1. SIMPLE CHATBOT (DialoGPT)
   - Maintains conversation context
   - Natural dialogue generation
   - Reset functionality

2. CREATIVE WRITER (GPT-2)
   - Story generation
   - Poem writing
   - Multiple endings
   - Temperature control

3. Q&A ASSISTANT
   - Answer from context
   - Knowledge base
   - Confidence scoring

4. SMART CHATBOT
   - Intent classification
   - Sentiment analysis
   - Conversation + Q&A

Key Takeaways:
✅ DialoGPT for conversations
✅ GPT-2 for creative text
✅ Pipeline API for quick tasks
✅ Context management for coherence
✅ Multiple deployment options

Next Steps:
- Fine-tune on your own data
- Add more capabilities (memory, tools)
- Deploy to production
- Build a web interface
"""

print(summary)

print("\n" + "=" * 60)
print("✅ Chatbot/Text Generator Project - Complete!")
print("=" * 60)
