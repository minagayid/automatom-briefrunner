# Devpost Account Audit — 27 August 2026

The Devpost session is authenticated as `minagayid` and can edit `https://devpost.com/software/automatom-briefrunner/edit`.

That project is submitted to the **Agents for Humans Hackathon**, not the All Things Agentic Hackathon. It currently contains legacy tags (`python`, `fastapi`, `strands-agents-sdk`, `amazon-bedrock`, `amazon-web-services`, `sqlite`), the old GitHub repository link, and a YouTube link. It must not be changed as a substitute for the All Things Agentic entry.

Next action: locate the distinct Devpost project associated with All Things Agentic, likely one of the other Automatom project slugs on the account, then inspect its editor before editing any fields.

A second editable project, `https://devpost.com/software/automatom/edit`, is a distinct legacy Automatom entry. Its current text describes Qwen, Alibaba Cloud, and the original GitHub repository. The edit page does not show a hackathon association in the visible content, so it must not be assumed to be the All Things Agentic submission. The account’s challenge/participation list must be checked next.

The authenticated All Things Agentic workspace confirms the relevant submission is `1133639-automatom` and exposes its editor at `https://devpost.com/submit-to/30845-all-things-agentic-hackathon/manage/submissions/1133639-automatom/edit`. This is distinct from both portfolio-only legacy projects. The hackathon dashboard reiterates the mandatory Gemini 3.5+, Google agent framework, and Google Cloud service requirements.

Authentication has now been restored for both accounts. Devpost is authenticated as `minagayid`; the confirmed All Things Agentic submission editor is available. Google Cloud Console is authenticated as `minagayid@gmail.com`, but no active project has been selected yet.

Google Cloud Console selected **My First Project** (`project-319b7de3-fbdb-4f01-abb`). It contains the existing `automatom-briefrunner` Cloud Run service in `us-central1`, last updated five days ago. The console displays a warning that the free trial is over and services require an upgrade to restore. The service detail URL is `https://console.cloud.google.com/run/detail/us-central1/automatom-briefrunner?project=project-319b7de3-fbdb-4f01-abb`.

Cloud Run logs show that the service successfully handled Gemini-mode requests on 22 August 2026, including `POST /demo-runs` and `GET /runs/...` requests returning HTTP 200. The current log shows an autoscaled instance starting successfully and responding HTTP 200 to `/health`, followed later by a GET request returning HTTP 500. The console-wide warning states that the project’s free trial is over and services require an upgrade to restore. This billing state is likely the controlling availability problem; no deployment should be initiated before the user explicitly confirms the intended billing action.

The official All Things Agentic Google Cloud credit request form is closed because all available credits have been distributed. Therefore, the only legitimate no-cost route is to rely on previously captured, truthful Cloud Run evidence and avoid redeployment; a new billable deployment cannot be created from this project without restoring billing.

The local reviewer demonstration is running on `http://127.0.0.1:8010`. Its `/health` output explicitly reports `agentMode: "offline"`, `vertexAiConfigured: false`, and `authentication: "unconfigured"`; it must be shown only as the reproducible workflow/approval demo, not as a live Gemini invocation.

On the confirmed All Things Agentic project details editor, the description, tags, and repository field have been replaced in the browser but have not been saved. The new repository field is `https://github.com/minagayid/automatom-briefrunner`; tags include Google Gen AI SDK, Gemini 3.5 Flash, Vertex AI, Google Cloud Run, and Cloud Logging. The old YouTube URL remains until the new 2:21 evidence video has been uploaded. The new video itself explicitly labels the local demo as offline and uses recorded Cloud Run URL/log evidence for the historical Gemini deployment.

## 2026-08-27 video-upload checkpoint
- YouTube Studio identity verification gate was completed; the account resumed normal upload access.
- Uploaded evidence video: `automatom_brief_runner_evidence_demo.mp4` (2:21).
- Assigned video URL: https://youtu.be/XqphKLthw5o
- Set title: `Automatom — Gemini 3.5 Flash & Cloud Run Evidence Demo`.
- Set a factual description that distinguishes the reproducible offline workflow from historic Vertex AI / Cloud Run evidence and notes the currently unavailable historic service.
- Selected `No, it's not made for kids` and no age restriction.
- The video remains private while the upload wizard progresses to final visibility/publication.

## 2026-08-27 public video publication
The replacement evidence video was published publicly on YouTube with the title `Automatom — Gemini 3.5 Flash & Cloud Run Evidence Demo`. The public video URL is https://youtu.be/XqphKLthw5o. YouTube Studio reported `No issues found` during copyright checks, and the final publication dialog confirmed `Video published` on 27 August 2026.

## Official requirements and no-cost credit result
The official All Things Agentic resources and FAQ state that each project must use Gemini 3.5 or newer, at least one Google agent framework, and at least one Google Cloud infrastructure service. They require an English public YouTube or Vimeo video of no more than four minutes, and require the video to demonstrate the backend running on Google Cloud; acceptable proof includes a Google Cloud Console recording or a live `.run` URL. The FAQ also confirms that a project need not remain live during judging if this proof has been captured. The $150 hackathon-credit form was the available no-cost route, but the form itself returned a closed notice because all available credits had been distributed. Sources: https://allthingsagentichackathon.devpost.com/resources ; https://allthingsagentichackathon.devpost.com/details/faqs ; https://forms.gle/5PtXmw1dSbDnpYke9
