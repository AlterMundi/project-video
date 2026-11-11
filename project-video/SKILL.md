---
name: project-video
description: Create concise project videos from selected project sources, real captures or work-story packets, including an editable composition, MP4, poster and captions when speech is used. Use for project demos, build stories and short explainers; use the existing publishing workflow for posting or scheduling.
metadata:
  version: "0.2.0"
---

# Project video

Make one understandable, distinctive video about a concrete project result.
Start with what a viewer can see or do. Preserve the project's own visual
identity and the distinction between demonstrated behavior and illustration.

## Select the story and evidence

Accept a selected project directory, URL, capture set or `work-story-capture`
packet. Read only relevant sources and the current request. A repository alone
can support a claim about its code; it does not prove deployment or physical use.
For a URL, inspect the rendered surface when plain text misses the product.

Reuse the selected packet's source IDs, revisions, credits, audience and media
masters. A packet is useful, not a prerequisite: a small project video may use
a compact source list. When available, `work-story-capture` can supply process evidence and editorial
handoff, and `audio-seed-bank` can supply explicitly selected recordings. These
are optional adapters: a local source list and permitted media are sufficient.
Do not require private services or install other skills just to accept inputs.

Decide the intended viewer, their reason to care and one useful next action.
Choose the strongest observable moment. For an app, inspect an action and its
result; for a build, inspect the object and what it actually does. If essential
footage is missing, finish the script/shot list and identify the exact missing
shot. Do not invent a working interface, successful experiment or testimonial.

Record the selected facts, source locations, evidence state and permitted
audience alongside the storyboard. Exclude private conversations, credentials
and unrelated files. Public source code does not make all local assets public.

## Direct the edit

Resolve routine choices from the request and material. A useful starting point
is 20–30 seconds, one central idea, a visible payoff near the beginning and a
clear ending. Use a longer explanation when the selected mechanism needs it.
Do not force a launch advertisement onto a process story.

Write a compact brief and timed storyboard before composing: purpose, opening,
selected visual proof, on-screen text, audio, closing action and sources.
Use [the brief example](templates/video-brief.json) only when structured handoff
helps; it is a filled fictional example, not a mandatory schema or project fact.

Use motion to direct attention. Animate actual product elements when useful;
let original footage carry a physical result. Keep diagrams and reconstructions
visibly distinct from original evidence. Match typography, palette and graphic
language to the project rather than applying one tribe-wide visual template.

For portrait delivery, compose for a phone while preserving the spatial context
needed to understand an action and its result. A stable complete-screen view can
be the right choice for an editor: keep native controls together and let them
appear through actual use. Use close-ups selectively when they improve the read
without losing that context. Respect the human's preferred reference and framing;
do not turn a phone-readability heuristic into a compulsory crop or redesign.
Keep intended editorial text readable, and identify native microcopy that is
context rather than required reading. Preserve the project's brand and let
continuous action carry a shot without a new headline each time.

Budget reading time after text has fully entered. Approximately 0.3 seconds per
word is an initial editing heuristic, not a measured accessibility guarantee.
Shorten copy before accelerating it. Inspect the final video at phone size.
Never let a music grid dictate an unreadable text reveal.

## Compose with the available tools

Read [production](references/production.md) for renderer selection, audio and
export. Reuse a qualified renderer and current native tool contracts. Keep the
editorial brief independent of the engine and model name. Do not change provider,
voice, account or runtime defaults to make a render work.

For an authorized video request, continue through rendering and review without
adding a routine preview approval round. Ask only for a missing decision that
materially changes the selected content, audience or external effect. A request
for an analysis or storyboard ends at that artifact unless production is also
requested.

Keep one editable source and versioned drafts in the owning project. Use the
current harness's delivery directory for final files. Before a substantial job,
record its scratch budget and cleanup point; use the receiving capability map
when selecting compute. Preserve supplied originals and uncertain provider work.

## Review and hand off

Check settled frames from every scene and frames inside transitions. Watch the
complete export, first muted for clarity, then with sound when present. Probe
and decode the actual MP4; a successful composition check is insufficient.
Correct missing media, illegible text, clipping and unsupported factual claims.
Label any review that could not be performed.

Challenge the scene grammar as well as individual frames: repeated title,
screenshot and paragraph layouts can pass structural checks while making a weak
film. At 360px width, identify what the eye sees first and whether the action
and result remain understandable. A passed check or still review is not a
comparison with another workflow and does not establish a best combined skill.

Deliver the MP4, strongest settled poster frame, concise accompanying text,
credits, review note and reproducible composition/source manifest. If speech is
used, include a reviewed transcript and timed captions. Link existing masters
instead of exporting unnecessary archives. Record source and output revisions.

For editorial release, use the selected publishing workflow within actual
authorization. If available, `daimon-social-identity` can receive the material;
it is not a runtime dependency. A rendered video is not a published post.

Use [the evaluation plan](references/evaluation.md) when comparing workflows
or qualifying a new material/runtime. Public availability does not establish
that every receiver or kind of source has been tested.
