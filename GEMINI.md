# Gemini Instructions

Use the shared repository guidance below when working on Yuuko Alert. Keep this file aligned with `AGENTS.md` so the project instructions do not diverge.

# Yuuko Alert — AI Coding Instructions

These instructions apply to AI coding assistants working in this repository. Keep changes focused, consistent with the existing project, and easy to review.

## Project Overview

Yuuko Alert is a small Python desktop application for Windows. It displays a “Selamat Pagi!” greeting with Yuuko's image and plays an audio clip.

- **Language:** Python
- **GUI:** Tkinter
- **Audio:** Pygame
- **Image handling:** Pillow
- **Windows integration:** `ctypes` through `platforms/windows.py`
- **Dependencies:** listed in `requirements.txt`
- **License:** MIT

## Project Structure

- `main.py` — application entry point, `AlertWindow` UI, and `SoundPlayer` audio helper.
- `platforms/windows.py` — Windows-specific helpers for DPI awareness, work-area detection, and application icon setup.
- `files/face.png` — application image.
- `files/icon.ico` — Windows application icon.
- `files/sound.mp3` — greeting audio.
- `requirements.txt` — Python dependencies.
- `README.md` — user-facing project documentation.

Treat the checked-out repository as the source of truth. If the structure changes, inspect the current files rather than assuming this list is still exact.

## Working Principles

1. **Understand first, then edit.** Read the relevant project context and inspect only what is necessary to implement the requested task.
2. **Keep scope narrow.** Do not refactor unrelated code, rename files, or change behavior beyond what the task requires.
3. **Preserve the existing design.** Follow the current object-oriented structure and naming conventions. Avoid duplicating existing functionality.
4. **Prefer small, clear changes.** Do not introduce abstractions or extra files without a concrete need.
5. **Keep dependencies minimal.** Prefer the Python standard library and existing dependencies. If a new dependency is necessary, explain why and update `requirements.txt`.
6. **Preserve application behavior.** The greeting, image, sound playback, window positioning, and Windows integration should remain intact unless the request explicitly changes them.
7. **Respect assets and licensing.** Do not replace, modify, or add third-party assets without a clear request and appropriate permission/license information.
8. **Do not claim tests were run unless they were actually run.** Mention any environment limitations, especially when Windows-specific behavior cannot be verified.

## Implementation Guidance

- Keep the application entry point in `main.py` unless a requested change justifies restructuring.
- Keep Windows-only API calls in `platforms/windows.py`; use a safe fallback where the current application already supports non-Windows execution.
- Keep user-facing text, layout values, and asset paths consistent with the existing constants and conventions.
- Preserve Tkinter image references for as long as they are displayed; avoid image garbage-collection issues.
- Avoid blocking the Tkinter event loop with long-running work.
- Use paths that work when the application is launched from the repository's expected working directory. If changing path handling, consider packaged Windows builds too.
- Update the README or changelog when a user-visible behavior or release-relevant change warrants it.

## Validation

For changes to the application, perform the checks that are practical in the current environment:

1. Review the changed code for correctness and consistency.
2. Confirm imports and dependency references are valid.
3. Run `python main.py` when a suitable GUI environment is available.
4. Test Windows-specific behavior on Windows when possible, including DPI handling, work-area centering, and icon setup.
5. For documentation-only changes, check formatting, links, and consistency with the repository.

Do not add a test framework solely for a small change unless requested or clearly beneficial.

## Response Expectations

When finishing a task, summarize:
- what changed;
- important implementation choices;
- checks performed and their results;
- anything that could not be verified.

Avoid unnecessary project-wide analysis or repeating existing code in the response.
