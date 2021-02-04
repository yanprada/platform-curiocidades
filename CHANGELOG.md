# Change Log

## Unreleased
### Bug fixes

- 2020-09-30 - Codebase & UI Update
    - Update project to the latest Django Dashboard codebase version

- Patch #4 - Whitenoise Fix - Wrong positioning in 'core/settings.py'
    - WhiteNoiseMiddleware must be positioned right after SecurityMiddleware
    - Impacted file: **core/settings.py** / MIDDLEWARE section

## [1.0.2] 2020-06-18
### Bug fixing, Improvements

- Patch #2 - Error when access `admin` path (no trailing slash)

## [1.0.1] 2020-05-30
### Bug fixing, Improvements

- Add CHANGELOG.md to track all changes
- Patch #1 - Error-404.html not used in all contexts
- Rename error pages: error-40X become page-40X
- Update LICENSE file - added more information regarding the app usage

## [1.0.0] 2020-02-07
### Initial Release
