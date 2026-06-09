# Gemini Image Generation Models - Nano Banana

> Last updated: 2026-03-14
> Aligned with Google's March 2026 API state and pricing

## Available Models

### gemini-3.1-flash-image-preview (Recommended - Speed + Quality)
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-3.1-flash-image-preview` |
| **Tier** | Nano Banana 2 (Flash) |
| **Speed** | Fast - optimized for high-volume use |
| **Aspect Ratios** | All 14 ratios (see table below) |
| **Max Resolution** | Up to 4096×4096 (4K tier) |
| **Features** | Google Search grounding (web + image), thinking levels, image-only output, extreme aspect ratios, 512px drafts |
| **Rate Limits (Free)** | ~5-15 RPM / ~20-500 RPD (preview model - more restrictive than stable) |
| **Output Tokens** | ~1,290 output tokens per image |
| **Cost (1K)** | ~$0.067/image |
| **Arena Rank** | #1 on Artificial Analysis Image Arena |
| **Best For** | Most blog images, rapid iteration, batch generation |

### gemini-3-pro-image-preview (Highest Quality - Text + Detail)
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-3-pro-image-preview` |
| **Tier** | Nano Banana Pro |
| **Speed** | Slower - uses reasoning before generating (generates interim images internally) |
| **Aspect Ratios** | All 14 ratios |
| **Max Resolution** | Up to 4096×4096 (4K tier) |
| **Features** | 94% text accuracy (quoted text), 14 reference images, C2PA Content Credentials |
| **Rate Limits (Free)** | ~5-10 RPM / ~20-100 RPD |
| **Output Tokens** | Higher (reasoning + generation) |
| **Cost (1K)** | ~$0.134/image (2× Flash) |
| **Best For** | Hero images with text overlays, highest quality final assets, branded content |

**Note:** The base text model `gemini-3-pro-preview` was deprecated March 9, 2026, but the **image variant** (`gemini-3-pro-image-preview`) remains active on AI Studio and Vertex AI.

