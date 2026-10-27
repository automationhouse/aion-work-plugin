# AION WORK

AION WORK brings daily work routines, MarketingOS, SalesOS, CustomerOS, personal MIND access and team collaboration to Codex and Claude Code. The plugin connects to AION over MCP. Its skills and working methods are primarily in Polish.

This is AION's distribution repository. Installing the plugin is separate from connecting an AION account. Protected features require an eligible AION account; individual modules and resources have their own access rules. Installing this public package does not grant access to paid methods, company data or private MIND content.

## Install

Use a current version of Codex or Claude Code with plugin marketplace support. Git is required to download this marketplace. Run the commands for your client in a terminal.

### Claude Code

```sh
claude plugin marketplace add automationhouse/aion-work-plugin --scope user
claude plugin install aion-work@aion-prod --scope user
```

### Codex

```sh
codex plugin marketplace add automationhouse/aion-work-plugin
codex plugin add aion-work@aion-prod
```

You can also select AION WORK from the `aion-prod` source in Codex's plugin browser after adding the marketplace.

Start a new session after installation. Invoke the `aion-work:start` skill (in Claude Code: `/aion-work:start`) and complete the client's AION sign-in and consent flow. The server is `https://app.aionwork.com/api/mcp/work`. Never paste passwords, tokens or OAuth callback URLs into a chat or repository.

The first successful check reads your account profile and AION's core working instructions. Setup uses available materials and existing team repositories, then moves to your first task. It does not require a personal profile, a communication-style questionnaire or routine configuration. A request to prepare a repository from Company Context authorizes only the agreed source, destination and recipients; starting the plugin alone does not import or publish data. An installed plugin alone does not confirm account access. Git and Python 3.10+ are needed for the optional repository guard and folder health workflows, not for accessing remote methods alone. GitHub repository access is authorized separately from AION sign-in.

## Additional setup for your team

To extend installation for a customer's environment, add `AION_INSTALLATION.md` to the root of that customer's working repository. This is a Markdown prompt with additional steps for AION start, such as installing a required tool or preparing resources. Keep it in the customer's repository, not in the plugin package.

Start reads this file after standard repository setup and carries out the additional steps before reporting completion. If the file is absent or empty, setup continues normally. Existing permissions and approval requirements still apply. On resumption, Start checks what is already ready and completes only missing work. Ordinary work and plugin updates do not repeat these steps.

Describe each requirement, the action to take when it is missing, and how to verify success. For example:

```markdown
# Additional installation

1. Check whether the tool described in `tools/README.md` is installed.
   If missing, install it using that document's instructions.
   Verify the installed version and report any remaining sign-in step.
2. Prepare the local resources described in `resources/README.md`.
   Preserve existing files and verify that the required resources are available.
```

Reference files that actually exist in your repository. Do not include passwords or tokens. If a step is blocked, Start reports what remains incomplete while preserving the completed setup.

## Update

Updating the plugin does not refresh guard copies installed in Git hooks. Before updating, ask the agent to identify existing AION guards in the current repository and any other repositories you explicitly name, and back up their files and previous guard sources outside the repository. Do not scan the disk or clone repositories to discover guards. Skip repositories without a connected guard and process shared worktree hook directories only once.

### Claude Code

```sh
claude plugin update aion-work@aion-prod
```

Use the same installation scope if you originally chose a scope other than `user`. Automatic updates for custom marketplaces are off by default; enable them for `aion-prod` in the plugin marketplace settings if desired.

### Codex

```sh
codex plugin marketplace upgrade aion-prod
```

Refresh the installed AION WORK plugin using your client's plugin controls. If your version has no update action, remove and add only this plugin:

```sh
codex plugin remove aion-work@aion-prod
codex plugin add aion-work@aion-prod
```

After updating, ask the agent to read `references/guard.md` in the installed plugin and follow “Aktualizacja istniejącego guarda”. Refresh only verified standard AION guard installations, preserving team hooks and `core.hooksPath`. Unknown, modified or custom integrations remain unchanged with a specific integration step reported. `install` does not overwrite an old guard. Verify standard guard copies with `status` from the new script; do not commit or push just to verify them. Report the package update, each repository guard and account connection separately.

