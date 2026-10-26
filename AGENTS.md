# AION WORK distribution repository

This public repository distributes production packages for Codex and Claude Code. It is not a development, planning or review workspace.

## Public content

- Keep only production package files, marketplace metadata, installation and update instructions, public release notes, and this guide.
- Write for people installing and using the plugin. Public descriptions, commits, issues, tags and releases must not contain internal decisions, coordination notes, task or conversation metadata, or links to private resources.
- Never copy internal source documentation, protected knowledge, customer data or credentials into this repository.

## Publishing

- Develop and review changes in the owning source workspace. Do not edit generated runtime files here.
- Publish validated production builds directly to `main` with a normal fast-forward push. Do not open pull requests for generated releases or use public branches for development previews.
- Respect branch protection and release permissions. Never force-push or bypass a rejected check.
- Changed production packages require a higher version. Keep manifests, marketplace metadata and build information aligned; identical rebuilds are no-ops.
- Build and validate the package before publishing. Release notes describe user-visible changes and installation requirements only. Do not claim a release is available until publication is confirmed.
- Preserve this guide during generation. Repository-policy updates may be committed directly to `main`; they do not change the plugin version.
