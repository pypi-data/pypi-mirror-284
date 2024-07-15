# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.3.0] - 2024-07-14

### Added

- Type value verification.
- Load ComicInfo from a `cbz` file.
- Built-in reader for dynamic viewing.
- Image compatibility checking.
- Added `save` method to directly save a page or comic.
- Display additional file information via the player.

### Changed

- Complete code refactoring.
- `pages` variable now public for native page manipulation in Python.
- Optimized `pack` function with caching.
- Library now supports loading `zip` files containing only images.

### Fixed

- Default value definitions.
- Corrected values written to XML.

### New Contributors

- [piskunqa](https://github.com/piskunqa)
- [OleskiiPyskun](https://github.com/OleskiiPyskun)
- [domenicoblanco](https://github.com/domenicoblanco)
- [RivMt](https://github.com/RivMt)

## [3.2.0] - 2024-03-17

### Changed

- New code structure.
- Deleting temporary files usage.
- Automatic correction of variable types.
- Simplifying constants.
- Binary input support for pages.
- Project `pycbzhelper` renamed to `cbz`.

## [3.1.2] - 2023-08-13

### Fixed

- Fixed missing `Tags` key, thanks to @RivMt

## [3.1.1] - 2023-06-04

### Changed

- Update `README.md`.

## [3.1.0] - 2023-06-04

### Added

- Installation with pip.
- Support for non-existent location.
- Support for web loading errors of pages.

### Fixed

- Fixed page support.

### Changed

- New name of some variables.
- Automatic cleanup of temporary files.
- New location for temporary files.
- File path now uses `pathlib`.

## [3.0.1] - 2023-02-06

### Added

- Initial release.

[3.3.0]: https://github.com/hyugogirubato/cbz/releases/tag/v3.3.0
[3.2.0]: https://github.com/hyugogirubato/cbz/releases/tag/v3.2.0
[3.1.2]: https://github.com/hyugogirubato/cbz/releases/tag/v3.1.2
[3.1.1]: https://github.com/hyugogirubato/cbz/releases/tag/v3.1.1
[3.1.0]: https://github.com/hyugogirubato/cbz/releases/tag/v3.1.0
[3.0.1]: https://github.com/hyugogirubato/cbz/releases/tag/v3.0.1
