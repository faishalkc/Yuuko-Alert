# Contributing to Yuuko Alert

Thank you for your interest in contributing to Yuuko Alert!

Yuuko Alert is a small Windows desktop application built with Python, Tkinter, Pygame, and Pillow. Contributions such as bug reports, documentation improvements, and code changes are welcome.

## Before You Start

- Check the existing [issues](https://github.com/faishalkc/Yuuko-Alert/issues) to see whether the bug or suggestion has already been reported.
- For significant changes, open an issue first to discuss the proposed approach.
- Please keep contributions focused and consistent with the project's lightweight scope.

## Reporting Bugs

When opening a bug report, please include:

- A clear and descriptive title.
- Your Windows version (or other operating system, if testing the documented fallback).
- The Python version, if running from source.
- Steps to reproduce the issue.
- What you expected to happen and what actually happened.
- Relevant error messages or screenshots, if available.

Please do not include personal information, credentials, or unrelated files in reports.

## Suggesting Features

Feature suggestions are welcome. Please describe:

- The problem or use case the feature would address.
- The behavior you would expect.
- Any relevant examples or screenshots.

Since Yuuko Alert is intentionally lightweight, proposals should preserve its simple purpose and user experience.

## Development Setup

1. Fork the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/Yuuko-Alert.git
   cd Yuuko-Alert
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the application from the repository root:

   ```bash
   python main.py
   ```

The application uses relative paths for assets in `files/`, so running it from the project root is important.

## Making Changes

- Keep changes focused and avoid unrelated refactoring.
- Follow the existing Python style and use clear, descriptive names.
- Keep Windows-specific functionality in `platforms/windows.py`.
- Preserve the existing project structure unless a change requires otherwise.
- Update the README when user-facing behavior, setup, requirements, or project structure changes.
- Do not commit generated executables, virtual environments, caches, or local configuration files.
- Do not add third-party assets unless their usage and redistribution terms are understood. The project includes character artwork and audio that may have separate rights from the source code license.

## Testing

Before submitting a change:

- Run the application from the repository root and check that the greeting window appears.
- Verify that the image and audio load correctly.
- Check that the OK button closes the application.
- If changing Windows-specific behavior, test it on Windows when possible.
- Include the test environment and any checks you could not perform in your pull request.

This project currently does not define an automated test suite. Please do not claim tests were run if they were not.

## Pull Requests

1. Create a branch for your change.
2. Make your changes and commit them with a concise, descriptive message.
3. Push the branch to your fork.
4. Open a pull request against the `main` branch of this repository.
5. In the pull request description, explain the change, why it is needed, and how you tested it. Link related issues when applicable.

A maintainer may request changes before merging. Please be respectful and allow time for review.

## License and Third-Party Content

By submitting a contribution, you agree that your original contributions to the project's code and documentation are made available under the project's MIT License, as applicable.

This does not grant permission to relicense third-party artwork, audio, trademarks, or other materials included with or referenced by the project. Contributors are responsible for ensuring that submitted materials may be used and distributed appropriately.

Thank you for helping improve Yuuko Alert!