Start a new session and verify the plugin version, AION tools, profile and core instructions. Reconnect through the native sign-in flow if requested. Do not copy credentials or replace your entire client configuration.

## Move from a downloaded ZIP

If `aion-prod` already points to a local ZIP extraction, replace that marketplace registration with this GitHub source. Do not register a second AION MCP server. Note your existing source path and installation scope first, and keep the old extraction until the new installation works.

Claude Code: first inspect the configured source and installed plugins:

```sh
claude plugin marketplace list
claude plugin list
```

Proceed only when `aion-prod` is the old local ZIP marketplace, AION WORK is its only installed plugin, the marketplace is declared only at that installation's scope, and the installation is not managed. Check user, project and local settings for marketplace declarations if the CLI listings do not show their scopes. Verify that the GitHub repository is reachable and its manifests identify marketplace `aion-prod` and plugin `aion-work` before changing the local installation. Both sources use the same marketplace name, so Claude Code cannot register them side by side. The AION plugin declares no saved options or secrets. If the installed copy has any, or any check fails, stop without changing anything.

Record the old source's absolute path as `<OLD_SOURCE>` and keep that directory intact until migration succeeds. Replace `<SCOPE>` with the existing `user`, `project`, or `local` scope:

```sh
claude plugin uninstall aion-work@aion-prod --scope <SCOPE> --keep-data
claude plugin marketplace remove aion-prod --scope <SCOPE>
claude plugin marketplace add automationhouse/aion-work-plugin --scope <SCOPE>
claude plugin marketplace list
claude plugin install aion-work@aion-prod --scope <SCOPE>
claude plugin list
```

Confirm the marketplace list shows the GitHub source and the installed plugin retains its existing scope. `--keep-data` preserves Claude Code's plugin data directory. Sign in again only if the client requests it.

If any step fails after uninstalling the old plugin, stop the migration and inspect the current state. Uninstall a partially installed replacement at `<SCOPE>` with `--keep-data` if present, then remove only the newly added marketplace declaration at `<SCOPE>` if present. Restore the recorded local source with `claude plugin marketplace add "<OLD_SOURCE>" --scope <SCOPE>` only if its declaration is missing, then reinstall `aion-work@aion-prod` at `<SCOPE>` and verify the source and installed scope. Restoration may use the previous version. If recovery fails, stop and report the remaining state. A client approval denial requires approval before the blocked operation; recovery is not a way around it.

If GitHub preflight failed, leave the original installation registered. To use a newer ZIP instead, inspect it first, back up and update only that local package directory, and refresh the plugin at `<SCOPE>`. Never add a second `user` installation as a migration fallback. Use `user` only for a fresh installation.

Codex:

```sh
codex plugin remove aion-work@aion-prod
codex plugin marketplace remove aion-prod
codex plugin marketplace add automationhouse/aion-work-plugin
codex plugin add aion-work@aion-prod
```

These commands replace only the AION WORK installation and its marketplace registration. Keep your work folders, other plugins and client permissions. Complete native sign-in again if the client requests it, then verify access in a fresh session without repeating setup for an existing work folder.

## Privacy and package contents

The package contains skills, runtime references, local guard/health scripts and public OAuth client settings. It contains no account credentials, customer data or copies of protected AION methods. Private profiles and journals belong outside company repositories and shared folders. The optional guard checks files before publication; installation does not install Git hooks or run the guard.

The marketplace name is `aion-prod`, and the plugin ID is `aion-work`. Both remain stable across releases. `build-info.json` at the repository root records the released version and MCP endpoint. Native Codex and Claude manifests use separate OAuth client configurations.

## Help and releases

Use [AION WORK](https://app.aionwork.com/work-plugin) for product access and account management. Report reproducible installation problems through [GitHub Issues](https://github.com/automationhouse/aion-work-plugin/issues), including the client and plugin versions. Do not include private work content, credentials or OAuth URLs.

This repository contains generated releases. Plugin changes are maintained in the AION source repository and published here after review. Changes to bundled skills require a versioned plugin update; authorized remote methods can be updated separately. Public availability of the installation package does not grant additional rights to the AION service or its protected content.