### gemini-2.5-flash-image (Stable Fallback)
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-2.5-flash-image` |
| **Tier** | Nano Banana Original (stable) |
| **Speed** | Fast |
| **Aspect Ratios** | 1:1, 16:9, 9:16, 4:3, 3:4 (5 only) |
| **Max Resolution** | Up to 1024×1024 (1K tier) |
| **Rate Limits (Free)** | ~10-15 RPM / ~500 RPD (stable - more generous than preview models) |
| **Cost (1K)** | ~$0.039/image |
| **Best For** | Budget-conscious workflows, proven quality, stable fallback |

### Imagen 4 (Dedicated Image Models)
| Property | Fast | Standard | Ultra |
|----------|------|----------|-------|
| **Pricing** | $0.02/image | $0.04/image | $0.06/image |
| **Speed** | Fastest | Medium | Slowest |
| **Best For** | Batch generation, drafts | General-purpose blog images | Maximum detail, print |

**Notes:** Imagen 4 models are dedicated image generators (not multimodal LLMs). They lack conversational editing but offer lower per-image cost for high-volume workflows.

## Deprecated Models (DO NOT USE)

### gemini-2.5-flash-image-preview
- **Status:** Shut down - use the stable `gemini-2.5-flash-image` variant

### gemini-2.0-flash-exp
- **Status:** Deprecated, shutdown June 1, 2026. Use `gemini-2.5-flash-image`

### Legacy models (Gemini 2.0 Flash and earlier)
- **Status:** All retiring June 1, 2026. Migrate to NB2 Flash or Imagen 4.

## Model Selection for Blog Content

| Blog Use Case | Recommended Model | Why |
|---------------|-------------------|-----|
| Quick draft / iteration | NB2 Flash (512px) | Fastest, cheapest, good enough for review |
| Standard blog images | NB2 Flash (1K-2K) | Best speed/quality ratio |
| Hero images with text | NB Pro | 94% text accuracy, reasoning mode |
| Final hero / OG at 4K | NB2 Flash or Pro (4K) | Both support 4K output |
| Budget batch generation | Original (2.5 Flash) | $0.039/img, proven quality |

## Aspect Ratios

All 14 supported ratios. Availability varies by model:

| Ratio | Orientation | Blog Use Cases | NB2 Flash | Pro | Original |
|-------|-------------|---------------|:---------:|:---:|:--------:|
| `1:1` | Square | Social posts, thumbnails | ✅ | ✅ | ✅ |
| `16:9` | Landscape | Blog headers, OG images | ✅ | ✅ | ✅ |
| `9:16` | Portrait | Stories, Reels, mobile | ✅ | ✅ | ✅ |
| `4:3` | Landscape | Product shots, inline | ✅ | ✅ | ✅ |
| `3:4` | Portrait | Book covers, portrait | ✅ | ✅ | ✅ |
| `2:3` | Portrait | Pinterest pins, posters | ✅ | ✅ | ❌ |
| `3:2` | Landscape | DSLR standard, prints | ✅ | ✅ | ❌ |
| `4:5` | Portrait | Instagram portrait | ✅ | ✅ | ❌ |
| `5:4` | Landscape | Large format | ✅ | ✅ | ❌ |
| `1:4` | Tall strip | Vertical banners | ✅ | ✅ | ❌ |
| `4:1` | Wide strip | Section dividers, headers | ✅ | ✅ | ❌ |
| `1:8` | Extreme tall | Narrow strips | ✅ | ✅ | ❌ |
| `8:1` | Extreme wide | Ultra-wide banners | ✅ | ✅ | ❌ |
| `21:9` | Ultra-wide | Cinematic headers | ✅ | ✅ | ❌ |

## Resolution Tiers

| `imageSize` | Pixel Range | Model Availability | Cost Multiplier | Blog Use |
|-------------|-------------|-------------------|:---------------:|----------|
| `512` | Up to 512×512 | All models | 0.5× | Drafts, quick iteration |
| `1K` (default) | Up to 1024×1024 | All models | 1× | Standard web/social |
| `2K` | Up to 2048×2048 | NB2 Flash, Pro | 2× | Quality inline images |
| `4K` | Up to 4096×4096 | NB2 Flash, Pro | 4× | Print, hero images, final assets |

**Notes:**
- Actual pixel dimensions depend on aspect ratio (e.g., 4K at 16:9 = 4096×2304)
- Default is `1K` if `imageSize` is not specified
- Known bug: `imageSize` sometimes ignored through LiteLLM proxy and in image-to-image workflows

## Rate Limits

Google cut free-tier limits by ~92% in December 2025. Current structure:

| Tier | RPM | RPD | How to Get |
|------|-----|-----|-----------|
| Free | ~5-15 | ~20-500 | Default (API key only, no billing) |
| Tier 1 (Pay-as-you-go) | 150-300 | 1,500-10,000 | Enable billing on Google Cloud project |
| Tier 2 ($250+ spend) | 1,000+ | Unlimited | Cumulative $250+ API spend |

**Important:** Preview models (NB2, Pro) have more restrictive limits than stable models. Free tier for image generation may require billing to be enabled - some users report 0 IPM (images per minute) without billing.

## Pricing (March 2026)

| Model | Resolution | Cost per Image | Notes |
|-------|-----------|---------------|-------|
| NB2 Flash | 1K | ~$0.067 | Standard |
| NB2 Flash | 2K | ~$0.134 | 2× standard |
| NB2 Flash | 4K | ~$0.268 | 4× standard |
| Pro | 1K | ~$0.134 | 2× Flash |
| Pro | 4K | ~$0.536 | Premium quality |
| Original (2.5) | 1K | ~$0.039 | Budget option |
| Imagen 4 Fast | - | $0.02 | Cheapest dedicated image model |
| Imagen 4 Standard | - | $0.04 | Mid-range dedicated |
| Imagen 4 Ultra | - | $0.06 | Highest quality dedicated |
| Batch API | Any | 50% discount | Asynchronous, higher latency |

**Cost optimization:** Use 512px for drafts (cheapest), 1K for standard blog images, reserve 2K-4K for hero images and final assets.

## Multi-Image Input

| Feature | Limit | Notes |
|---------|-------|-------|
| Object references | Up to 6 | Style, composition, visual matching |
| Character references | Up to 5 | Assign names to preserve features |
| Total references | Up to 14 | Combined across types |
| Max input image size | 7 MB | Per image |

Useful for brand-consistent blog imagery: provide brand style references to maintain visual identity across generated images.

## Safety Filters - Dual Layer Architecture

### Layer 1: Input Filters (Configurable)
Standard harm category filtering via `safetySettings` API parameter. Covers hate speech, harassment, sexually explicit, and dangerous content.

### Layer 2: Output Filters (NON-CONFIGURABLE)
Server-side analysis of the **generated image itself**. Cannot be disabled through any API parameter.
- Returns `finishReason: "IMAGE_SAFETY"` (distinct from `"SAFETY"`)
- Known to be overly cautious - Google acknowledged "filters became way more cautious than we intended"
- Benign prompts like "dog" or "bowl of cereal" have been blocked
- Celebrity blocking tightened significantly with NB2

| `finishReason` | Meaning | Layer | Retryable? |
|----------------|---------|:-----:|:----------:|
| `STOP` | Successful generation | - | N/A |
| `IMAGE_SAFETY` | Output blocked by Layer 2 | 2 | Rephrase prompt |
| `PROHIBITED_CONTENT` | Content policy violation | 1 | No - topic blocked |
| `SAFETY` | General safety block | 1 | Rephrase prompt |
| `RECITATION` | Detected copyrighted content | 2 | Rephrase prompt |

**No workaround exists for Layer 2 blocks beyond rephrasing the prompt.**

## Content Credentials

- **SynthID watermarks** are always embedded (invisible, machine-readable). Survives rescaling, compression, and most edits - cannot be disabled
- **C2PA Content Credentials** are embedded on Nano Banana Pro images from Gemini App, Vertex AI, and Google Ads

## Blog Image Post-Processing

| Step | Target | Tool |
|------|--------|------|
| Generate | 2K resolution | Gemini API |
| Convert | WebP (25-30% smaller than JPEG, 97% browser support) | ImageMagick or Sharp |
| Fallback | AVIF (50% smaller than WebP, 90% support) with JPEG fallback | ImageMagick |
| Hero size | 1920x1080 (16:9) or 1200x630 (OG) | Resize |
| Inline size | < 200KB compressed | Quality adjustment |
| Hero size | < 500KB compressed | Quality adjustment |
| Metadata | Strip EXIF, keep SynthID + C2PA | ImageMagick -strip |

## Key Limitations
- No native transparent backgrounds (workaround: prompt green background, then chromakey removal)
- Text rendering quality varies - keep text under 25 characters for best results (Pro achieves 94% accuracy with quoted text)
- Safety filters may block benign prompts - use auto-rephrase workflow
- Session context resets between Claude Code conversations
- `imageSize` and thinking level depend on MCP package version support
- No video generation (use Veo 3.1 for image-to-video workflows)
