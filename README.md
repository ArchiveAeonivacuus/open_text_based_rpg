# Why open_text_based_rpg?

## Text Based RPG

Do you know traditional text-based RPG games? They're probably the easiest type of RPG to get into and the simplest to create. In my opinion, if someone wants to develop an RPG with near-infinite freedom, starting with a text-based RPG might be the easiest approach.

The first text-based RPG I've ever played was an _Era_ series game related to _Touhou_ Project. Its map was incredibly detailed - every location, character, and item - they all had its own stats, descriptions, and so on. The interactions were so rich that you could almost say it would have been even more amazing with more detailed visuals.

## Open

Text-based RPGs still rely on predetermined outputs that are written into codes before. But it would be different if AI were introduced. When it comes to the questions that why not just play with a chat AI directly? Why a project? Because when interacting directly with an AI, you often run into issues like inaccurate long-term memory, imprecise numerical calculations, and the generation of content that doesn't fit the established setting - hallucinations, so to speak. That's why I want to start a project called `open_text_rpg`. The idea is to use precise code to store settings, numerical values, states, and so on, while using AI to generate the emotional and interactive content. This would transform the kind of exploratory, adventure-driven games that previously required a human 'DM' (like in D&D) into something achievable through code combined with AI.

## Instructions

Currently the project has just begun, so there is no detailed explanation at the moment. When we start writing code, we may add some explanations here.

## Construction

The current expected structure is as follows:

```text
OpenTextRPG/
├── Game Engine (Deterministic)
│   ├── State Manager - Local Storage Game State
│   ├── Rule Engine - Handling rules for battles, skills, economics, and more
│   ├── Event System - Task Trigger, World Events
│   └── Validator - Ensure that AI output complies with game rules (also accepts manual rollback)
├── AI Integration Layer
│   ├── Context Builder - Assembly Prompt Words
│   ├── Output Parser - Extract Structured Data
│   ├── Memory Manager - Store Key Memory in Vector Database
│   └── Style Controller - Maintain Narrative Consistent
└── Interactive Interface
    ├── Web/Mobile Frontend
    ├── Command Line Interface
    └── API Services
```

## Developer

[ArchiveAeonivacuus](www.github.com/ArchiveAeonivacuus)

Tongyi Lingma is also used. [Tongyi Lingma](https://lingma.aliyun.com/)
