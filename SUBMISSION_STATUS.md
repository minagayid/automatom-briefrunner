# Submission Status — Automatom — BriefRunner

**Status as of 27 August 2026:** The repository is repaired, publicly available, and locally validated. The Devpost form, Google Cloud deployment, and public demonstration video remain account-bound actions and have **not** been completed or represented as complete.

> Do not submit the existing Devpost entry or reuse its old AWS/Strands description, old repository URL, ten-second static video, or failing Cloud Run URL. The entry will remain ineligible until the three required Google technologies are actually deployed and evidenced in the submitted video.

## Completed repository work

| Requirement or issue raised in the feedback | Completed correction | Verification |
|---|---|---|
| Required Gemini use | Added the Google Gen AI SDK adapter for `gemini-3.5-flash` through Vertex AI | `app/google_runtime.py`; unit test constructs the Vertex client |
| Required Google agent framework | Declared and documented Google Gen AI SDK (`google-genai`) | `requirements-google.txt`, README, architecture |
| Required Google Cloud service | Added Cloud Run container configuration and exact deployment instructions | `Dockerfile`, README deployment section |
| AWS/Strands mismatch | Removed the legacy AWS/Strands runtime and invalid static demo footage from the submission repository | Repository history and source files |
| Missing reproducibility instructions | Added local run, Vertex AI, Cloud Run, verification, and test instructions | `README.md` |
| Pre-submission repo history concern | Created a clean public submission repository with a transparent pre-existing-work disclosure | [`PRE_EXISTING_WORK.md`](PRE_EXISTING_WORK.md) and repository history |
| Devpost copy | Prepared complete field-by-field replacement content | [`DEVPOST_SUBMISSION.md`](DEVPOST_SUBMISSION.md) |
| Architecture | Re-rendered a diagram that explicitly names Cloud Run, Google Gen AI SDK, Gemini through Vertex AI, state, logging, and human approval | `all-things-agentic-architecture.png` |
| Code validation | Passed six regression tests and a local end-to-end offline contract test | Test output from 27 August 2026 |

## Account-bound actions still required

| Priority | Action | Why it cannot be safely inferred or fabricated |
|---|---|---|
| 1 | Deploy the repository to a Google Cloud project with Vertex AI enabled and verify `/health` reports `agentMode: "gemini"` | The previous published Cloud Run URL returned a 500 error; this repository does not have access to a Google Cloud account or billing project. |
| 2 | Record and publish a new public YouTube/Vimeo video, under four minutes, showing Cloud Run/Vertex evidence and a real Gemini-mode run | The prior local video was only ten seconds and did not show a live demo or Google Cloud evidence. |
| 3 | Sign in to the original Devpost account and replace the old form content using `DEVPOST_SUBMISSION.md` | The browser session could not authenticate to Devpost, and no changes should be submitted without confirming the final links. |

## Final submission sequence

1. In a Google Cloud project, follow the **Deploy to Cloud Run** section of `README.md`. Use the command only after confirming the project, enabled billing, and the service account permissions.
2. Call `<Cloud Run URL>/health`. Confirm it returns HTTP 200 and shows `agentMode: "gemini"`, `agentFramework: "Google Gen AI SDK"`, and `vertexAiConfigured: true`.
3. Record one continuous, truthful video using the timing checklist in the README: explain the problem and value; show the Cloud Run dashboard or `.run.app` URL; invoke `POST /demo-runs`; poll the Gemini-generated result; call the approval endpoint and show `sent: false`; show the architecture.
4. Upload the video as **public** on YouTube or Vimeo. Copy the final public URL.
5. Sign in to the existing Devpost account. Replace the project description and built-with list with [`DEVPOST_SUBMISSION.md`](DEVPOST_SUBMISSION.md), set **Taskmaster** as the category, replace the repository link with `https://github.com/minagayid/automatom-briefrunner`, and enter the verified Cloud Run and video URLs.
6. Include the disclosure paragraph exactly or equivalently, upload the rendered architecture image, review all final links, and submit before **31 August 2026 at 5:00 PM Pacific Time**. [1]

## Authentication fallback

If Devpost login continues to fail, do **not** create a duplicate Devpost account or a duplicate entry. Use the login method originally linked to the existing account and then the Devpost account-recovery/support flow. The existing project is publicly visible at `https://devpost.com/software/automatom-briefrunner`, confirming the correct account/project to recover.

## References

[1]: https://allthingsagentichackathon.devpost.com/rules "All Things Agentic Hackathon Official Rules"
