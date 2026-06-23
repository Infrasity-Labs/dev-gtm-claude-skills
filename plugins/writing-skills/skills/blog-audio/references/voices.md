# Gemini TTS Voice Catalog

30 prebuilt voices for Google Gemini TTS. All voices support 80+ languages
with automatic language detection.

## Full Voice Table

| Voice | Tone | Best For |
|-------|------|----------|
| Zephyr | Bright | Energetic intros, lifestyle content |
| Puck | Upbeat | Podcast host, casual blogs |
| Charon | Informative | Article narration (default), technical content |
| Kore | Firm | Expert/authority voice, dialogue guest |
| Fenrir | Excitable | Product launches, news highlights |
| Leda | Youthful | Youth-oriented content, tutorials |
| Orus | Firm | Business, formal content |
| Aoede | Breezy | Lifestyle, wellness, travel |
| Callirrhoe | Easy-going | Casual blogs, personal essays |
| Autonoe | Bright | Marketing, upbeat summaries |
| Enceladus | Breathy | Intimate storytelling, ASMR-adjacent |
| Iapetus | Clear | Technical documentation, clarity-first |
| Umbriel | Easy-going | Relaxed tutorials, guides |
| Algieba | Smooth | Professional narration, case studies |
| Despina | Smooth | Polished delivery, executive summaries |
| Erinome | Clear | Educational content, explainers |
| Algenib | Gravelly | Character voice, dramatic reading |
| Rasalgethi | Informative | News analysis, data-driven content |
| Laomedeia | Upbeat | Co-host voice, interview-style |
| Achernar | Soft | Gentle delivery, mindfulness content |
| Alnilam | Firm | Authoritative statements, conclusions |
| Schedar | Even | Neutral delivery, balanced reporting |
| Gacrux | Mature | Thought leadership, industry analysis |
| Pulcherrima | Forward | Direct, opinion pieces |
| Achird | Friendly | How-to guides, tutorials (recommended) |
| Zubenelgenubi | Casual | Conversational blogs, Reddit-style |
| Vindemiatrix | Gentle | Health, wellness, sensitive topics |
| Sadachbia | Lively | Listicles, roundups, energetic content |
| Sadaltager | Knowledgeable | Deep dives, pillar pages |
| Sulafat | Warm | Welcome messages, community content |

## Recommended by Blog Type

| Blog Type | Single Voice | Why |
|-----------|-------------|-----|
| How-to guide | Achird (Friendly) | Approachable, clear instruction delivery |
| Technical tutorial | Iapetus (Clear) | Precision and clarity for code/data |
| News analysis | Rasalgethi (Informative) | Authoritative without being dry |
| Thought leadership | Gacrux (Mature) | Gravitas for opinion and prediction |
| Listicle | Sadachbia (Lively) | Keeps energy up across list items |
| Case study | Algieba (Smooth) | Professional, results-focused delivery |
| Product review | Charon (Informative) | Balanced, trustworthy assessment |
| Pillar page | Sadaltager (Knowledgeable) | Sustained depth over long content |
| Lifestyle/wellness | Aoede (Breezy) | Light, inviting, relaxed pace |
| FAQ/knowledge base | Erinome (Clear) | Direct answers, no filler |

## Dialogue Mode Pairings

Recommended voice combinations for two-speaker podcast/dialogue format:

| Pair | Host | Guest/Expert | Style |
|------|------|-------------|-------|
| **Default** | Puck (Upbeat) | Kore (Firm) | Energetic host + authoritative expert |
| Professional | Achird (Friendly) | Charon (Informative) | Warm interviewer + knowledgeable guest |
| Casual | Zubenelgenubi (Casual) | Callirrhoe (Easy-going) | Relaxed conversation, both laid-back |
| Technical | Laomedeia (Upbeat) | Iapetus (Clear) | Curious host + precise technical expert |
| News | Schedar (Even) | Rasalgethi (Informative) | Neutral anchor + informed analyst |

## Model Comparison

| Model | ID | Best For | Cost (output) |
|-------|----|---------|----|
| **Flash** | `gemini-2.5-flash-preview-tts` | Summaries, standard narration, cost-sensitive | $10/1M tokens |
| **Pro** | `gemini-2.5-pro-preview-tts` | Dialogue mode, premium podcasts, audiobooks | $20/1M tokens |

**Default:** Flash for summary/full modes, Pro for dialogue mode.

Flash is 2x cheaper and faster. Pro has higher fidelity and better handling of
multi-speaker turn-taking. Use Pro when audio quality is the priority.

## Language Notes

- All 30 voices support 80+ languages via automatic detection
- Pass text in any supported language: no language parameter needed
- Voice characteristics (Bright, Firm, etc.) carry across languages
- For best results with non-English text, test voice-language combinations
- BCP-47 language codes are auto-detected from input text

## Style Control

Gemini TTS does not support SSML. Control style via natural language in the text:

Instead of markup, write the text in the desired style:
- For emphasis: use naturally emphatic phrasing
- For pauses: use punctuation (periods, ellipses, commas)
- For pace: shorter sentences = faster pace, longer = slower
- For tone: word choice drives delivery (urgent words = urgent delivery)

The TTS model interprets natural language prosody cues automatically.
