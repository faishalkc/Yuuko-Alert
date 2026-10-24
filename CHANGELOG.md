# Changelog

All notable changes to Yuuko Alert are documented in this file.

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Changes that have not yet been included in a release.

## [1.2] - 2026-10-11

### Changed
- Centered the application window without a visible position jump during startup.
- Centered the window within the desktop work area, accounting for the taskbar.
- Improved the alignment and spacing of the window contents.
- Adjusted the window title to prevent it from being clipped by the title bar buttons.
- Updated the text and button to use the default Windows system font.
- Increased the image size, spacing, and button size for improved readability.
- Applied consistent scaling to the window layout using a centralized setting.
- Improved image positioning to prevent clipping at the bottom edge.
- Restructured the codebase using an object-oriented design with `AlertWindow` and `SoundPlayer` classes.
- Centralized layout values, text, and file paths as class constants.
- Simplified font handling by reading the Windows system font directly.

### Maintained
- The familiar "Selamat Pagi!" greeting.
- Yuuko's image and voice playback.

## [1.1] - 2024-06-21

### Changed
- Refined display scaling handling.
- Improved integration with the Windows desktop environment.

### Maintained
- The familiar "Selamat Pagi!" greeting.
- Yuuko's image and voice playback.

## [1.0] - 2023-12-25

### Added
- Initial release of Yuuko Alert.
- Displays a cheerful "Selamat Pagi!" greeting.
- Plays Yuuko's voice when the application starts.
- Displays Yuuko's image alongside the greeting.
- Provides a simple pop-up window with an OK button.

[Unreleased]: https://github.com/faishalkc/Yuuko-Alert/compare/v1.2...HEAD
[1.2]: https://github.com/faishalkc/Yuuko-Alert/releases/tag/v1.2
[1.1]: https://github.com/faishalkc/Yuuko-Alert/releases/tag/v1.1
[1.0]: https://github.com/faishalkc/Yuuko-Alert/releases/tag/v1.0
