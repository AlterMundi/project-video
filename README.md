# Project Video

Create clear project demos and stories from selected source material: one
observable idea, real actions/results, an intentional edit and an editable
handoff. The skill includes optional metadata and a small read-only export
checker. It does not bundle or install a video engine, media assets or accounts.

## Install

Download a versioned release archive and verify it against SHA256SUMS.txt.
Copy its `project-video/` directory to your agent's skills directory, or use your
agent's GitHub skill installer with this repository and path `project-video`.
Keep the whole folder so references and scripts remain available. Optional
`agents/openai.yaml` metadata can be ignored by other runtimes.

Invoke `$project-video` with a selected project directory, URL, permitted capture
set or work-story packet. For example: "Make a30-second product demo using this
capture set. Keep the whole editor visible and show the real controls in use."
A longer process story or narration is selected by the actual request, not added
automatically. The skill is also available for normal automatic discovery.

## Tools

Use an existing qualified renderer/editor and its actual local instructions.
Hyperframes0.9.31 and FFmpeg were exercised during development; neither is a
mandatory skill backend. Source/corpus, voice and publishing adapters are
optional and use the receiver's existing authorized routes.

The included checker needs Python3 and installed FFprobe, plus FFmpeg for full
decode. From this repository:

```sh
python3 project-video/scripts/verify_video.py result.mp4 --duration 30 --size 1080x1920 --fps 30 --web-compatible --decode
python3 -m unittest discover -s project-video/tests -v
```

It verifies the encoded file and selected expectations, with read-only local
processing. It does not judge the story, a viewer's understanding or human
listening. The tests generate their own short media fixture; no private input
recordings are required to run them.

## Release scope

0.2.0 is the first public distribution of this package. See
[validation and remaining limits](docs/VALIDATION.md): actual app/process and
narration trials, an independent forward test, export verification and a clean
isolated installation. Physical-action footage, another being's receiving
adoption, human listening and first-view comprehension remain unverified.
No comparative superiority is claimed.

Published snapshots contain only this skill and its validation guidance.
Private case media, account/runtime bindings and generated project outputs are
excluded. Contributions should preserve the package's portable core and include
relevant verification; publication and installation do not grant resource access.

## License and attribution

MIT for this package's instructions and helper code. See LICENSE and
project-video/NOTICE. A generated project's music, fonts, footage and other
assets retain their own licenses and audiences; they are not relicensed here.
