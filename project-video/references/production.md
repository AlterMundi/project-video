# Production choices

## Choose the engine from the material

Use an existing working project renderer first. The smallest useful choices are:

| Material | Preferred route | What to retain |
|---|---|---|
| UI and designed motion | Qualified local Hyperframes, or an already working HTML/Remotion composition | Local assets, exact tool versions and seekable timeline |
| Physical footage, interviews, mixed captures | Existing editor or FFmpeg edit with intentional crops, titles and sound | Original clips, source time ranges and edit decisions |
| Sparse screenshots or diagrams | Designed motion composition with a concrete reveal | Source images/diagrams, layout and timing |

Hyperframes 0.9.31 was exercised with Node24, Chromium156 and FFmpeg7.1.5 in
app-demo and process-story trials. It is not bundled. That observation does not
qualify another receiver: resolve its actual CLI, browser and locally installed
engine guidance, then check and render a bounded real project. An existing
working renderer is preferable to installing another engine for this skill.
Pin the selected toolchain rather than fetching an unbounded latest version.
Follow its current composition and media contracts; use unique media IDs,
seekable timelines and local fonts/assets. A successful editor preview is not
proof that the encoded video uses the same framing or has working audio.

Estimate scratch from the renderer's decoded-frame/cache behavior, not only
compressed clip sizes. In an independent full-screen UI trial, frame extraction
approached the selected limit before the final MP4 existed. Uniformly scaling
the whole intermediate to its actual on-screen pixel dimensions reduced that
working set without cropping; retain the original and record the transform.
Observe a bounded first render and stop that owned local attempt before its
limit when necessary. Do not replay uncertain external generations to fix a
local encoding or cache problem.

FFmpeg can edit real footage and finish exports; its availability alone does
not supply motion design. Avoid turning unavailable animation tooling into an
unrequested deck of title cards. A model-authored HTML composition is an option
only when its capture route works: seek to a deterministic time, await fonts
and assets, then capture. Do not record an uncontrolled wall-clock animation.

Record the actual engine, version, render settings, source hashes and asset
locations in a small manifest. Keep the material local where practical; cloud
rendering, provider processing and paid generation require actual task scope
and the receiving route. Skill text grants no account access.

## Audio and captions

Choose sound for this story. A clear UI demo can use music and a few quiet
interaction cues; an instrument or physical experiment may need its original
sound to carry the result. Silence is valid when deliberate. Do not add sound
that suggests an action occurred when it did not.

Use the already selected authorized voice route only when narration is requested
or clearly part of the brief. Keep synthesized narration identified in the
source record. Generate a concise script, measure the resulting audio, and
adjust the edit to the actual delivery. Do not stretch speech until it becomes
unnatural. Never clone a participant's voice from supplied footage by inference.

Reuse existing timed transcripts. For new source speech, use an available qualified
transcription workflow and review difficult words. For generated speech,
reuse genuine alignment or perform qualified alignment. Do not manufacture
word times by dividing duration evenly. SRT/VTT captions and on-screen titles
serve different purposes; deliver captions when the video contains speech.

When word alignment is unavailable, separately generated short passages can
support phrase captions using their actual clip boundaries and measured PCM
durations. Check the generated transcript against the intended script and keep
the original audio. Those boundaries do not establish individual word timing
or perceptual listening.

Listen for intelligibility, clipping, abrupt edits and repeated sharp effects.
Measure the mix when useful and document its actual loudness/peak settings;
no universal platform loudness target is imposed here. Fade the end deliberately.
Use licensed or original music and retain the asset-specific attribution.
The reviewed brag music is CC BY 4.0 even though its code is MIT.

## Formats and review

Choose the requested aspect ratio; otherwise infer it from the destination and
footage. Typical delivery sizes are 1080×1920, 1920×1080 or 1080×1080 at 30 fps.
Recompose for each needed ratio instead of blindly cropping captions or UI.
Inspect readable titles and supporting text at a realistic phone preview size.
Keep critical content clear of the destination's actual overlay areas.

Judge editorial text after delivery scaling: a360px preview of a1080px-wide
master is one third of the authored size, so36px becomes12px. A large canvas
font is not automatically a readable phone label. Native microcopy in an
explicitly selected whole-screen overview may be context; important editorial
instructions still need their own readable treatment.

For a broadly compatible MP4, H.264 with yuv420p and AAC when audio is present
is a useful default. Check actual duration, dimensions, frame rate and decode
health with installed `ffprobe`/`ffmpeg`. Inspect the export, not only the editor.

Select a representative settled poster. A separate poster and a strong natural
opening are more robust than a promise that replacing frame zero controls every
platform's thumbnail. Use a platform's supported thumbnail option when posting.

Inspect painted layers as well as measured boxes. In the first process-story
trial, a padded card covered supporting text while the engine's layout checks
passed. Phone-size settled frames exposed it; correcting the card's box sizing
and document margins resolved the actual visual fault. Preserve that distinction
when using automated checks as evidence.

Check whether each promised change remains visible in the next shot. Choose
an actual matching source frame when animation temporarily hides an accessory
or face. Keep original save/reload proof distinct from a later posed render,
and document crops, holds or slowing used to explain it.

Inspect contrast inside captured media as well as DOM text. Thin historical
ASCII strokes passed the engine's text checks but disappeared on the phone
sheet. A documented contrast grade and closer crop made the actual source
readable; preserve its ungraded original separately.

Keep a concise review note: factual claims checked against which sources;
visual coverage; full-playback and listening status; caption review; known gaps;
render time and approximate resource/cost observations when measured. Automated
checks cannot establish that the story is understandable or beautiful.


## Reusable export check

`../scripts/verify_video.py` uses installed `ffprobe`, with optional full decode
through `ffmpeg`. It accepts an output file and optional expected duration, size
and frame rate. From the skill directory:

```sh
python3 scripts/verify_video.py result.mp4 --duration 30 --size 1080x1920 --fps 30 --web-compatible --decode
```

A nonzero exit or `ok:false` means the selected expectations did not pass. It
checks the actual encoded file; it cannot assess readable UI, story quality,
listening, asset permission or a person's understanding. Retain its report with
the project's source/edit manifest rather than interpreting it as human review.
